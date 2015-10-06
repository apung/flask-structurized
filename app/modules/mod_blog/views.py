from flask import Blueprint, render_template

mod = Blueprint('blog', __name__, url_prefix='/blog', template_folder='templates',  static_folder='static')


@mod.route('/')
def blog_home():
	return render_template("blog/home.html");