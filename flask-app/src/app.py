from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sample")
def sample_data():
    return render_template("sample-data.html", sample_count = range(20))



@app.route("/hello")
def hello():
    return "Hello Flask!"



if __name__ == "__main__":
    app.run()