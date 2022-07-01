from unittest import result
from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre=nombre
        self.apellido = apellido
        self.email = email
        self.password = password

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
        return resultado
        
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
        return resultado