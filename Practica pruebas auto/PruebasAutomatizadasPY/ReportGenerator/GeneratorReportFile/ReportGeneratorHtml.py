from jinja2 import Template
from datetime import datetime



class GeneratorReportHTML:
    def __init__(self, path_report, results, FailedNO, PassedNO):
        self.path_reporte = path_report
        self.resultss = results
        self.passed = PassedNO
        self.failed = FailedNO

    def generate_report(self):
        with open("./PruebasAutomatizadasPY/ReportGenerator/GeneratorReportFile/ReportTemplate.html") as file:
            template = Template(file.read())
       
        rendered_html = template.render(resultados=self.resultss, datetime = datetime.now(), FailedNO = self.failed, PassedNO = self.passed )

        with open(self.path_reporte, "w") as file:
            file.write(rendered_html)
            

            