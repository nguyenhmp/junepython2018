from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "my secret key"

@app.route("/", methods=["GET"])
def index():
        if not "users" in session:
        session["users"] = []
    display_message = len(session["users"]) == 0
    return render_template("index.html", something="Minh", students=session["users"], no_users=display_message)

@app.route("/hello", methods=["GET"])
def hello_world():
    return "asrewuaofsd"

@app.route("/process", methods=["POST"])
def process_data():
    session["users"].append({"first_name":request.form["first_name"], "last_name":request.form["last_name"]})
    session.modified = True
    return redirect("/")

@app.route("/nuke")
def nuke():
    session.clear()
    return redirect("/")
app.run(debug=True)

