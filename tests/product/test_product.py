from inventory_report.inventory.product import Product


def test_cria_produto():
    liquidificador = Product(
        1,
        "liquidificador",
        "ricardoEletrico",
        "01/02/2003",
        "10/11/2005",
        "2",
        "na tomada",
    )
    assert liquidificador.id == 1
    assert liquidificador.nome_do_produto == "liquidificador"
    assert liquidificador.nome_da_empresa == "ricardoEletrico"
    assert liquidificador.data_de_fabricacao == "01/02/2003"
    assert liquidificador.data_de_validade == "10/11/2005"
    assert liquidificador.numero_de_serie == "2"
    assert liquidificador.instrucoes_de_armazenamento == "na tomada"
