from flask import Flask, render_template
import requests

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


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)