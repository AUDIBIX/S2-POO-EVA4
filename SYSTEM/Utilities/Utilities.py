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