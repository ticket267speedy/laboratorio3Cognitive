class Usuario:
    def __init__(self, id=None, nombre=None, email=None, password=None, rol=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
        }
    
    @staticmethod
    def from_dict(data):
        return Usuario(
            id=data.get('id'),
            nombre=data.get('nombre'),
            email=data.get('email'),
            password=data.get('password'),
            rol=data.get('rol')
        )