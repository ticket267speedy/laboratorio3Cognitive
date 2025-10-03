import pymysql
from flask import current_app
from app.models.curso import Curso

class CursoRepository:
    
    def _get_connection(self):
        """Crear conexión a la base de datos"""
        return pymysql.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB'],
            port=current_app.config['MYSQL_PORT'],
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def obtener_todos(self):
        """Obtener todos los cursos"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM cursos ORDER BY id DESC"
                cursor.execute(sql) # execute configura la BDsql
                resultados = cursor.fetchall()
                return [Curso.from_dict(row) for row in resultados]
        finally:
            connection.close()
    
    def obtener_por_id(self, curso_id):
        """Obtener un curso por ID"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM cursos WHERE id = %s"
                cursor.execute(sql, (curso_id,))
                resultado = cursor.fetchone()
                return Curso.from_dict(resultado) if resultado else None
        finally:
            connection.close()
    
    def crear(self, curso):
        """Crear un nuevo curso"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO cursos (nombre, creditos) 
                         VALUES (%s, %s)"""
                cursor.execute(sql, (
                    curso.nombre,
                    curso.creditos
                ))
                connection.commit()
                return cursor.lastrowid
        finally:
            connection.close()
    
    def actualizar(self, curso):
        """Actualizar un curso existente"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """UPDATE cursos 
                         SET nombre = %s, creditos = %s 
                         WHERE id = %s"""
                cursor.execute(sql, (
                    curso.nombre,
                    curso.creditos,
                    curso.id
                ))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()
    
    def eliminar(self, curso_id):
        """Eliminar un curso"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM cursos WHERE id = %s"
                cursor.execute(sql, (curso_id,))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()