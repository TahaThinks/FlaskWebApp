from flask import Flask, render_template, request
import requests
import smtplib
from personal_data import MY_EMAIL, MY_PASSWORD

app = Flask(__name__)

blog_url = "https://api.npoint.io/787ffa6facf056891dd7"
response = requests.get(url=blog_url)
all_blogs = response.json()

@app.route("/")
def home():
    print(all_blogs)
    return render_template("index.html", data=all_blogs)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_blogs:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact_page():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return f"<h1>Successfully sent your message {data['name']}</h1>"


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


# @app.route("/form-entry", methods=["POST", "GET"])
# def receive_data():
#     return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
# // Hello, I am interested in learning more about your services
