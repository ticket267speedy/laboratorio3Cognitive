from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, session, g
)
from functools import wraps
from app.services.usuario_service import UsuarioService

# Creación del Blueprint para el controlador de usuarios
usuario_bp = Blueprint('usuarios', __name__)
usuario_service = UsuarioService()

# Decorador para proteger rutas que requieren login
def login_required(view):
    """
    Decorador que redirige a la página de login si el usuario no está autenticado.
    """
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Debes iniciar sesión para acceder a esta página.', 'error')
            return redirect(url_for('usuarios.login'))
        return view(**kwargs)
    return wrapped_view

@usuario_bp.before_app_request
def load_logged_in_user():
    """
    Carga los datos del usuario desde la sesión en cada petición.
    """
    user_id = session.get('user_id')
    g.user = usuario_service.obtener_usuario(user_id) if user_id else None

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Maneja el inicio de sesión del usuario"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        usuario = usuario_service.verificar_credenciales(email, password)
        
        if usuario:
            session.clear()
            session['user_id'] = usuario.id
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('usuarios.index'))
        else:
            flash('Email o contraseña incorrectos.', 'error')
    
    return render_template('laboTres/login.html')

@usuario_bp.route('/logout')
def logout():
    """Cierra la sesión del usuario"""
    session.clear()
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('usuarios.login'))

@usuario_bp.route('/')
@login_required
def index():
    """Muestra la lista de todos los usuarios"""
    usuarios = usuario_service.listar_usuarios()
    return render_template('laboTres/usuarios/index.html', usuarios=usuarios)

@usuario_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    """Crea un nuevo usuario"""
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'rol': request.form.get('rol')
        }
        resultado = usuario_service.crear_usuario(datos)
        if resultado['success']:
            flash('Usuario creado exitosamente.', 'success')
            return redirect(url_for('usuarios.index'))
        else:
            for error in resultado.get('errores', []):
                flash(error, 'error')
    
    return render_template('laboTres/usuarios/crear.html')

@usuario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    """Edita un usuario existente"""
    usuario = usuario_service.obtener_usuario(id)
    if not usuario:
        flash('Usuario no encontrado.', 'error')
        return redirect(url_for('usuarios.index'))

    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'rol': request.form.get('rol')
        }
        resultado = usuario_service.actualizar_usuario(id, datos)
        if resultado['success']:
            flash('Usuario actualizado exitosamente.', 'success')
            return redirect(url_for('usuarios.index'))
        else:
            for error in resultado.get('errores', []):
                flash(error, 'error')
    
    return render_template('laboTres/usuarios/editar.html', usuario=usuario)

@usuario_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar(id):
    """Elimina un usuario"""
    resultado = usuario_service.eliminar_usuario(id)
    if resultado['success']:
        flash('Usuario eliminado exitosamente.', 'success')
    else:
        flash(resultado.get('error', 'Ocurrió un error'), 'error')
        
    return redirect(url_for('usuarios.index'))