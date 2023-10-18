def generate_report(report_type, data):
    if report_type == "HTML":
        reporte = HTMLReporter()
        decorator = HTMLNegativeDecorator(reporte)
    elif report_type == "Console":
        reporte = ConsoleReporter()
        decorator = ConsoleNegativeDecorator(reporte)
    else:
        raise ValueError("Tipo de informe no admitido")

    decorator.format(data)
    reporte.generate_report(data)

if __name__ == "__main__":
    data = {
        "Sección 1": {
            "Valor 1": 42,
            "Valor 2": -32,
        },
        "Sección 2": {
            "Valor 3": 15,
        }
    }

    print("Informe en formato HTML:")
    generate_report("HTML", data)

    print("\nInforme en formato de consola:")
    generate_report("Console", data)