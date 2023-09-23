class Bebida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class cantina:
    def __init__(self):
        self.enlistado = []

    def enlistar(self, bebida, precio):
        bebida_obj = Bebida(bebida, precio)
        self.enlistado.append(bebida_obj)

    def mostrar_enlistado(self):
        print("Enlistado de bebidas:")
        for bebida_obj in self.enlistado:
            print(f"Bebida: {bebida_obj.nombre}, Precio: {bebida_obj.precio}")

if __name__ == "__main__":
    cantina = cantina()


    cantina.enlistar("Cerveza", 5.0)
    cantina.enlistar("Vino tinto", 7.0)
    cantina.enlistar("Refresco", 2.0)

  
    cantina.mostrar_enlistado()
