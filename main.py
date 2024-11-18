class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio= precio
        self.registro = registro

    def cambiarColor(self, color):
        list= ["rojo", "verde", "amarillo", "negro", "blanco"]
        hay = True
        for i in list:
            if i == color:
                self.color=i
                return self.color
            else:
                hay = False

        if hay == False:
            pass

class Auto:

    cantidad_creados= ""

    def __init__(self, modelo, precio, asientos, marca, Motor, registro):

        self.modelo = modelo
        self.precio = precio
       
       
        self.asientos: list[Asiento] = asientos
        
        self.motor = Motor
        self.registro = registro

    def cantidadAsientos(self):

        filtered_list = list(filter(lambda x: x is not None, self.asientos))
        j =len(filtered_list)
        return j

    def Integridad(self):
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if asiento.registro != self.motor.registro:
                    return "Las piezas no son originales"
                elif asiento.registro != self.registro:
                    return "Las piezas no son originales"
                elif self.registro != self.motor.registro:
                     return "Las piezas no son originales"
        return "Auto original"

class Motor:
    tiposPosibles: list[str] = ["electrico", "gasolina"]

    def __init__(self, numeroCilindros: int, tipo: str, registro: int) -> None:
        self.numeroCilindros: int = numeroCilindros
        self.tipo: str = tipo
        self.registro: int = registro

    def cambiarRegistro(self, registro: int) -> None:
        self.registro: int = registro

    def asignarTipo(self, tipo: str) -> None:
        if tipo in Motor.tiposPosibles:
            self.tipo: str = tipo

a = Auto("model 3", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)
    
a.asientos = [Asiento("blanco", 5000, 435),None, None, Asiento("blanco", 5000, 435), None]

print(a.cantidadAsientos())