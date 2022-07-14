from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json

import xmltodict


class Inventory:
    @staticmethod
    def dataCsv(stringOfPathData, typeOfReport):
        with open(stringOfPathData) as file:
            data = list(csv.DictReader(file, delimiter=",", quotechar='"'))
            if typeOfReport == "simples":
                return SimpleReport.generate(data)
            elif typeOfReport == "completo":
                return CompleteReport.generate(data)

    @staticmethod
    def dataJson(stringOfPathData, typeOfReport):
        with open(stringOfPathData) as file:
            content = file.read()
            data = json.loads(content)
            if typeOfReport == "simples":
                return SimpleReport.generate(data)
            elif typeOfReport == "completo":
                return CompleteReport.generate(data)

    @staticmethod
    def dataXml(stringOfPathData, typeOfReport):
        with open(stringOfPathData) as file:
            doc = xmltodict.parse(file.read())
            data = doc["dataset"]["record"]
            if typeOfReport == "simples":
                return SimpleReport.generate(data)
            elif typeOfReport == "completo":
                return CompleteReport.generate(data)

    def import_data(stringOfPath, typeOfReport):
        if stringOfPath.endswith(".csv"):
            return Inventory.dataCsv(stringOfPath, typeOfReport)
        if stringOfPath.endswith(".json"):
            return Inventory.dataJson(stringOfPath, typeOfReport)
        if stringOfPath.endswith(".xml"):
            return Inventory.dataXml(stringOfPath, typeOfReport)
