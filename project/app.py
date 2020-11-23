from flask import Flask, render_template
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)
app.config["SECERET_KEY"] = "1f249004b450cee67629fe240fa36f0a"


@app.route("/")
@app.route("/welcome/<name>")
def welcome(name=None):
    if name:
        return render_template("welcome.html", name=name)
    return "Welcome to your crypto tracking platform!"


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)
