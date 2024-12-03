from SYSTEM.DTO.Package import *
from SYSTEM.DTO.Destination import *

if __name__ == "__main__":
    package = Package("Paquete 1", "Descripcion del paquete 1", 1000)
    package.generateDestination()
    print(package)