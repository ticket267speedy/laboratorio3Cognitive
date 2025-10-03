class Curso:
    def __init__(self, id=None, nombre=None, creditos=None):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'creditos': self.creditos
        }
    
    @staticmethod
    def from_dict(data):
        return Curso(
            id=data.get('id'),
            nombre=data.get('nombre'),
            creditos=data.get('creditos')
        )