from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email

app = Flask(__name__)
app.config["SECRET_KEY"] = "THIS IS A SECRET, DON'T DO THIS!"
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[Length(min=5)])


class RegisterForm(FlaskForm):
    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[Length(min=5)])
    repeat_password = PasswordField("repated_password", validators=[Length(min=5)])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return "it's valid"

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return "it's valid"

    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run()