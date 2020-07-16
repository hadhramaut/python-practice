from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create DB using the next commands:
# from app import db
# db.create_all()

class Article(db.Model):
    # Creating columns in DB for needed fields
    article_id = db.Column(db.Integer, primary_key=True)  # This field should be unique. Will be set by default
    title = db.Column(db.String(100), nullable=False)  # Don't allow setting empty title
    intro = db.Column(db.String(300), nullable=False)  # Don't allow setting empty intro
    text = db.Column(db.Text, nullable=False)  # Don't allow setting empty intro
    date = db.Column(db.DateTime, default=datetime.utcnow)  # Set actual date during article creation

    def __repr__(self):
        return f'<Article {self.article_id}>'


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/posts')
def posts():
    # Make call to DB via any class and get all available data. Sort output by date
    post_articles = Article.query.order_by(Article.date.desc()).all()  # desc() - from new to old
    # `post_articles` will be used as arg in posts.html. Better to define the same name as for variable above
    return render_template('posts.html', post_articles=post_articles)


@app.route('/posts/<int:post_id>')
def detailed_post(post_id):
    article = Article.query.get(post_id)  # Get ID of required article
    return render_template('detailed_post.html', article=article)


@app.route('/create-article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        # Create object
        article = Article(title=title, intro=intro, text=text)

        # Save object in database
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')  # Redirect to page with posts after article is created
        except:
            return "При добавлении статьи произошла ошибка!"

    else:
        return render_template('create-article.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, user_id):
    return f"User page: {name} with id={user_id}"


if __name__ == '__main__':
    app.run(debug=True)

# Lesson 2: https://www.youtube.com/watch?v=crUHP8Zo12k
