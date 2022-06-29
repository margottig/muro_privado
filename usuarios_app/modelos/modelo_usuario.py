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
        resultado = connectToMySQL('usuarios_db').query_db(query, data)
        print(resultado, "*/"*10)
        return resultado