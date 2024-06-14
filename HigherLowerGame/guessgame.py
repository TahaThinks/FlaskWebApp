from flask import Flask
import random

number = random.randint(0, 9)
print(number)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp">')

@app.route("/<int:user_guess>")
def guessed_number(user_guess):
    if user_guess > number:
        return ('<h1>Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    if user_guess < number:
        return ('<h1>Too Low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    else:
        return ('<h1>You Found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)
