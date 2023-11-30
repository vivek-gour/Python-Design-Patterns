from flask import Flask, render_template, request, send_file
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'merged_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file types
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def merge_pdfs(file_paths, output_path):
    pdf_writer = PdfFileWriter()

    for file_path in file_paths:
        pdf_reader = PdfFileReader(file_path)
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

@app.route('/', methods=['GET', 'POST'])
def merge_pdfs_route():
    uploaded_files = []

    if request.method == 'POST':
        # Check if the post request has the file part
        if 'files' not in request.files:
            return render_template('index.html', error='No file part')

        files = request.files.getlist('files')

        # If user does not select file, browser also
        # submit an empty part without filename
        if not files or all(file.filename == '' for file in files):
            return render_template('index.html', error='No selected files')

        for file in files:
            if file and allowed_file(file.filename):
                # Save the file to the uploads folder
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                uploaded_files.append(file_path)
            else:
                return render_template('index.html', error='Invalid file type. Allowed types: pdf')

        # Merge the uploaded PDF files
        merged_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
        merge_pdfs(uploaded_files, merged_file_path)

        return render_template('index.html', message='Files successfully merged', merged_file=merged_file_path)

    return render_template('index.html')

@app.route('/merged_files/merged.pdf')
def download_file():
    merged_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
    return send_file(merged_file_path)

if __name__ == '__main__':
    app.run(debug=True)
