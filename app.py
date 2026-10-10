#!/usr/bin/env python3

import os
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename, safe_join


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
    return render_template(
        'index.html',
        chihuahuas=chihuahuas,
        error=request.args.get('error'),
        form_data={},
        agregado=request.args.get('agregado') == '1',
    )


@app.route('/chihuahuas', methods=['POST'])
def add_chihuahua():
    tipo = request.form.get('tipo', '').strip()
    descripcion = request.form.get('descripcion', '').strip()
    
    # Recibimos el archivo físico y la ruta de texto del formulario
    file = request.files.get('imagen_file')
    imagen_path_text = request.form.get('imagen_path', '').strip()

    imagen_db = ''

    if not tipo or len(tipo) > 100:
        error = 'El tipo es obligatorio y debe tener como máximo 100 caracteres.'
    elif not descripcion:
        error = 'La descripción es obligatoria.'
    else:
        # Si el usuario seleccionó un archivo mediante el explorador
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(app.static_folder, 'images')
            os.makedirs(upload_folder, exist_ok=True)
            
            # Guardar físicamente la imagen en static/images/
            save_path = os.path.join(upload_folder, filename)
            file.save(save_path)
            
            # Ruta que se guardará en la base de datos
            imagen_db = f"images/{filename}"
        else:
            # Si se escribió manualmente una ruta existente
            imagen_db = imagen_path_text

        # Validar que la ruta de la imagen exista físicamente
        image_full_path = safe_join(app.static_folder, imagen_db)
        
        if not imagen_db or len(imagen_db) > 255 or not image_full_path or not os.path.isfile(image_full_path):
            error = 'Indica una imagen válida existente dentro de static (por ejemplo, images/chihuahua_manzana.png).'
        else:
            chihuahua = Chihuahua(tipo=tipo, descripcion=descripcion, imagen=imagen_db)
            db.session.add(chihuahua)
            db.session.commit()
            return redirect(url_for('index', agregado='1'), code=303)

    chihuahuas = Chihuahua.query.all()
    return render_template(
        'index.html',
        chihuahuas=chihuahuas,
        error=error,
        form_data=request.form,
        agregado=False,
    ), 400


# cd "C:\Python\DevOps 2026\zoo"
# docker compose up   /   docker compose up --build
# http://localhost:5000


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
