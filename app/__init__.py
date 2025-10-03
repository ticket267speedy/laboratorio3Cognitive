from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config.from_object('app.config.Config')
    
    from app.controllers.producto_controller import producto_bp
    app.register_blueprint(producto_bp, url_prefix='/productos')
    
    from app.controllers.curso_controller import curso_bp
    app.register_blueprint(curso_bp, url_prefix='/cursos')
    
    # Registro del nuevo Blueprint de Usuarios y Login
    from app.controllers.usuario_controller import usuario_bp
    # Registro sin prefijo para que sobresalga sobre el resto, porque se trata de la plantilla de las clases pasadas
    app.register_blueprint(usuario_bp)
    
    return app