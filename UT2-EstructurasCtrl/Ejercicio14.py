

class ErrorImporteInvalido(Exception):
    def __int__(self, importe, mensaje :str="El importe debe ser positivo"):
        self.importe = importe
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def validar_pago(importe_a_validar :{_le_} ):
        if importe_a_validar <= 0:
            raise ErrorImporteInvalido(importe_a_validar)
        print("Procesando pago de: ", importe_a_validar)

try:
    validar_pago(-100)
except (TypeError, ValueError) as e:
    print("Error al pagar")
print("Buenos dias")