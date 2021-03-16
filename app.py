from flask import Flask
import flask
from flask_login import login_required, logout_user, login_user, current_user, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

from database.database import db, init_database
import database.models
from sar2019.config import Config
from flask import request, render_template, redirect, url_for, request, flash
import base64

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


with app.test_request_context():
    init_database()


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return database.models.User.query.filter_by(email=user).first()



@app.route('/')
def index():
    posts = database.models.Post.query.all()
	@@ -98,100 +82,18 @@ def delete_post(post_id=None):
    db.session.commit()
    return flask.redirect(flask.url_for('index'))\


@app.route("/comment/delete/<comment_id>")
def delete_comment(comment_id=None):
    comment = database.models.Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return flask.redirect(flask.url_for('index'))


@app.route("/search")
def search(search_string=None):
    search_result = database.models.Post.query.filter(search_string.in_(database.models.PostS.title))
    return flask.render_template("homepage.html.jinja2", posts=search_result)


@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html.jinja2")

@app.route('/signup', methods=["GET"])
def signup_form():
    return render_template("signup.html.jinja2")

@app.route('/signup', methods=["POST"])
def signup():
    username = flask.request.form.get("username")
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")

    #si le pseudo existe déjà dans la base de donnée alors un message d'erreur est envoyé
    user = database.models.User.query.filter_by(username=username).first()
    if user: #si la variable user n'est pas vide
        flash('Ce Pseudo existe déjà, réessayez')
        return redirect(url_for('signup'))

    #si l'&dresse mail existe déjà dans la base de donnée alors un message d'erreur est envoyé
    user = database.models.User.query.filter_by(email=email).first()
    if user: #si la variable user n'est pas vide
        flash('Cette adresse mail existe déjà, réessayez')
        return redirect(url_for('signup'))

    if username and email:
        user = database.models.User(
            username=username,
            email=email,
            password=generate_password_hash(
                password,
                method='sha256'))
        db.session.add(user)
        db.session.commit()

    else:
        return "Rentrez tous les champs du formulaire s'il vous plait"

    return profile()


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = database.models.User.query.filter_by(username=username).first()

        if not user :
            flash('Le pseudo que vous avez entré n\'est pas reconnu')
            return render_template("login.html.jinja2")
        if not check_password_hash(user.password, password):
            flash('Le mot de passe est incorrect')
            return render_template("login.html.jinja2")
    else:
        return render_template('login.html.jinja2')
    login_user(user)
    return render_template('profile.html.jinja2')


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("homepage.html.jinja2")


@app.route('/users')
def show_users():
    users_list = database.models.User.query.all()
    return render_template("users.html.jinja2", users_list=users_list)


if __name__ == '__main__':
    app.run()
