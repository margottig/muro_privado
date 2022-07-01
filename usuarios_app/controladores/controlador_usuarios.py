from flask import redirect, render_template, request, session
from usuarios_app.modelos.modelo_usuario import Usuario
from usuarios_app import app

app.secret_key = "estoessecreto"

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
    session['userid'] = resultado
    print("SE CREO EL USUARIO?", resultado)
    return redirect('/dashboard')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    data = {
        "id":session['userid']
    }
    usuarioLogeado = Usuario.usuarioLogeado(data)
    todos_usuarios_excepto_yo = Usuario.todos_usuarios_excepto_yo(data)
    return render_template('dashboard.html', todos_usuarios=todos_usuarios_excepto_yo, usuarioLogeado=usuarioLogeado) 


@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    usuario = Usuario.getEmail(data)
    print(usuario, "EL USUARIO EXISTE?")
    if not usuario:
        return redirect('/')
    session['userid'] = usuario[0]['id']
    return redirect('/dashboard')

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect('/')
