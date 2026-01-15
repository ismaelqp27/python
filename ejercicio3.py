precios_frutas_dic = {
    'Plátano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}

fruta = input("¿Qué fruta busca? ").title()
kilos = float(input("¿Cuántos kilos desea? "))

if fruta in precios_frutas_dic:
    precio_total = precios_frutas_dic[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es {precio_total:.2f}€")
else:
    print(f"Lo sentimos, la fruta '{fruta}' no está disponible.")