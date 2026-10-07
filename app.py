#!/usr/bin/env python3

from flask import Flask, render_template

# CRUD de animales ---
# TODO: Como integrar un motor de MySQL dentro del contenedor
# para que todos los chihuahuas se guarden en una base de datos dentro del contenedor
# y cualquiera pueda acceder a ella desde la web y ver los tipos de chihuahuas que hay en la base de datos

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
