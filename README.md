# S2-POO-EVA4
Semestre 2 Programación Orientada a Objetos, Evaluación Sumativa 4 Semana 8

# Sistema de Gestión de Viajes ✈️
Este proyecto es un sistema de viajes que permite a los usuarios explorar paquetes de viajes prearmados y crear sus propios paquetes personalizados según sus preferencias. El sistema está desarrollado en Python y sigue una arquitectura de Programación Orientada a Objetos (POO) con una API para la interacción con los datos.

## Funcionalidades 🚀
Funcionalidades principales:
Explorar paquetes de viajes predefinidos:
Los usuarios pueden ver y seleccionar entre diferentes paquetes de viajes ya creados que incluyen destinos, alojamiento, actividades y transporte.

### Crear paquetes personalizados:
Los usuarios pueden crear un paquete de viaje personalizado eligiendo sus propios destinos, alojamiento, transporte y actividades adicionales.

### Gestión de usuarios y paquetes:
Registro y autenticación de usuarios.
Visualización y modificación de los paquetes creados.
Eliminación de paquetes de viaje.

### API REST:
Una API que expone los servicios principales del sistema, permitiendo la interacción desde aplicaciones externas o clientes web.

## Requisitos 📋
Para ejecutar este proyecto, se necesita:

Python 3.8 o superior
Bibliotecas listadas en requirements.txt

Instale las dependencias ejecutando:
```pip install -r API/requirements.txt```


## Estructura del proyecto 🗂️
```
S2-POO-EVA4/
├── API/                   # Lógica de API y servicios
│   ├── controllers/       # Controladores para manejar las solicitudes HTTP
│   ├── models/            # Definición de los modelos de datos
│   ├── repositories/      # Acceso y manipulación de la base de datos
│   ├── services/          # Lógica de negocio
│   ├── main.py            # Punto de entrada de la API
│   └── requirements.txt   # Dependencias del proyecto
├── SYSTEM/                # Lógica interna del sistema
│   ├── DAO/               # Data Access Object para interactuar con los datos
│   ├── DTO/               # Data Transfer Objects para estructurar los datos
│   ├── Utilities/         # Utilidades y funciones auxiliares
│   └── main.py            # Punto de entrada del sistema principal
├── LICENSE                # Licencia del proyecto
└── README.md              # Este archivo
```

# Cómo ejecutar el sistema ▶️
Hay dos opciones, instalar las librerías manualmente o utilizar un entorno virtual

## Instalar las librerías manualmente

### Instalar las dependencias
Desde la carpeta principal, ejecute:
```pip install -r API/requirements.txt```

### Ejecutar la API
Navega a la carpeta API y ejecuta el archivo main.py:
```python API/main.py```
Esto iniciará el servidor API en http://localhost:5000 (o el puerto especificado).

### Ejecutar el sistema principal
Navega a la carpeta SYSTEM y ejecuta el archivo main.py:
```python SYSTEM/main.py```

## Utilizar un entorno virtual

### Instalar pipenv
Si no se tiene instalado pipenv, ejecute:
```pip install pipenv```

### Instalar las dependencias
Para instalar las dependencias del programa, ejecute:
```pipenv install```

### Ejecutar una terminal en la carpeta principal
Abra una terminal en la carpeta principal y cree un entorno virtual con:
```pipenv shell```

### Ejecutar la API
Para ejecutar la API, ejecute:
```pipenv run python API/main.py```

### Ejecutar el sistema principal
Finalmente, para ejecutar el sistema principal, ejecute:
```pipenv run python main.py```