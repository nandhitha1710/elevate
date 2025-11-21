from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print("New message received:")
        print(name, email, message)
        return "Your message has been submitted successfully!"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
