from flask import Flask

def make_bold(endpoint):
    def bold():
        return f'<b>{endpoint()}</b>'
    return bold

def make_emphasis(endpoint):
    def emphasis():
        return f'<em>{endpoint()}</em>'
    return emphasis

def make_underlined(endpoint):
    def underline():
        return f'<u>{endpoint()}</u>'
    return underline

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align:center'>Hello, World!</h1>"
            "<p>This is a paragraph</p>"
            "<img src='https://hips.hearstapps.com/hmg-prod/images/2023-porsche-911-dakar-122-1668632011.jpg?crop=0.598xw:0.897xh;0.163xw,0.0911xh&resize=1200:*' width='200px'></img>"
            )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

# Start the app here instead of the terminal
if __name__ == "__main__":
    app.run(debug=True)
