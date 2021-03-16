from flask import Flask
import flask
from database.database import db, init_database
import database.models
from sar2019.config import Config
from flask import request
import base64
from sar2019.auxiliaire import parsing

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.test_request_context():
    init_database()


@app.route('/')
def index():
    posts = database.models.Post.query.all()
    print(posts)
    return flask.render_template("homepage.html.jinja2",
                                 posts=posts)


@app.route("/posts/edit/", methods=["GET", "POST"])
@app.route("/posts/edit/<post_id>", methods=["GET", "POST"])
def create_or_process_post(post_id=None):
    # Fetch the corresponding post from the database. If no ID is provided,
    # then post will be 'None', and the form will consider this value
    # as a sign that a new post should be created
    post = database.models.Post.query.filter_by(id=post_id).first()
    form = request.form
    #form = PostEditForm(obj=post)
    if request.method=='POST':
        file = request.files['file']
        if file.filename=='':
            file=None
    else :
        file=None
    if file != None:
        if post is None:
            post = database.models.Post()
        post.user_id = 1
        post.title = form.get("title","")
        post.content = form.get("description","")
        post.tags = form.get("tags")
        post.likes = 0
        #print(post.title)
        #print(post.content)
        post.image_data = base64.b64encode(file.read())
        #print(post.image_data)
        db.session.add(post)
        db.session.commit()



        return flask.redirect(flask.url_for('index'))
    else:
        return flask.render_template('edit_post_form.html.jinja2', form=form, post=post)


@app.route("/comment/", methods=["GET", "POST"])
@app.route("/comment/<post_id>", methods=["GET", "POST"])
#@app.route("/comment/<post_id>/<comment_id>", methods=["GET", "POST"])
def comment_a_post(comment_id=None,post_id=None):
    comment = database.models.Comment.query.filter_by(id=comment_id).first()
    form = request.form
    if request.method=='POST':
        if comment is None:
            comment = database.models.Comment()

        comment.user_id = 1
        comment.post_id = form.get("post_id")
        comment.content = form.get("description")
        post = database.models.Post.query.filter_by(id=post_id).first()
        comment.post=post # permet de gérer le backpopulates de "post.comments"
        db.session.add(comment)
        db.session.commit()

        return flask.redirect(flask.url_for('index'))
    #return flask.render_template('comment_post.html.jinja2', post_id=post_id,form=form, comment=comment)


@app.route("/posts/delete/<post_id>")
def delete_post(post_id=None):
    post = database.models.Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return flask.redirect(flask.url_for('index'))\


@app.route("/comment/delete/<comment_id>")
def delete_comment(comment_id=None):
    comment = database.models.Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return flask.redirect(flask.url_for('index'))


@app.route("/search", methods=["GET", "POST"])
def search():
    form =request.form
    search_string = form.get("search_string")
    search_result = database.models.Post.query.filter((database.models.Post.tags.contains(search_string))).all()
    print(search_result)
    return flask.render_template("homepage.html.jinja2", posts=search_result)


if __name__ == '__main__':
    app.run()
