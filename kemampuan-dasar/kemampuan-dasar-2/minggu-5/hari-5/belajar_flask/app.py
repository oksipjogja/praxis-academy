from flask import Flask # render_template
from markupsafe import escape
from flask_pymongo import PyMongo 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/kampus"
mongo = PyMongo(app)

@app.route("/")
def home_page():
  online_users = mongo.db.users.find({"online": True})
  # return render_template("index.html", online_users=online_users)


# app = Flask(__name__)
# if __name__ == '__main__':
#   app.run(port=80, debug=True)

# @app.route("/")
# def index():
#   return "index.pagi"
  # ------------------------------------
# @app.route("/syafak")
# def hai():
  # return "Assalam Mualaikum Warahtullahi Wabarokatuh!!"
  # -------------------------------------
# @app.route('/')
# def index():
#   return render_template('index.html')
  # -------------------------------------
# @app.route("/<Doni>")
# def hello(name):
#   return f"Hello, {escape(name)}"
# --------------------------------------
# @app.route('/user/<Adi>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'
# -----------------------------------------------------------------
# @app.route("/users", methods=["POST"])
# def create_user():
#   return "X"
