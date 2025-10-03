from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.curso_service import CursoService

curso_bp = Blueprint('cursos', __name__)
curso_service = CursoService()

# Rutas para cursos
@curso_bp.route('/')
def index():
    """Listar todos los cursos"""
    cursos = curso_service.listar_cursos()
    return render_template('indexcurso.html', cursos=cursos)

@curso_bp.route('/curso/<int:id>')
def ver(id):
    """Ver detalles de un curso"""
    curso = curso_service.obtener_curso(id)
    if not curso:
        flash('Curso no encontrado', 'error')
        return redirect(url_for('cursos.index'))
    return render_template('vercurso.html', curso=curso)

@curso_bp.route('/curso/crear', methods=['GET', 'POST'])
def crear():
    """Crear un nuevo curso"""
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'creditos': request.form.get('creditos')
        }
        
        resultado = curso_service.crear_curso(datos)
        
        if resultado['success']:
            flash('Curso creado exitosamente', 'success')
            return redirect(url_for('cursos.index'))
        else:
            for error in resultado['errores']:
                flash(error, 'error')
    
    return render_template('crearcurso.html')

@curso_bp.route('/curso/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Editar un curso existente"""
    curso = curso_service.obtener_curso(id)
    
    if not curso:
        flash('Curso no encontrado', 'error')
        return redirect(url_for('cursos.index'))
    
    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'creditos': request.form.get('creditos')
        }
        
        resultado = curso_service.actualizar_curso(id, datos)
        
        if resultado['success']:
            flash('Curso actualizado exitosamente', 'success')
            return redirect(url_for('cursos.index'))
        else:
            for error in resultado['errores']:
                flash(error, 'error')
    
    return render_template('editarcurso.html', curso=curso)

@curso_bp.route('/curso/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    """Eliminar un curso"""
    resultado = curso_service.eliminar_curso(id)
    
    if resultado['success']:
        flash('Curso eliminado exitosamente', 'success')
    else:
        flash(resultado['error'], 'error')
    
    return redirect(url_for('cursos.index'))
