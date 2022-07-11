class SimpleReport:
    def generate(self, list):
        filtered_list_valid = [
            int(filtered_date["data_de_validade"])
            for filtered_date in list
            if filtered_date["data_de_validade"].isnumeric()
        ]
        bigger = filtered_list_valid[0]
        smaller = filtered_list_valid[0]
        for number in filtered_list_valid:
            if number > bigger:
                bigger = number
            elif number < smaller:
                smaller = number

            print(filtered_list)
