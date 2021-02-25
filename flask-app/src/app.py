from flask import Flask, render_template, render_template_string, request, session, redirect, url_for, logging, flash
from data import posts
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from datetime import date
from forms import RegisterForm, PostForm, ContactForm
from functools import wraps
import json

app = Flask(__name__)

app.debug = True

postsCollection = posts()

# MYSQL Connection Properties 
app.config['MYSQL_HOST'] = '192.168.0.103'
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
            print("session is logged in")
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
    result = cur.execute("SELECT id, title, left(body, 500) as body, author, create_date FROM posts order by id DESC")
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
    return render_template("about.html")

# /about
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm(request.form)
    if request.method == 'POST' and contact_form.validate():

        name = contact_form.name.data
        email = contact_form.email.data
        company = contact_form.company.data
        notes = contact_form.notes.data

        # Create Connection
        cur = mysql.connection.cursor()

        # Insert Data
        cur.execute("INSERT INTO contacts(id, name, company, email, note) values(null, %s, %s, %s, %s)", (name, company, email, notes))

        # Commit to DB
        mysql.connection.commit()

        flash("Thanks you submitting contact", "info")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=contact_form)

# Add Route register
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
@app.route("/dashboard")
@is_logged_in
def dashboard():

    author = session['name']
    # Create Cursor
    cur = mysql.connection.cursor()
    # Execute Query
    res = cur.execute("SELECT id, title, left(body, 50) as body, author, create_date FROM posts WHERE author = %s", [author])

    if res > 0:
        # Fetch all Post
        post_list = cur.fetchall()
        return render_template("dashboard.html", post_list=post_list)
    else:
        return render_template("dashboard.html")


# Add Post Route
@app.route("/dashboard/add_post", methods=['GET', 'POST'])
@is_logged_in
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

# Add Edit Route
@app.route("/dashboard/edit_post/<string:id>", methods=['GET', 'POST'])
@is_logged_in
def edit_post(id):
    post_form = PostForm(request.form)
    if request.method ==  "POST" and post_form.validate():
        title = post_form.title.data
        body = post_form.body.data
        _id = post_form.id.data

        print("_id", _id)
        # Create Cursor
        cur = mysql.connection.cursor()
        # Interting POST
        cur.execute("UPDATE posts SET title = %s, body = %s WHERE id = %s ", (title, body, _id))
        # Commiting Transcation
        mysql.connection.commit()
        # Close Cursor
        cur.close()
        flash("Post Updated", "info")
        return redirect(url_for("dashboard"))
    # Create Cursor
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM posts WHERE id = %s ", [id])
    if result > 0:
        post = cur.fetchone()
        post_form = PostForm(request.form, id=post['id'], title=post['title'], body=post['body'])
    return render_template("dashboard.html", form=post_form, edit_post=True)


# Delete Post
@app.route("/dashboard/delete_post/<string:id>", methods=['POST'])
@is_logged_in
def delete_post(id):
    print("_id to Delete", id)
    # Create Cursor
    cur = mysql.connection.cursor()
    # Interting POST
    cur.execute("DELETE FROM posts WHERE id = %s ", [id])
    # Commiting Transcation
    mysql.connection.commit()
    # Close Cursor
    cur.close()
    flash("Post Delete", "danger")
    return redirect(url_for("dashboard"))



# logout Route
@app.route("/logout")
@is_logged_in
def logout():
    # Method to log session out
    session.clear()
    flash("Logout Susscess", "info")
    return redirect(url_for("index"))


@app.route("/search")
def search():
    return render_template("search.html")




#Tests routes
@app.route("/sample")
def sample_data():
    # Sample Methos
    return render_template("sample-data.html", sample_count = list(range(20)))

@app.route("/hello")
def hello():
    return "Hello Flask!"

@app.route("/rendered")
def render_html():
    return render_template_string("<h1>Rendered HTML {{name}}</h1>", name="Digivjay")

@app.route("/idea")
def idea():
    return render_template("sample-idea.html")

@app.route("/post-collection")
def getPostCollection():
    return json.dump(postsCollection);


if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run()