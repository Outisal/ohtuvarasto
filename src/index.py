from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:\n"
          f"Mehuvarasto: {mehua}\n"
          f"Olutvarasto: {olutta}\n"
          "\nOlut getterit:\n"
          f"saldo = {olutta.saldo}\n"
          f"tilavuus = {olutta.tilavuus}\n"
          f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n"
          "\nMehu setterit:\n"
          "Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\n"
          "Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}\n"
          "\nVirhetilanteita:")

    error_cases = [
        ("Varasto(-100.0)", Varasto(-100.0)),
        ("Varasto(100.0, -50.7)", Varasto(100.0, -50.7))
    ]
    for desc, varasto in error_cases:
        print(f"{desc}\n{varasto}")

    actions = [
        ("Olutvarasto", ", lisätään 1000.0", olutta.lisaa_varastoon, 1000.0),
        ("Mehuvarasto", ", lisätään -666.0", mehua.lisaa_varastoon, -666.0),
        ("Olutvarasto", ", otetaan 1000.0", olutta.ota_varastosta, 1000.0),
        ("Mehuvarasto", ", otetaan -32.9", mehua.ota_varastosta, -32.9)
    ]

    for name, desc, method, amount in actions:
        print(f"\n{name}{desc}")
        if method(amount) is not None:  # Only print result if it's not None
            print(f"saatiin {method(amount)}")
        print(f"{name}: {olutta if 'Olut' in desc else mehua}")

if __name__ == "__main__":
    main()
