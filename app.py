from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "1234567890"


from flask import render_template, redirect, url_for
import sqlite3
from forms import Create_ChangeForm, DeleteForm

@app.route("/", methods=["GET", 'POST'])
def index():
    form = DeleteForm()
    conn = sqlite3.connect("database.db")
    if form.validate_on_submit():
        nums = form.num.data.split()
        for i in nums:
            conn.execute("DELETE FROM posts WHERE id = ?", (int(i),))
        conn.commit()
    return render_template("index.html", form=form, posts= conn.execute("SELECT * FROM posts").fetchall())

@app.route("/create", methods=["GET", 'POST'])
def create():
    form = Create_ChangeForm()
    if form.validate_on_submit():
        conn = sqlite3.connect("database.db")
        nums = conn.execute("SELECT id FROM posts").fetchall()
        if len(nums) == 0:
            a = 1
        else:
            a = int(nums[len(nums)-1][0])+1
        conn.execute("INSERT INTO posts VALUES(?, ?)", ((a), form.content.data))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("create.html", form=form)

@app.route("/change/<string:id>", methods=["GET", 'POST'])
def change(id):
    id = str(id)
    form = Create_ChangeForm()
    if form.validate_on_submit():
        conn = sqlite3.connect("database.db")
        conn.execute("DELETE FROM posts WHERE id = ?", (id,))
        conn.execute("INSERT INTO posts VALUES(?, ?)", (id, form.content.data))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template('change.html', form=form)

