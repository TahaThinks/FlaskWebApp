from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "bye"


# Start the app here instead of the terminal
if __name__ == "__main__":
    app.run()
