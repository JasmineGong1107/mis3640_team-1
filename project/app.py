from flask import Flask, render_template, flash, redirect
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)
app.config["SECERET_KEY"] = "1f249004b450cee67629fe240fa36f0a"


@app.route("/")
@app.route("/home/<name>")
def home(name=None):
    if name:
        return render_template("home.html", name=name)
    else:
        return "Welcome to your crypto tracking platform!"


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account Created for{form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
