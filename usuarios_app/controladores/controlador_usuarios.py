from flask import flash, redirect, render_template, request, session
from usuarios_app.modelos.modelo_mensajes import Mensaje
from usuarios_app.modelos.modelo_usuario import Usuario
from usuarios_app import app
from flask_bcrypt import Bcrypt        

bcrypt = Bcrypt(app)     
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
    # if request.form['password'] != request.form['confirm_psw']:
    validacion = Usuario.validaciones_formulario(request.form)
    if validacion == True:
        psw_hash = bcrypt.generate_password_hash(request.form['password'])
        data['password'] = psw_hash
    #     data = {
    #     "nombre":request.form['nombre'],
    #     "apellido": request.form['apellido'],
    #     "email": request.form['email'],
    #     "password": psw_hash
    # }
        resultado =  Usuario.nuevoUsuario(data)
        session['userid'] = resultado
        return redirect('/dashboard')
    # flash("No coincide psw", 'psw')
    return redirect('/')
    # print("SE CREO EL USUARIO?", resultado)
   


@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'userid' not in session:
        return redirect('/')
    data = {
        "id":session['userid']
    }
    usuarioLogeado = Usuario.usuarioLogeado(data)
    todos_usuarios_excepto_yo = Usuario.todos_usuarios_excepto_yo(data)
    mensajes_enviados_para_mi = Mensaje.mensajes_enviados_para_mi(data)

    return render_template('dashboard.html', todos_usuarios=todos_usuarios_excepto_yo, usuarioLogeado=usuarioLogeado, mensajes_para_mi = mensajes_enviados_para_mi ) 


@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
   
    usuario = Usuario.getEmail(data)
    print(usuario, "QUE CONTIENE USUARIO"*10)
    print(usuario, "EL USUARIO EXISTE?")
    if not usuario:
        flash("Informacion no valida", "invalid_psw")
        return redirect('/')
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash('Password invalido', 'invalid_psw')
        return redirect('/')

    session['userid'] = usuario.id
    return redirect('/dashboard')

@app.route("/enviarmensaje/<int:para_usuario_id>", methods=['POST'])
def enviarMensaje(para_usuario_id):
    data = {
        "mensaje":request.form['mensaje'],
        "para_usuario_id": para_usuario_id,
        "de_usuario_id": session['userid']
    }
    print(data, "DATA PARA ENVIAR MENSAJE")
    validacion = Mensaje.validaciones_formulario_mensajes(request.form)
    if validacion == True:
        enviar_mensaje = Mensaje.enviarMensaje(data)
        return redirect("/dashboard")
    return redirect("/dashboard")

@app.route('/borrarmensaje/<int:id_mensaje>', methods=['GET'])
def borrarMensaje(id_mensaje):
    data = {
        "mensaje_id":id_mensaje
    }
    borrarMensaje = Mensaje.borrarMensaje(data)
    return redirect('/dashboard')



@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect('/')
