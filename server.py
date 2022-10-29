from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_folder>/<string:page_name>")
def about(page_folder=None,page_name="index.html"):
    return render_template(page_folder + "/" + page_name)


