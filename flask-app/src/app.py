from flask import Flask, render_template, render_template_string, request, session, redirect, url_for, logging, flash
from data import posts
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from datetime import date
from forms import RegisterForm, PostForm
from functools import wraps

app = Flask(__name__)

app.debug = True

postsCollection = posts()

# MYSQL Connection Properties 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'temp'
app.config['MYSQL_PASSWORD'] = 'temp'
app.config['MYSQL_DB'] = 'flaskBookStore'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # by default it is tuple

# Init MySQL
mysql = MySQL(app)

# Filter
# Filter filter_trimed
def filter_trimed(s, count=100):
    return s[:count]
app.jinja_env.filters['trimed'] = filter_trimed

@app.template_filter('uppar')
def filter_uppar(s):
    return s.upper()

@app.template_filter('date_format')
def date_format(d):
    if type(d) is date:
        return d.strftime("%A %d. %B %Y")
    return d

# Check if user logged in

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return  f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for("login"))
    return wrap



# App Routes
# Index
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# /blog
@app.route("/blog")
def blog():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT id, title, left(body, 500) as body, author, create_date FROM posts ")
    postsDB = cur.fetchall()
    return render_template("blog.html", posts=postsDB)

# /blog/post/{id}
@app.route("/blog/post/<string:id>")
def post(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM posts  WHERE id = %s", [id])
    postsDB = cur.fetchone()
    return render_template("post.html", post=postsDB)

# /about
@app.route("/about")
def about():
    return render_template("index.html")

# /about
@app.route("/contact")
def contact():
    return render_template("index.html")

# /register
@app.route("/register", methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm(request.form)
    if request.method == 'POST' and reg_form.validate():
        name = reg_form.name.data
        email = reg_form.email.data
        username = reg_form.username.data
        password = sha256_crypt.encrypt(str(reg_form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()
        # Execute query
        cur.execute("INSERT INTO user(name, email, username, password, creation_date) VALUES(%s, %s, %s, %s, curdate())", (name, email, username, password))
        # Commit to DB
        mysql.connection.commit()
        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=reg_form)

# /login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        loginId = request.form['loginId']
        inputPassword = request.form['passwordInput']

        # Create cursor
        cur = mysql.connection.cursor()

        # Execute Query
        result = cur.execute("SELECT * FROM user  WHERE username = %s", [loginId])

        if result > 0:
            # Fetching Data
            user = cur.fetchone()
            password = user['password']

            if sha256_crypt.verify(inputPassword, password):
                session['logged_in'] = True
                session['username'] = loginId
                session['name'] = user['name']

                flash('You are now logged in', 'success')

                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

        mysql.connection.commit()
        cur.close()
    return render_template("login.html")

# Dashboard Route
@is_logged_in
@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


# Add Post Route
@is_logged_in
@app.route("/dashboard/add_post", methods=['GET', 'POST'])
def add_post():
    post_form = PostForm(request.form)
    if request.method ==  "POST" and post_form.validate():
        title = post_form.title.data
        body = post_form.body.data
        author = session['name']
        # Create Cursor
        cur = mysql.connection.cursor()
        # Interting POST
        cur.execute("INSERT INTO posts(title, body, author, create_date) VALUES(%s, %s, %s, curdate())", (title, body, author))
        # Commiting Transcation
        mysql.connection.commit()
        # Close Cursor
        cur.close()
        flash("Post Saved", "info")
        return redirect(url_for("dashboard"))
    return render_template("dashboard.html", form=post_form, add_post=True)

# logout Route
@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    flash("Logout Susscess", "info")
    return redirect(url_for("index"))



# Tests routes
@app.route("/sample")
def sample_data():
    return render_template("sample-data.html", sample_count = range(20))

@app.route("/hello")
def hello():
    return "Hello Flask!"

@app.route("/rendered")
def render_html():
    return render_template_string("<h1>Rendered HTML {{name}}</h1>", name="Digivjay")

@app.route("/idea")
def idea():
    return render_template("sample-idea.html")


if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run()