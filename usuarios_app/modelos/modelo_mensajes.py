from usuarios_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime
import math 
class Mensaje:
    def __init__(self, data):
        self.id = data['id']
        self.contenido = data['contenido']
        self.de_usuario_id = data['de_usuario_id']
        self.para_usuario_id = data['para_usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    def tiempo(self):
        ahora = datetime.now()
        diferencia = ahora - self.created_at
        if diferencia.days > 0:
            return f'{diferencia.days} dias atras'
        elif diferencia.total_seconds() >= 60:
            return f'{math.floor(diferencia.total_seconds()/60)} minutos atras'
        else:
            return f"{diferencia.total_seconds()} segundos atras"

    @classmethod
    def mensajes_enviados_para_mi(cls, data):
        query ="""
        SELECT * FROM mensajes JOIN usuarios on usuarios.id = mensajes.de_usuario_id
        WHERE mensajes.para_usuario_id = %(id)s;
        """
        resultado = connectToMySQL('muro_privado').query_db(query, data)
        mensajes = []
        for mensaje in resultado:
            mensajes.append(cls(mensaje))
        return mensajes

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

    @staticmethod
    def validaciones_formulario_mensajes(formulario):
        is_valid=True
        if len(formulario['mensaje']) < 5:
            flash("Escribe algo más", 'errorNombre' )
            is_valid = False
        return is_valid