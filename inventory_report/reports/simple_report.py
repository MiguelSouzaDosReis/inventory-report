from datetime import date


def validity(list):
    filtered_list_valid = [
        date.fromisoformat(filtered_date["data_de_validade"])
        for filtered_date in list
    ]
    nearest_expiration_date = filtered_list_valid[0]
    for number in filtered_list_valid:
        if number < nearest_expiration_date:
            nearest_expiration_date = number
    return nearest_expiration_date


def manufacturing(list):
    filtered_list_fabric = [
        date.fromisoformat(filtered_date["data_de_fabricacao"])
        for filtered_date in list
    ]
    oldest_manufacture = filtered_list_fabric[0]
    for number in filtered_list_fabric:
        if number < oldest_manufacture:
            oldest_manufacture = number
            return oldest_manufacture


def companyName(list):
    filtered_list_name = [
        filtered_name["nome_da_empresa"]
        for filtered_name in list
        if filtered_name["data_de_validade"] != ""
    ]
    counter = 0
    name = filtered_list_name[0]

    for index in filtered_list_name:
        actual = filtered_list_name.count(index)
        if actual > counter:
            counter = actual
            name = index
            return name


class SimpleReport:
    def generate(list):
        validade = validity(list)
        fabricação = manufacturing(list)
        filtered_list_name = [
            filtered_name["nome_da_empresa"]
            for filtered_name in list
            if filtered_name["data_de_validade"] != ""
        ]

        counter = 0
        name = filtered_list_name[0]

        for index in filtered_list_name:
            actual = filtered_list_name.count(index)
            if actual > counter:
                counter = actual
                name = index

        return (
            f"Data de fabricação mais antiga: {fabricação}\n"
            f"Data de validade mais próxima: {validade}\n"
            f"Empresa com mais produtos: {name}"
        )
