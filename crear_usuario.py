class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def crear_usuario(self):
        if self.es_mayor_de_edad():
            print("El usuario se puede crear:")
            print("Nombre:", self.nombre)
            print("Apellido:", self.apellido)
            print("Edad:", self.edad)
        else:
            print("El usuario", self.nombre, "no puede tener un registro ya que no cumple los 18 ve y toma yogurt")

    def mostrar_usuario_creado(self):
        if self.es_mayor_de_edad():
            print("El usuario de nombre", self.nombre, "y de apellido", self.apellido, "ha sido creado")
        else:
            print(".")


def main():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))

    usuario = Usuario(nombre, apellido, edad)
    usuario.crear_usuario()
    usuario.mostrar_usuario_creado()


if __name__ == "__main__":
    main()
