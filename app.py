from flask import Flask, request
from flask import render_template

app = Flask(__name__)


def user_data():
    user_ip = request.remote_addr

    # Get request method
    request_method = request.method

    # Get user agent
    user_agent = request.user_agent.string

    # Get query parameters
    query_params = request.args

    # Get request headers
    headers = request.headers

    # Access cookies
    cookies = request.cookies

    # print(user_ip, request_method, user_agent, query_params, headers, cookies)

@app.route('/')
def hello_world():  # put application's code here

    # get user data
    user_data()

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
