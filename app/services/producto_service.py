from app.repositories.producto_repository import ProductoRepository
from app.models.producto import Producto

class ProductoService:
    
    def __init__(self):
        self.repository = ProductoRepository()
    
    def listar_productos(self):
        """Listar todos los productos"""
        return self.repository.obtener_todos()
    
    def obtener_producto(self, producto_id):
        """Obtener un producto específico"""
        return self.repository.obtener_por_id(producto_id)
    
    def crear_producto(self, datos):
        """Crear un nuevo producto con validaciones"""
        # Validaciones
        errores = []
        
        if not datos.get('nombre') or len(datos.get('nombre', '').strip()) == 0:
            errores.append('El nombre es obligatorio')
        
        try:
            precio = float(datos.get('precio', 0))
            if precio < 0:
                errores.append('El precio debe ser mayor o igual a 0')
        except ValueError:
            errores.append('El precio debe ser un número válido')
            precio = 0
        
        try:
            cantidad = int(datos.get('cantidad', 0))
            if cantidad < 0:
                errores.append('La cantidad debe ser mayor o igual a 0')
        except ValueError:
            errores.append('La cantidad debe ser un número entero válido')
            cantidad = 0
        
        if errores:
            return {'success': False, 'errores': errores}
        
        # Crear producto
        producto = Producto(
            nombre=datos.get('nombre').strip(),
            descripcion=datos.get('descripcion', '').strip(),
            precio=precio,
            cantidad=cantidad
        )
        
        producto_id = self.repository.crear(producto)
        return {'success': True, 'id': producto_id}
    
    def actualizar_producto(self, producto_id, datos):
        """Actualizar un producto existente con validaciones"""
        # Validar que el producto existe
        producto_existente = self.repository.obtener_por_id(producto_id)
        if not producto_existente:
            return {'success': False, 'errores': ['Producto no encontrado']}
        
        # Validaciones
        errores = []
        
        if not datos.get('nombre') or len(datos.get('nombre', '').strip()) == 0:
            errores.append('El nombre es obligatorio')
        
        try:
            precio = float(datos.get('precio', 0))
            if precio < 0:
                errores.append('El precio debe ser mayor o igual a 0')
        except ValueError:
            errores.append('El precio debe ser un número válido')
            precio = 0
        
        try:
            cantidad = int(datos.get('cantidad', 0))
            if cantidad < 0:
                errores.append('La cantidad debe ser mayor o igual a 0')
        except ValueError:
            errores.append('La cantidad debe ser un número entero válido')
            cantidad = 0
        
        if errores:
            return {'success': False, 'errores': errores}
        
        # Actualizar producto
        producto = Producto(
            id=producto_id,
            nombre=datos.get('nombre').strip(),
            descripcion=datos.get('descripcion', '').strip(),
            precio=precio,
            cantidad=cantidad
        )
        
        self.repository.actualizar(producto)
        return {'success': True}
    
    def eliminar_producto(self, producto_id):
        """Eliminar un producto"""
        producto_existente = self.repository.obtener_por_id(producto_id)
        if not producto_existente:
            return {'success': False, 'error': 'Producto no encontrado'}
        
        self.repository.eliminar(producto_id)
        return {'success': True}