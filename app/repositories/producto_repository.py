import pymysql
from flask import current_app
from app.models.producto import Producto

class ProductoRepository:
    
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
        """Obtener todos los productos"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM productos ORDER BY id DESC"
                cursor.execute(sql) # execute configura la BDsql
                resultados = cursor.fetchall()
                return [Producto.from_dict(row) for row in resultados]
        finally:
            connection.close()
    
    def obtener_por_id(self, producto_id):
        """Obtener un producto por ID"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM productos WHERE id = %s"
                cursor.execute(sql, (producto_id,))
                resultado = cursor.fetchone()
                return Producto.from_dict(resultado) if resultado else None
        finally:
            connection.close()
    
    def crear(self, producto):
        """Crear un nuevo producto"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO productos (nombre, descripcion, precio, cantidad) 
                         VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql, (
                    producto.nombre,
                    producto.descripcion,
                    producto.precio,
                    producto.cantidad
                ))
                connection.commit()
                return cursor.lastrowid
        finally:
            connection.close()
    
    def actualizar(self, producto):
        """Actualizar un producto existente"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = """UPDATE productos 
                         SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s 
                         WHERE id = %s"""
                cursor.execute(sql, (
                    producto.nombre,
                    producto.descripcion,
                    producto.precio,
                    producto.cantidad,
                    producto.id
                ))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()
    
    def eliminar(self, producto_id):
        """Eliminar un producto"""
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM productos WHERE id = %s"
                cursor.execute(sql, (producto_id,))
                connection.commit()
                return cursor.rowcount > 0
        finally:
            connection.close()