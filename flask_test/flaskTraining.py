from flask import Flask, request, render_template

app = Flask(__name__)

"""
    # run flask app
    $ set FLASK_APP=filename.py or export FLASK_APP=filename.py
    $ flask run --host=0.0.0.0 --port=8000
    
    # debug mode or developer mode
    To enable all development features (including debug mode) you can export the FLASK_ENV environment variable and 
    set it to development before running the server:

    $ set FLASK_ENV=development or export FLASK_ENV=development
    $ flask run
    
    string  (default) accepts any text without a slash
    int     accepts positive integers
    float	accepts positive floating point values
    path	like string but also accepts slashes
    uuid	accepts UUID strings
    
    Unique URLs / Redirection Behavior
    The following two rules differ in their use of a trailing slash.
    
    URL Building
    url_for()
    
    HTTP Methods
    @app.route('/login', methods=['GET', 'POST'])
    
    Static Files
    url_for('static', filename='style.css')
    
    Rendering Templates
    
    
"""


def do_the_login():
    return True


def show_the_login_form():
    return "Logged In"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
