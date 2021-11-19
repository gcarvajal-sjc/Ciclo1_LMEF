def precioFinalVenta(producto1, producto2, producto3, producto4):

    # Logica
    IVA = 0.19

    acumuladorImpuestos = 0

    acumuladorImpuestos += producto1*IVA
    acumuladorImpuestos += producto2*IVA
    acumuladorImpuestos += producto3*IVA
    acumuladorImpuestos += producto4*IVA

    valorTotalProductos = sum((producto1, producto2, producto3, producto4))

    valorTotal = valorTotalProductos + acumuladorImpuestos
    return valorTotal


def precioFinalVenta2(producto1, producto2, producto3, producto4):
    return sum((producto1, producto2, producto3, producto4))*1.19
