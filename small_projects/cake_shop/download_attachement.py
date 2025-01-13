import os
import imaplib
import email
from email.header import decode_header
import shutil


def download_attachments(username, app_password, sender_emails, download_folder):
    # Connect to the Gmail server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    # Login with your Gmail credentials
    mail.login(username, app_password)

    # Select the mailbox you want to read (e.g., 'inbox')
    mail.select('inbox')

    # Search for all emails from the specified sender
    for sender_email in sender_emails:
        company = sender_email.split('@')[-1].replace('.com', '').replace('.in', '')
        status, messages = mail.search(None, f'(FROM "{sender_email}")')
        if status == 'OK':
            for num in messages[0].split():
                # Fetch the email by its ID (num)
                status, msg_data = mail.fetch(num, '(RFC822)')

                if status == 'OK':
                    # Parse the email content
                    email_message = email.message_from_bytes(msg_data[0][1])
                    # Get the email subject
                    # subject, encoding = decode_header(email_message["Subject"])[0]
                    # if isinstance(subject, bytes):
                    #     subject = subject.decode(encoding if encoding else 'utf-8')
                    #
                    # # Print email details
                    # print(f"Subject: {subject}")

                    # Download attachments
                    for part in email_message.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue

                        filename = part.get_filename().replace('/', '')
                        if 'zip' in filename or 'xlsx' in filename:
                            filepath = os.path.join(download_folder, company, filename)

                            # Save the attachment to the specified folder
                            with open(filepath, 'wb') as f:
                                f.write(part.get_payload(decode=True))

    # Logout and close the connection
    mail.logout()


# Replace 'your_email@gmail.com', 'your_app_password', 'sender_email@example.com',
# and '/path/to/download/folder' with your actual values
# download_attachments('vikas59u@gmail.com', 'onacicjfjfgnalhp', ['payments@swiggy.in'], 'E:/Download_Folder')
# emails 'billing@zomato.com',
# 'vikas59u@gmail.com',  'onacicjfjfgnalhp' 'viv30ek@gmail.com', 'qxebwfevvcfmjlwm'

def move_file_to_folder(word, source_folder):
    target_folder = os.path.join(source_folder, word)
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Check if the target folder exists, and create it if not
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Target folder '{target_folder}' created.")

    for file_name in os.listdir(source_folder):
        if word in file_name and '.' in file_name:
            # Construct the full paths for the source file and the target folder
            source_file_path = os.path.join(source_folder, file_name)
            target_file_path = os.path.join(target_folder, file_name)

            # Check if the source file exists
            if os.path.exists(source_file_path):
                # Move the file to the target folder
                shutil.move(source_file_path, target_file_path)
                print(f"File '{file_name}' moved to '{target_folder}'.")
            else:
                print(f"File '{file_name}' not found in '{source_folder}'.")


# Replace 'file_to_move.txt', 'source_folder', and 'target_folder'
# with your actual values
move_file_to_folder('2023', 'E:/Download_Folder/swiggy')
