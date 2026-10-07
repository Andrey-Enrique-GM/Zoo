#!/usr/bin/env python3

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# CRUD de animales ---
# TODO: Como integrar un motor de MySQL dentro del contenedor
# para que todos los chihuahuas se guarden en una base de datos dentro del contenedor
# y cualquiera pueda acceder a ella desde la web y ver los tipos de chihuahuas que hay en la base de datos

app = Flask(__name__)

# Configuración de la conexión a MySQL usando SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 
    'mysql+pymysql://zoo_user:zoo_password@db/zoo_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para la tabla de chihuahuas
class Chihuahua(db.Model):
    __tablename__ = 'chihuahuas'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    imagen = db.Column(db.String(255), nullable=False)


@app.route('/')
def index():
    chihuahuas = Chihuahua.query.all()
    return render_template('index.html', chihuahuas=chihuahuas)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
