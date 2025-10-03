import os

class Config:
    # Configuración de MySQL
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DB = os.getenv('MYSQL_DB', 'flask_crud_db')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    
    # Secret key para sesiones
    SECRET_KEY = os.getenv('SECRET_KEY', 'tu-clave-secreta-aqui')