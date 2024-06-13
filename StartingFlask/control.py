from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align:center'>Hello, World!</h1>"
            "<p>This is a paragraph</p>"
            "<img src='https://hips.hearstapps.com/hmg-prod/images/2023-porsche-911-dakar-122-1668632011.jpg?crop=0.598xw:0.897xh;0.163xw,0.0911xh&resize=1200:*' width='200px'></img>"
            )


@app.route("/bye")
def say_bye():
    return "bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"

# Start the app here instead of the terminal
if __name__ == "__main__":
    app.run(debug=True)
