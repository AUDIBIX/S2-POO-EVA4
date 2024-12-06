import re, bcrypt


def print_options(opciones=list):
    for idx,opcion in enumerate(opciones,start=1):
        print(f"{idx}. {opcion}")

def valid_input(string_input, string_error, var_type, condition):
    while True:
        try:
            value = var_type(input(string_input))
            if condition(value):
                return value
        except ValueError:
            pass
        except Exception as e:
            print(f"Error inesperado: {e}")
        print(string_error)

def valid_date(fecha):
    from datetime import datetime

    try:
        datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    
def hashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def checkPassword(plainPassword, hashedPassword):
    return bcrypt.checkpw(plainPassword.encode('utf-8'), hashedPassword.encode('utf-8'))

#mensajes de getvaiola
def validateEmail(email):

    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex, email):
        raise ValueError("Correo electrónico no válido: Parece que el correo electrónico que ingresaste no es correcto. Por favor, revisa y asegúrate de que esté bien escrito")
    return email

def validatePassword(password):
    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(regex, password):
        raise ValueError(
            "Formato de Contraseña No Valido: debe tener al menos 8 caracteres, una mayuscula, una miniscula, un número y un caracter especial"
        )
    return password

def validateName(name):
    regex = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"
    if not re.match(regex, name):
        raise ValueError("Nombre no valido: El nombre que ingresaste contiene caracteres no permitidos. Por favor, usa solo letras y espacios. Revisa tu entrada y prueba de nuevo")
    return name

def validateRut(rut):
    regex = r"^\d{1,2}\d{3}\d{3}-[\dkK]$"
    if not re.match(regex, rut):
        raise ValueError("Formato Incorrecto: El formato de tu RUT no es correcto. Asegúrate de seguir el formato: XXXXXXXX-X")
    return rut

def validateUsername(username):
    regex = r"^[a-zA-Z0-9_]{4,16}$"
    if not re.match(regex, username):
        raise ValueError("El nombre de usuario debe tener entre 4 y 16 caracteres, letras, numeros y guiones bajos.")
    return username