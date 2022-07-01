from usuarios_app.config.mysqlconnection import connectToMySQL

class Mensaje:
    def __init__(self, data):
        self.id = data['id']
        self.contenid = data['contenido']
        self.de_usuario_id = data['de_usuario_id']
        self.para_usuario_id = data['para_usuario_id']


