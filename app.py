class Usuario:
    def init(self, nombre, apellido, edad):
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
            print("El usuario de nombre", self.nombre, "y de apellido", self.apellido, "h creado")
        else:
            print("no se pudo crear el usuario por viejo HP.")


class cantina:
    def init(self):
        self.enlistado = []

    def enlistar(self, bebida, precio):
        bebida_obj = {"nombre": bebida, "precio": precio}
        self.enlistado.append(bebida_obj)

    def mostrar_enlistado(self):
        print("Enlistado de bebidas:")
        for bebida_obj in self.enlistado:
            print(f"Bebida: {bebida_obj['nombre']}, Precio: {bebida_obj['precio']}")

def main():
    usuarios = [
        Usuario("samuel", "parody", 45),
        Usuario("Aaron", "elver", 54),
        Usuario("pedro", "galarga", 76),
        Usuario("Pepe", "fernandez", 54),
        Usuario("luffy", "D.monky", 17),
       Usuario("Zoro", "Roronoa",  21),
    ]

    for i, usuario in enumerate(usuarios, 1):
        print(f"-----------")
        print(f"Usuario #{i}")
        usuario.crear_usuario()
        usuario.mostrar_usuario_creado()

        cantina = cantina()
        cantina.enlistar("pilsen", 9000)
        cantina.enlistar("roncaldas", 6000)
        cantina.mostrar_enlistado()

if name == "main":
    main()
