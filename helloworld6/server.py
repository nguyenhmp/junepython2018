from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "adsfkla;jewiunx.,nvdsjf"

@app.route("/")
def index():
    if not "users" in session:
        session["users"] = []
    user_length = len(session["users"])
    return render_template("index.html", length=user_length, students=session["users"])

@app.route("/process_data", methods=["POST"])
def process():
    session["users"].append(
        {"first_name":request.form["first_name"], "last_name":request.form["last_name"]}
    )
    session.modified = True
    return redirect("/")

@app.route("/nuke")
def nuke_session():
    session.clear()
    return redirect("/")

@app.route("/ninja/<color>")
def display_ninja(color):
    return render_template("index.html", chosen_color=color)


app.run(debug=True)