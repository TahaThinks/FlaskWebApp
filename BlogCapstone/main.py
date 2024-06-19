from flask import Flask, render_template, request
import requests
from smtplib import SMTP

app = Flask(__name__)


@app.route("/")
def home():
    blog_url = "https://api.npoint.io/787ffa6facf056891dd7"
    response = requests.get(url=blog_url)
    all_blogs = response.json()
    print(all_blogs)
    return render_template("index.html", data=all_blogs)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact_page():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        data = request.form
        return f"<h1>Successfully sent your message {data['name']}</h1>"



# @app.route("/form-entry", methods=["POST", "GET"])
# def receive_data():
#     return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
# // Hello, I am interested in learning more about your services