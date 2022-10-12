from flask import request, flash
from usuarios_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PSW_REGEX =  re.compile(r'^[A-Za-z0-9@#$%^&+=]{8,}$')
class Usuario:
    def __init__(self, diccionario):
        self.id = diccionario['id']
        self.nombre=diccionario['nombre']
        self.apellido = diccionario['apellido']
        self.email = diccionario['email']
        self.password = diccionario['password']
    
    @classmethod
    def nuevoUsuario(cls, data):
        query = """
        INSERT INTO usuarios(nombre, apellido, email, password)
         VALUES (%(nombre)s,%(apellido)s, %(email)s, %(password)s);
        """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        print(resultado, "*/"*10)
        return resultado

    @classmethod
    def getEmail(cls, data):
        query = """
        SELECT * FROM usuarios WHERE email = %(email)s;
        """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        print(resultado, "/="*5)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])
        
    @classmethod
    def todos_usuarios_excepto_yo(cls, data):
        query = """
        SELECT * FROM usuarios WHERE id != %(id)s;
        """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        print("TODOS USUSARIOS MENOS YO", resultado)
        return resultado

    @classmethod
    def usuarioLogeado(cls, data):
        query = """
        SELECT * FROM usuarios WHERE id = %(id)s;
        """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        print("USUARIO LOGEADO", resultado)
        return cls(resultado[0])

    @staticmethod
    def validaciones_formulario(formulario):
        is_valid=True
        if len(formulario['nombre'])< 2:
            flash("Nombre no puede contener menos de 2 caracteres", 'errorNombre' )
            is_valid = False
        if len(formulario['apellido']) <2:
            flash("Apellido no puede conteneenos de 2 caracteres", 'errorNombre' )
            is_valid = False
        if not EMAIL_REGEX.match(formulario['email']): 
            flash("Email incorrecto", "email")
            is_valid = False
        if not PSW_REGEX.match(formulario['password']):
            flash("Contraseña debe tener al menos 8 caracteres, letras mayúsculas", "email")
            is_valid = False
        if request.form['password'] != request.form['confirm_psw']:
            flash ("Contrasenias no coinciden", "psw")
            is_valid = False
        return is_valid

          