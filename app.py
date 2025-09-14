from flask import Flask

app = Flask(__name__)  # create Flask application

@app.route("/")  # URL route: homepage
def home():
    return "Hello, Flask!"  # response

@app.route("/welcome")
def welcome():
    return "this is home."

if __name__ == "__main__":
    app.run(debug=True)  # start development server
