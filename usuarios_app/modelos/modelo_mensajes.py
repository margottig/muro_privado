from usuarios_app.config.mysqlconnection import connectToMySQL

class Mensaje:
    def __init__(self, data):
        self.id = data['id']
        self.contenid = data['contenido']
        self.de_usuario_id = data['de_usuario_id']
        self.para_usuario_id = data['para_usuario_id']


    @classmethod
    def mensajes_enviados_para_mi(cls, data):
        query ="""
        SELECT * FROM mensajes JOIN usuarios on usuarios.id = mensajes.de_usuario_id
        WHERE mensajes.para_ususario_id = %(id)s;
        """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        return resultado

    @classmethod
    def enviarMensaje(cls, data):
        query = """
        INSERT INTO mensajes ( contenido, de_usuario_id, para_ususario_id) 
        VALUES (%(mensaje)s, %(de_usuario_id)s,  %(para_usuario_id)s);
            """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        return resultado

    @classmethod
    def borrarMensaje(cls, data):
        query = """
        DELETE FROM mensajes WHERE (id = %(mensaje_id)s)
        """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        return resultado