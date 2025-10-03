from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario import Usuario


class UsuarioService:
    
    def __init__(self):
        self.repository = UsuarioRepository()
    
    def listar_usuarios(self):
        """Devuelve una lista de todos los usuarios."""
        return self.repository.obtener_todos()
    
    def obtener_usuario(self, usuario_id):
        """Obtiene un usuario por su ID."""
        return self.repository.obtener_por_id(usuario_id)

    def verificar_credenciales(self, email, password):
        """Verifica las credenciales de un usuario para el login."""
        usuario = self.repository.obtener_por_email(email)
        if not usuario:
            return None # Usuario no encontrado
        
        # Comprobación de contraseña en texto plano (como en tu BBDD inicial)
        if usuario.password == password:
            return usuario
        
        # NOTA: En un sistema real, la comprobación sería así:
        # if check_password_hash(usuario.password, password):
        #     return usuario
            
        return None # Contraseña incorrecta

    def crear_usuario(self, datos):
        """Crea un nuevo usuario con validaciones."""
        errores = []
        
        # Validaciones de campos obligatorios
        if not datos.get('nombre') or not datos.get('nombre').strip():
            errores.append('El nombre es obligatorio.')
        if not datos.get('email') or not datos.get('email').strip():
            errores.append('El email es obligatorio.')
        if not datos.get('password') or not datos.get('password').strip():
            errores.append('La contraseña es obligatoria.')
        if not datos.get('rol') or datos.get('rol') not in ['admin', 'usuario']:
            errores.append('El rol no es válido.')

        # Validación de email único
        if not errores and self.repository.obtener_por_email(datos.get('email')):
            errores.append('El email ya está registrado.')

        if errores:
            return {'success': False, 'errores': errores}
        
        # Lógica para encriptar la contraseña (ejemplo para el futuro)
        # hashed_password = generate_password_hash(datos.get('password'))

        nuevo_usuario = Usuario(
            nombre=datos.get('nombre').strip(),
            email=datos.get('email').strip(),
            password=datos.get('password'), # Usamos la contraseña en texto plano por ahora
            # password=hashed_password, # Así sería en un caso real
            rol=datos.get('rol')
        )
        
        usuario_id = self.repository.crear(nuevo_usuario)
        return {'success': True, 'id': usuario_id}

    def actualizar_usuario(self, usuario_id, datos):
        """Actualiza un usuario existente."""
        usuario_existente = self.repository.obtener_por_id(usuario_id)
        if not usuario_existente:
            return {'success': False, 'errores': ['Usuario no encontrado.']}

        errores = []
        if not datos.get('nombre') or not datos.get('nombre').strip():
            errores.append('El nombre es obligatorio.')
        if not datos.get('email') or not datos.get('email').strip():
            errores.append('El email es obligatorio.')
        if not datos.get('rol') or datos.get('rol') not in ['admin', 'usuario']:
            errores.append('El rol no es válido.')

        # Validar que el nuevo email no pertenezca a otro usuario
        otro_usuario = self.repository.obtener_por_email(datos.get('email'))
        if otro_usuario and otro_usuario.id != usuario_id:
            errores.append('El email ya está en uso por otro usuario.')

        if errores:
            return {'success': False, 'errores': errores}

        usuario_actualizado = Usuario(
            id=usuario_id,
            nombre=datos.get('nombre').strip(),
            email=datos.get('email').strip(),
            rol=datos.get('rol')
        )
        
        self.repository.actualizar(usuario_actualizado)
        return {'success': True}

    def eliminar_usuario(self, usuario_id):
        """Elimina un usuario."""
        usuario_existente = self.repository.obtener_por_id(usuario_id)
        if not usuario_existente:
            return {'success': False, 'error': 'Usuario no encontrado.'}
        
        self.repository.eliminar(usuario_id)
        return {'success': True}