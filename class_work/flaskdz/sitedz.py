from flask import Flask, render_template, url_for, request, flash, session, redirect, g
from SFData import SFData
import os
import sqlite3


DATABASE = "fsk.db"
SECRET_KEY = "e73d2be26f725632aa92b3e94a7c5d9980043ea0"
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'fsk.db')))


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('slite_db.sql', 'r') as f:
        db.cursor().executescript(f.read())


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
@app.route("/catalog")
def catalog():
    dbase = get_db()
    db = SFData(dbase)
    return render_template('index.html', menu=db.get_menu(), title="Каталог курсов", courses=db.get_course_announce())


@app.route("/add_course", methods=["POST", "GET"])
def add_course():
    dbase = get_db()
    db = SFData(dbase)

    if request.method == "POST":
        if len(request.form['name']) > 5 and len(request.form['price']) > 4 and len(request.form['url']) and len(request.form['course_info']) > 10:
            res = db.add_course(request.form['name'], request.form['price'], request.form['url'], request.form['course_info'])
            if not res:
                flash("Ошибка добавления курса!", category="error")
            else:
                flash("Курс успешно добавлен!", category="success")
        else:
            flash("Ошибка ввода данных", category="error")

    return render_template("add_course.html", menu=db.get_menu(), title="Добавить курс")


@app.route("/course/<alias>")
def show_course(alias):
    dbase = get_db()
    db = SFData(dbase)
    title, price, info = db.get_course(alias)
    return render_template("course.html", menu=db.get_menu(), title=title, price=price, info=info)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == '__main__':
    app.run()



