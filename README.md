# laboratorio3Cognitive
Creación con flask y mariaDB
## Flash CRUD MVC

# Estructura de carpetas
# Nota: estoy usando la plantilla de clase y lo que hice en clase que es "curso" para guiarme, pero lo estoy separando dentro de la inicialización.
```
flask_crud_mvc/
│
├── venv/                      # Virtual
│
├── app/
│   ├── __init__.py           # Inicialización de la app Flask
│   ├── config.py             # Configuración de la base de datos
│   │
│   ├── controllers/
│   │   ├── producto_controller.py
│   │   ├── curso_controller.py
│   │   └── usuario_controller.py    # Modelo Usuario para el lab3
│   │
│   ├── models/
│   │   ├── producto.py
│   │   ├── curso.py
│   │   └── usuario.py
│   │
│   ├── repositories/
│   │   ├── producto_repository.py
│   │   ├── curso_repository.py
│   │   └── usuario_repository.py
│   │
│   ├── services/
│   │   ├── producto_service.py
│   │   ├── curso_service.py
│   │   └── usuario_service.py
│   │
│   ├── templates/
│   │   ├── laboTres/
│   │   │   ├── usuarios/
│   │   │   │   ├── base.html
│   │   │   │   ├── index.html
│   │   │   │   ├── crear.html
│   │   │   │   └── editar.html
│   │   │   └── login.html
│   │   │
│   │   ├── ... (plantillas de producto y curso que usé durante las clases)
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── requirements.txt          # Dependencias del proyecto (flask y MySQL)
└── run.py                    # Punto de entrada para ejecutar la aplicación
```

# 1. Requisitos Previos

Python 3.8 o superior instalado
MySQL Server instalado y ejecutándose
pip (gestor de paquetes de Python)

# 2 Crear el proyecto

# Crear directorio del proyecto
mkdir flask_crud_mvc
cd flask_crud_mvc

# Crear la estructura de carpetas
mkdir -p app/{models,repositories,services,controllers,templates,static/css}

# Pasos para instalar y ejecutar la aplicación
# Abrimos powerShell como administrador
# 1.clonamos en la carpeta que tengamos, supongamos ICC/sem07
git clone https://github.com/ticket267speedy/laboratorio3Cognitive.git

# 2. Creamos el entorno virtual
python -m venv env

# 3. activamos el entorno virtual
.\env\Scripts\Activate.ps1

# 4. Instalamos las dependencias que estan en requirements.txt
pip install -r requirements.txt

# 5. Ejecutamos la aplicación
py run.py
