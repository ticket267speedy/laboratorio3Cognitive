import pymysql
from flask import current_app
from app.models.usuario import Usuario

class UsuarioRepository:
    
    def _get_connection(self):
        """Crea una conexión a la base de datos."""
        return pymysql.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB'],
            port=current_app.config['MYSQL_PORT'],
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def obtener_todos(self):
        """Obtiene todos los usuarios de la base de datos."""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, nombre, email, rol FROM usuarios ORDER BY id ASC"
                cursor.execute(sql)
                resultados = cursor.fetchall()
                return [Usuario.from_dict(row) for row in resultados]
        finally:
            connection.close()

    def obtener_por_id(self, usuario_id):
        """Obtiene un usuario por su ID."""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM usuarios WHERE id = %s"
                cursor.execute(sql, (usuario_id,))
                resultado = cursor.fetchone()
                return Usuario.from_dict(resultado) if resultado else None
        finally:
            connection.close()

    def obtener_por_email(self, email):
        """Obtiene un usuario por su email. (Útil para el login)"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM usuarios WHERE email = %s"
                cursor.execute(sql, (email,))
                resultado = cursor.fetchone()
                return Usuario.from_dict(resultado) if resultado else None
        finally:
            connection.close()

    def crear(self, usuario):
        """Crea un nuevo usuario en la base de datos."""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO usuarios (nombre, email, password, rol) 
                         VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql, (
                    usuario.nombre,
                    usuario.email,
                    usuario.password, # Guardaremos la contraseña aquí
                    usuario.rol
                ))
                connection.commit()
                return cursor.lastrowid
        finally:
            connection.close()

    def actualizar(self, usuario):
        """Actualiza los datos de un usuario existente."""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """UPDATE usuarios 
                         SET nombre = %s, email = %s, rol = %s 
                         WHERE id = %s"""
                cursor.execute(sql, (
                    usuario.nombre,
                    usuario.email,
                    usuario.rol,
                    usuario.id
                ))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()

    def eliminar(self, usuario_id):
        """Elimina un usuario por su ID."""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(sql, (usuario_id,))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()