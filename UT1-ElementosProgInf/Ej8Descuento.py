precio_original = float(input("Ingrese el precio original: "))
descuento_porcentaje = float(input("Ingrese el descuento: "))

descuento = precio_original * (descuento_porcentaje / 100)
precio_final = precio_original - descuento

print(f"Precio final: {precio_final}")
print(f"Descuento aplicado: {descuento}")