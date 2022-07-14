from inventory_report.inventory.product import Product


def test_relatorio_produto():
    liquidificador = Product(
        1,
        "liquidificador",
        "ricardoEletrico",
        "01/02/2003",
        "10/11/2005",
        2,
        "na tomada",
    )
    releatorioLiquidificador = liquidificador.__repr__()
    esperado = (
        "O produto liquidificador fabricado em 01/02/2003 por "
        "ricardoEletrico com validade até 10/11/2005 "
        "precisa ser armazenado na tomada.")
    assert str(releatorioLiquidificador) == esperado
