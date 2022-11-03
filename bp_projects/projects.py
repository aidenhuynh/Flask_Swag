from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

@app_projects.route('/sabinesblog/')
def sabinesblog():
    return render_template("sabinesblog.html")

@app_projects.route('/dashsblog/')
def dashsblog():
    return render_template("dashsblog.html")

@app_projects.route('/aidensblog/')
def aidensblog():
    return render_template("aidensblog.html")

@app_projects.route('/ahadsblog/')
def ahadsblog():
    return render_template("ahadsblog.html")

@app_projects.route('/whosthatpokemon/')
def whosthatpokemon():
    return render_template("whosthatpokemon.html")

@app_projects.route('/tetris/')
def tetris():
    return render_template("tetris.html")

@app_projects.route('/flappybird/')
def flappybird():
    return render_template("flappybird.html")