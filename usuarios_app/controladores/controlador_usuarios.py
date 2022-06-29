from flask import redirect, render_template, request
from usuarios_app.modelos.modelo_usuario import Usuario
from usuarios_app import app

@app.route('/', methods=['GET'])
def raiz():
    return render_template('index.html')

@app.route('/nuevousuario', methods=["POST"])
def agregarUsuario():
    data = {
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    resultado =  Usuario.nuevoUsuario(data)
    print("SE CREO EL USUARIO?", resultado)
    return redirect('/')