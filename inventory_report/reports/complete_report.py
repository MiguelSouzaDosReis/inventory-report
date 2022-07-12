from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list):
        filtered_list_name = [
            filtered_productCompany["nome_da_empresa"]
            for filtered_productCompany in list
        ]

        report = "Produtos estocados por empresa:\n"
        counterOfFiltered = Counter(filtered_list_name).most_common()
        for company, quantity in counterOfFiltered:
            report += f"- {company}: {quantity}\n"
        return (
            f"{SimpleReport.generate(list)}\n"
            f"{report}"
        )
