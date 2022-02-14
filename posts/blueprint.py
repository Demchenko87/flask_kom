from flask import Blueprint, render_template
from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def blog():
    posts = Post.query.all()
    return render_template('posts/blog.html', posts=posts)

@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('posts/post.html', post=post)
