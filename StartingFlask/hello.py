from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

#Start the app here instead of the terminal
if __name__ == "__main__":
    app.run()