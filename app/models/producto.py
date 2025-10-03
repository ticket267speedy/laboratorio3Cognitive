class Producto:
    def __init__(self, id=None, nombre=None, descripcion=None, precio=None, cantidad=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': float(self.precio) if self.precio else 0,
            'cantidad': self.cantidad
        }
    
    @staticmethod
    def from_dict(data):
        return Producto(
            id=data.get('id'),
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            cantidad=data.get('cantidad')
        )