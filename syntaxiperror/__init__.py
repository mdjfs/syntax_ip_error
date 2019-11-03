from .validates import SyntaxIP,validate_address
from .error import SyntaxIPError

def address(val):
    try:
        if validate_address(val) and SyntaxIP(val):
            print("La sintaxis de la IP es correcta.")
        else:
            raise SyntaxIPError()
    except SyntaxIPError as error:
        print(error)