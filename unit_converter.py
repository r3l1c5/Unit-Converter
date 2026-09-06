import math


def get_value():
    while True:
        try:
            return float(input("Enter value: "))
        except ValueError:
            print("Invalid value. Please enter a number.")


def show_result(result, unit):
    print(f"\nResult: {result:g} {unit}")


def length_converter():
    units = {
        "1": ("Miles", 0.621371),
        "2": ("Kilometers", 1.609344),
        "3": ("Feet", 3.28084),
        "4": ("Meters", 0.3048),
        "5": ("Inches", 0.393701),
        "6": ("Centimeters", 2.54),
        "7": ("Yards", 1.093613),
        "8": ("Meters", 0.9144),
        "9": ("Inches", 39.3701),
        "10": ("Meters", 0.0254),
        "11": ("Meters", 1000),
        "12": ("Kilometers", 0.001),
        "13": ("Feet", 5280),
        "14": ("Miles", 1 / 5280),
        "15": ("Kilometers", 1.852),
        "16": ("Nautical Miles", 0.539957)
    }

    print("\nLENGTH CONVERTER")
    print("----------------")
    options = [
        "Kilometers → Miles",
        "Miles → Kilometers",
        "Meters → Feet",
        "Feet → Meters",
        "Centimeters → Inches",
        "Inches → Centimeters",
        "Meters → Yards",
        "Yards → Meters",
        "Meters → Inches",
        "Inches → Meters",
        "Kilometers → Meters",
        "Meters → Kilometers",
        "Miles → Feet",
        "Feet → Miles",
        "Nautical Miles → Kilometers",
        "Kilometers → Nautical Miles"
    ]

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in units:
        value = get_value()
        unit, multiplier = units[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def area_converter():
    conversions = {
        "1": ("Square Feet", 10.7639),
        "2": ("Square Meters", 0.092903),
        "3": ("Square Miles", 0.386102),
        "4": ("Square Kilometers", 2.58999),
        "5": ("Acres", 2.47105),
        "6": ("Hectares", 0.404686),
        "7": ("Square Centimeters", 10000),
        "8": ("Square Meters", 0.0001),
        "9": ("Square Inches", 1550.0031),
        "10": ("Square Meters", 0.00064516),
        "11": ("Square Kilometers", 1e-6),
        "12": ("Square Meters", 1e6)
    }

    options = [
        "Square Meters → Square Feet",
        "Square Feet → Square Meters",
        "Square Kilometers → Square Miles",
        "Square Miles → Square Kilometers",
        "Hectares → Acres",
        "Acres → Hectares",
        "Square Meters → Square Centimeters",
        "Square Centimeters → Square Meters",
        "Square Meters → Square Inches",
        "Square Inches → Square Meters",
        "Square Meters → Square Kilometers",
        "Square Kilometers → Square Meters"
    ]

    print("\nAREA CONVERTER")
    print("--------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def volume_converter():
    conversions = {
        "1": ("Gallons", 0.264172),
        "2": ("Liters", 3.78541),
        "3": ("Milliliters", 1000),
        "4": ("Liters", 0.001),
        "5": ("Liters", 1000),
        "6": ("Cubic Meters", 0.001),
        "7": ("Cubic Feet", 35.3147),
        "8": ("Cubic Meters", 0.0283168),
        "9": ("Cubic Inches", 61.0237),
        "10": ("Cubic Centimeters", 16.3871),
        "11": ("Pints", 2.11338),
        "12": ("Liters", 0.473176),
        "13": ("Quarts", 1.05669),
        "14": ("Liters", 0.946353)
    }

    options = [
        "Liters → Gallons",
        "Gallons → Liters",
        "Liters → Milliliters",
        "Milliliters → Liters",
        "Cubic Meters → Liters",
        "Liters → Cubic Meters",
        "Cubic Meters → Cubic Feet",
        "Cubic Feet → Cubic Meters",
        "Liters → Cubic Inches",
        "Cubic Inches → Liters",
        "Liters → Pints",
        "Pints → Liters",
        "Liters → Quarts",
        "Quarts → Liters"
    ]

    print("\nVOLUME CONVERTER")
    print("----------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def mass_converter():
    conversions = {
        "1": ("Pounds", 2.20462),
        "2": ("Kilograms", 0.453592),
        "3": ("Grams", 1000),
        "4": ("Kilograms", 0.001),
        "5": ("Ounces", 0.035274),
        "6": ("Grams", 28.3495),
        "7": ("Kilograms", 1000),
        "8": ("Tonnes", 0.001),
        "9": ("Pounds", 2204.62),
        "10": ("Tonnes", 0.000453592),
        "11": ("Milligrams", 1e6),
        "12": ("Grams", 0.001)
    }

    options = [
        "Kilograms → Pounds",
        "Pounds → Kilograms",
        "Kilograms → Grams",
        "Grams → Kilograms",
        "Grams → Ounces",
        "Ounces → Grams",
        "Tonnes → Kilograms",
        "Kilograms → Tonnes",
        "Tonnes → Pounds",
        "Pounds → Tonnes",
        "Kilograms → Milligrams",
        "Milligrams → Grams"
    ]

    print("\nWEIGHT / MASS CONVERTER")
    print("-----------------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def temperature_converter():
    print("\nTEMPERATURE CONVERTER")
    print("---------------------")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    value = get_value()

    if choice == "1":
        result = value * 9 / 5 + 32
        show_result(result, "°F")
    elif choice == "2":
        result = (value - 32) * 5 / 9
        show_result(result, "°C")
    elif choice == "3":
        result = value + 273.15
        show_result(result, "K")
    elif choice == "4":
        result = value - 273.15
        show_result(result, "°C")
    elif choice == "5":
        result = (value - 32) * 5 / 9 + 273.15
        show_result(result, "K")
    elif choice == "6":
        result = (value - 273.15) * 9 / 5 + 32
        show_result(result, "°F")
    else:
        print("Invalid option.")


def time_converter():
    conversions = {
        "1": ("Minutes", 60),
        "2": ("Hours", 1 / 60),
        "3": ("Seconds", 60),
        "4": ("Minutes", 1 / 60),
        "5": ("Seconds", 3600),
        "6": ("Hours", 1 / 3600),
        "7": ("Hours", 24),
        "8": ("Days", 1 / 24),
        "9": ("Days", 1 / 1440),
        "10": ("Minutes", 1440),
        "11": ("Seconds", 86400),
        "12": ("Days", 1 / 86400)
    }

    options = [
        "Hours → Minutes",
        "Minutes → Hours",
        "Minutes → Seconds",
        "Seconds → Minutes",
        "Hours → Seconds",
        "Seconds → Hours",
        "Days → Hours",
        "Hours → Days",
        "Days → Minutes",
        "Minutes → Days",
        "Days → Seconds",
        "Seconds → Days"
    ]

    print("\nTIME CONVERTER")
    print("--------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def speed_converter():
    conversions = {
        "1": ("mph", 0.621371),
        "2": ("km/h", 1.60934),
        "3": ("km/h", 3.6),
        "4": ("m/s", 1 / 3.6),
        "5": ("km/h", 1.852),
        "6": ("knots", 1 / 1.852),
        "7": ("mph", 2.23694),
        "8": ("m/s", 0.44704)
    }

    options = [
        "Kilometers/hour → Miles/hour",
        "Miles/hour → Kilometers/hour",
        "Meters/second → Kilometers/hour",
        "Kilometers/hour → Meters/second",
        "Knots → Kilometers/hour",
        "Kilometers/hour → Knots",
        "Meters/second → Miles/hour",
        "Miles/hour → Meters/second"
    ]

    print("\nSPEED CONVERTER")
    print("----------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def pressure_converter():
    conversions = {
        "1": ("PSI", 14.5038),
        "2": ("Bar", 0.0689476),
        "3": ("PSI", 14.6959),
        "4": ("Atmospheres", 1 / 14.6959),
        "5": ("Pascals", 100000),
        "6": ("Bar", 0.00001),
        "7": ("Pascals", 101325),
        "8": ("Atmospheres", 1 / 101325),
        "9": ("Kilopascals", 100),
        "10": ("Pascals", 0.01)
    }

    options = [
        "Bar → PSI",
        "PSI → Bar",
        "Atmosphere → PSI",
        "PSI → Atmosphere",
        "Bar → Pascal",
        "Pascal → Bar",
        "Atmosphere → Pascal",
        "Pascal → Atmosphere",
        "Bar → Kilopascal",
        "Kilopascal → Pascal"
    ]

    print("\nPRESSURE CONVERTER")
    print("------------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def energy_converter():
    conversions = {
        "1": ("Kilojoules", 0.001),
        "2": ("Joules", 1000),
        "3": ("Joules", 4184),
        "4": ("Kilocalories", 1 / 4184),
        "5": ("Joules", 3600000),
        "6": ("Kilowatt-hours", 1 / 3600000),
        "7": ("Calories", 1000),
        "8": ("Kilocalories", 0.001),
        "9": ("BTU", 0.000947817),
        "10": ("Joules", 1055.06)
    }

    options = [
        "Joules → Kilojoules",
        "Kilojoules → Joules",
        "Kilocalories → Joules",
        "Joules → Kilocalories",
        "Kilowatt-hours → Joules",
        "Joules → Kilowatt-hours",
        "Kilocalories → Calories",
        "Calories → Kilocalories",
        "Joules → BTU",
        "BTU → Joules"
    ]

    print("\nENERGY CONVERTER")
    print("----------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def power_converter():
    conversions = {
        "1": ("Kilowatts", 0.001),
        "2": ("Watts", 1000),
        "3": ("Horsepower", 0.00134102),
        "4": ("Watts", 745.7),
        "5": ("Megawatts", 1e-6),
        "6": ("Watts", 1e6),
        "7": ("Kilowatts", 0.00135962),
        "8": ("Watts", 735.499)
    }

    options = [
        "Watts → Kilowatts",
        "Kilowatts → Watts",
        "Watts → Horsepower",
        "Horsepower → Watts",
        "Watts → Megawatts",
        "Megawatts → Watts",
        "Watts → Metric Horsepower",
        "Metric Horsepower → Watts"
    ]

    print("\nPOWER CONVERTER")
    print("----------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def data_converter():
    print("\nDATA / STORAGE CONVERTER")
    print("------------------------")
    print("1. Bytes → Kilobytes")
    print("2. Kilobytes → Megabytes")
    print("3. Megabytes → Gigabytes")
    print("4. Gigabytes → Terabytes")
    print("5. Terabytes → Gigabytes")
    print("6. Gigabytes → Megabytes")
    print("7. Megabytes → Kilobytes")
    print("8. Kilobytes → Bytes")
    print("9. Bits → Bytes")
    print("10. Bytes → Bits")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    value = get_value()

    conversions = {
        "1": ("KB", value / 1024),
        "2": ("MB", value / 1024),
        "3": ("GB", value / 1024),
        "4": ("TB", value / 1024),
        "5": ("GB", value * 1024),
        "6": ("MB", value * 1024),
        "7": ("KB", value * 1024),
        "8": ("Bytes", value * 1024),
        "9": ("Bytes", value / 8),
        "10": ("Bits", value * 8)
    }

    if choice in conversions:
        unit, result = conversions[choice]
        show_result(result, unit)
    else:
        print("Invalid option.")


def frequency_converter():
    conversions = {
        "1": ("Hertz", 1000),
        "2": ("Kilohertz", 0.001),
        "3": ("Megahertz", 1e-6),
        "4": ("Gigahertz", 1e-9),
        "5": ("Megahertz", 1000),
        "6": ("Gigahertz", 1000),
        "7": ("Hertz", 1e9),
        "8": ("Hertz", 1e6)
    }

    options = [
        "Kilohertz → Hertz",
        "Hertz → Kilohertz",
        "Hertz → Megahertz",
        "Hertz → Gigahertz",
        "Megahertz → Kilohertz",
        "Gigahertz → Megahertz",
        "Gigahertz → Hertz",
        "Megahertz → Hertz"
    ]

    print("\nFREQUENCY CONVERTER")
    print("-------------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def angle_converter():
    print("\nANGLE CONVERTER")
    print("----------------")
    print("1. Degrees → Radians")
    print("2. Radians → Degrees")
    print("3. Degrees → Gradians")
    print("4. Gradians → Degrees")
    print("5. Radians → Gradians")
    print("6. Gradians → Radians")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    value = get_value()

    if choice == "1":
        result = math.radians(value)
        show_result(result, "radians")
    elif choice == "2":
        result = math.degrees(value)
        show_result(result, "degrees")
    elif choice == "3":
        result = value * 10 / 9
        show_result(result, "gradians")
    elif choice == "4":
        result = value * 0.9
        show_result(result, "degrees")
    elif choice == "5":
        result = value * 200 / math.pi
        show_result(result, "gradians")
    elif choice == "6":
        result = value * math.pi / 200
        show_result(result, "radians")
    else:
        print("Invalid option.")


def fuel_economy_converter():
    conversions = {
        "1": ("L/100 km", 235.214583 / 1),
        "2": ("MPG", 235.214583 / 1),
        "3": ("km/L", 1 / 0.425144),
        "4": ("L/100 km", 100 / 1),
        "5": ("MPG", 2.35214583),
        "6": ("km/L", 0.425144)
    }

    options = [
        "MPG → L/100 km",
        "L/100 km → MPG",
        "MPG → km/L",
        "km/L → L/100 km",
        "L/100 km → km/L",
        "km/L → MPG"
    ]

    print("\nFUEL ECONOMY CONVERTER")
    print("----------------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    value = get_value()

    if choice == "1":
        result = 235.214583 / value
        show_result(result, "L/100 km")
    elif choice == "2":
        result = 235.214583 / value
        show_result(result, "MPG")
    elif choice == "3":
        result = value * 0.425144
        show_result(result, "km/L")
    elif choice == "4":
        result = 100 / value
        show_result(result, "L/100 km")
    elif choice == "5":
        result = 100 / value
        show_result(result, "km/L")
    elif choice == "6":
        result = value * 2.35214583
        show_result(result, "MPG")
    else:
        print("Invalid option.")


def digital_converter():
    conversions = {
        "1": ("Bits", 8),
        "2": ("Bytes", 1 / 8),
        "3": ("Megabits", 1 / 1000000),
        "4": ("Megabytes", 1 / 8000000),
        "5": ("Gigabits", 1 / 1000000000),
        "6": ("Gigabytes", 1 / 8000000000),
        "7": ("Bytes", 1024),
        "8": ("Kilobytes", 1 / 1024)
    }

    options = [
        "Bytes → Bits",
        "Bits → Bytes",
        "Bits → Megabits",
        "Bits → Megabytes",
        "Bits → Gigabits",
        "Bits → Gigabytes",
        "Kilobytes → Bytes",
        "Bytes → Kilobytes"
    ]

    print("\nDIGITAL / COMPUTING CONVERTER")
    print("-----------------------------")

    for i, option in enumerate(options, 1):
        print(f"{i:2}. {option}")
    print(" 0. Back")

    choice = input("Choose conversion: ")

    if choice == "0":
        return

    if choice in conversions:
        value = get_value()
        unit, multiplier = conversions[choice]
        show_result(value * multiplier, unit)
    else:
        print("Invalid option.")


def main():
    while True:
        print("\n")
        print("╔══════════════════════════════════════╗")
        print("║          UNIT CONVERTER v2.0         ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Length                           ║")
        print("║  2. Area                             ║")
        print("║  3. Volume                           ║")
        print("║  4. Weight / Mass                    ║")
        print("║  5. Temperature                      ║")
        print("║  6. Time                             ║")
        print("║  7. Speed                            ║")
        print("║  8. Pressure                         ║")
        print("║  9. Energy                           ║")
        print("║ 10. Power                            ║")
        print("║ 11. Data Storage                     ║")
        print("║ 12. Frequency                        ║")
        print("║ 13. Angle                            ║")
        print("║ 14. Fuel Economy                     ║")
        print("║ 15. Digital / Computing Units        ║")
        print("║  0. Exit                             ║")
        print("╚══════════════════════════════════════╝")

        choice = input("Choose a category: ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            area_converter()
        elif choice == "3":
            volume_converter()
        elif choice == "4":
            mass_converter()
        elif choice == "5":
            temperature_converter()
        elif choice == "6":
            time_converter()
        elif choice == "7":
            speed_converter()
        elif choice == "8":
            pressure_converter()
        elif choice == "9":
            energy_converter()
        elif choice == "10":
            power_converter()
        elif choice == "11":
            data_converter()
        elif choice == "12":
            frequency_converter()
        elif choice == "13":
            angle_converter()
        elif choice == "14":
            fuel_economy_converter()
        elif choice == "15":
            digital_converter()
        elif choice == "0":
            print("\nThank you for using Unit Converter.")
            break
        else:
            print("\nInvalid category. Please try again.")


if __name__ == "__main__":
    main()