from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'


if __name__ == '__main__':
    app.run(debug=True)
