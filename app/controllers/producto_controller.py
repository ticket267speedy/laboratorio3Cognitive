from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.producto_service import ProductoService

producto_bp = Blueprint('productos', __name__)
# Blueprint es una libreria que nos permite manejar rutas
producto_service = ProductoService()

@producto_bp.route('/')
def index():
    """Listar todos los productos"""
    productos = producto_service.listar_productos()
    return render_template('index.html', productos=productos)

@producto_bp.route('/producto/<int:id>')
def ver(id):
    """Ver detalles de un producto"""
    producto = producto_service.obtener_producto(id)
    if not producto:
        flash('Producto no encontrado', 'error')
        return redirect(url_for('productos.index'))
    return render_template('ver.html', producto=producto)

@producto_bp.route('/producto/crear', methods=['GET', 'POST'])
def crear():
    """Crear un nuevo producto"""
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'descripcion': request.form.get('descripcion'),
            'precio': request.form.get('precio'),
            'cantidad': request.form.get('cantidad')
        }
        
        resultado = producto_service.crear_producto(datos)
        
        if resultado['success']:
            flash('Producto creado exitosamente', 'success')
            return redirect(url_for('productos.index'))
        else:
            for error in resultado['errores']:
                flash(error, 'error')
    
    return render_template('crear.html')

@producto_bp.route('/producto/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Editar un producto existente"""
    producto = producto_service.obtener_producto(id)
    
    if not producto:
        flash('Producto no encontrado', 'error')
        return redirect(url_for('productos.index'))
    
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'descripcion': request.form.get('descripcion'),
            'precio': request.form.get('precio'),
            'cantidad': request.form.get('cantidad')
        }
        
        resultado = producto_service.actualizar_producto(id, datos)
        
        if resultado['success']:
            flash('Producto actualizado exitosamente', 'success')
            return redirect(url_for('productos.index'))
        else:
            for error in resultado['errores']:
                flash(error, 'error')
    
    return render_template('editar.html', producto=producto)

@producto_bp.route('/producto/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    """Eliminar un producto"""
    resultado = producto_service.eliminar_producto(id)
    
    if resultado['success']:
        flash('Producto eliminado exitosamente', 'success')
    else:
        flash(resultado['error'], 'error')
    
    return redirect(url_for('productos.index'))