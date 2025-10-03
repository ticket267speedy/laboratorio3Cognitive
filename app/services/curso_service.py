from app.repositories.curso_repository import CursoRepository
from app.models.curso import Curso

class CursoService:
    
    def __init__(self):
        self.repository = CursoRepository()
    
    def listar_cursos(self):
        """Listar todos los cursos"""
        return self.repository.obtener_todos()
    
    def obtener_curso(self, curso_id):
        """Obtener un curso específico"""
        return self.repository.obtener_por_id(curso_id)
    
    def crear_curso(self, datos):
        """Crear un nuevo curso con validaciones"""
        # Validaciones
        errores = []
        
        if not datos.get('nombre') or len(datos.get('nombre', '').strip()) == 0:
            errores.append('El nombre es obligatorio')
        
        try:
            creditos = float(datos.get('creditos', 0))
            if creditos < 0:
                errores.append('Los créditos deben ser mayor o igual a 0')
        except ValueError:
            errores.append('Los créditos deben ser un número válido')
            creditos = 0
        
        
        if errores:
            return {'success': False, 'errores': errores}
        
        # Crear curso
        curso = Curso(
            nombre=datos.get('nombre').strip(),
            creditos=creditos # antes usaba get('creditos', '').strip() y estaba mal
        )   # daba error lo de arriba, recordar eso
        
        curso_id = self.repository.crear(curso)
        return {'success': True, 'id': curso_id}
    
    def actualizar_curso(self, curso_id, datos):
        """Actualizar un producto existente con validaciones"""
        # Validar que el producto existe
        curso_existente = self.repository.obtener_por_id(curso_id)
        if not curso_existente:
            return {'success': False, 'errores': ['Curso no encontrado']}
        
        # Validaciones
        errores = []
        
        if not datos.get('nombre') or len(datos.get('nombre', '').strip()) == 0:
            errores.append('El nombre es obligatorio')
        
        try:
            creditos = float(datos.get('creditos', 0))
            if creditos < 0:
                errores.append('Los créditos deben ser mayor o igual a 0')
        except ValueError:
            errores.append('Los créditos deben ser un número válido')
            creditos = 0
        
        
        if errores:
            return {'success': False, 'errores': errores}
        
        # Actualizar producto
        curso = Curso(
            id=curso_id,
            nombre=datos.get('nombre').strip(),
            creditos=creditos # antes usaba get('creditos', '').strip() y estaba mal
        )   # daba error lo de arriba, recordar eso
        
        self.repository.actualizar(curso)
        return {'success': True}
    
    def eliminar_curso(self, curso_id):
        """Eliminar un curso"""
        curso_existente = self.repository.obtener_por_id(curso_id)
        if not curso_existente:
            return {'success': False, 'error': 'Curso no encontrado'}
        
        self.repository.eliminar(curso_id)
        return {'success': True}