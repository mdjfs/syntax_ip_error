import math

class SyntaxIPError(Exception):
    def __init__(self):
        self.message= 'La sintaxis de la IP es incorrecta.'
    
    def __str__(self):
        return self.message



def address(val):
    try:
        if validate_address(val) and SyntaxIP(val):
            print("La sintaxis de la IP es correcta.")
        else:
            raise SyntaxIPError()
    except SyntaxIPError as error:
        print(error)

direccion = "255.255.0.255"

print(address(direccion))