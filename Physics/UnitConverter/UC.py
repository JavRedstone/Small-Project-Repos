# Conversion factors
conversion_factors = {
    # Length
    'meter': 1,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'micrometer': 0.000001,
    'nanometer': 0.000000001,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34,
    'nautical mile': 1852,

    # Mass
    'kilogram': 1,
    'gram': 0.001,
    'milligram': 0.000001,
    'microgram': 0.000000001,
    'metric ton': 1000,
    'ounce': 0.0283495,
    'pound': 0.453592,
    'ton': 907.185,

    # Time
    'second': 1,
    'millisecond': 0.001,
    'microsecond': 0.000001,
    'nanosecond': 0.000000001,
    'minute': 60,
    'hour': 3600,
    'day': 86400,
    'week': 604800,
    'month': 2629800,
    'year': 31557600,

    # Temperature
    'celsius': lambda x: x,
    'fahrenheit': lambda x: (x - 32) * 5 / 9,
    'kelvin': lambda x: x + 273.15,

    # Other quantities
    'meter per second': 1,
    'kilometer per hour': 0.277778,
    'mile per hour': 0.44704,
    'knot': 0.514444,
    'square meter': 1,
    'square kilometer': 1000000,
    'square foot': 0.092903,
    'square yard': 0.836127,
    'square mile': 2590000,
    'cubic meter': 1,
    'liter': 0.001,
    'milliliter': 0.000001,
    'gallon': 0.00378541,
    'ounce (volume)': 0.0000295735,
    'pound (volume)': 0.000473176,
    'newton': 1,
    'dyne': 0.00001,
    'pound-force': 4.44822,
    'joule': 1,
    'calorie': 4.184,
    'electronvolt': 1.60219e-19
}

def convert(value, from_unit, to_unit):
    # Convert from base unit to the desired unit
    if to_unit in conversion_factors:
        conversion_fn = conversion_factors[to_unit]
        if callable(conversion_fn):
            base_value = value
            result = conversion_fn(base_value)
            return result
        else:
            # Convert the value to base unit
            base_value = value * conversion_factors[from_unit]
            return base_value / conversion_factors[to_unit]
    else:
        return None

def print_menu():
    print("Unit Conversion Menu:")
    print("1. Length")
    print("2. Mass")
    print("3. Time")
    print("4. Temperature")
    print("5. Other Quantities")
    print("6. Quit")

def print_sub_menu(category):
    print(f"{category} Conversion:")
    i = 1
    for unit in conversion_factors:
        if unit.lower() in category.lower():
            print(f"{i}. {unit.capitalize()}")
            i += 1

# Main program
while True:
    print_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':  # Length conversion
        print_sub_menu('Length')
        units = list(conversion_factors.keys())
        from_unit = input("Enter the source unit (choose from the list): ")
        while from_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            from_unit = input("Enter the source unit (choose from the list): ")
        to_unit = input("Enter the target unit (choose from the list): ")
        while to_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            to_unit = input("Enter the target unit (choose from the list): ")
        value = float(input("Enter the value: "))
        result = convert(value, from_unit.lower(), to_unit.lower())
        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}\n")
        else:
            print("Invalid unit.\n")

    elif choice == '2':  # Mass conversion
        print_sub_menu('Mass')
        units = list(conversion_factors.keys())
        from_unit = input("Enter the source unit (choose from the list): ")
        while from_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            from_unit = input("Enter the source unit (choose from the list): ")
        to_unit = input("Enter the target unit (choose from the list): ")
        while to_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            to_unit = input("Enter the target unit (choose from the list): ")
        value = float(input("Enter the value: "))
        result = convert(value, from_unit.lower(), to_unit.lower())
        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}\n")
        else:
            print("Invalid unit.\n")

    elif choice == '3':  # Time conversion
        print_sub_menu('Time')
        units = list(conversion_factors.keys())
        from_unit = input("Enter the source unit (choose from the list): ")
        while from_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            from_unit = input("Enter the source unit (choose from the list): ")
        to_unit = input("Enter the target unit (choose from the list): ")
        while to_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            to_unit = input("Enter the target unit (choose from the list): ")
        value = float(input("Enter the value: "))
        result = convert(value, from_unit.lower(), to_unit.lower())
        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}\n")
        else:
            print("Invalid unit.\n")

    elif choice == '4':  # Temperature conversion
        print_sub_menu('Temperature')
        units = list(conversion_factors.keys())
        from_unit = input("Enter the source unit (choose from the list): ")
        while from_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            from_unit = input("Enter the source unit (choose from the list): ")
        to_unit = input("Enter the target unit (choose from the list): ")
        while to_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            to_unit = input("Enter the target unit (choose from the list): ")
        value = float(input("Enter the value: "))
        result = convert(value, from_unit.lower(), to_unit.lower())
        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}\n")
        else:
            print("Invalid unit.\n")

    elif choice == '5':  # Other quantities conversion
        print_sub_menu('Other Quantities')
        units = list(conversion_factors.keys())
        from_unit = input("Enter the source unit (choose from the list): ")
        while from_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            from_unit = input("Enter the source unit (choose from the list): ")
        to_unit = input("Enter the target unit (choose from the list): ")
        while to_unit.lower() not in [unit.lower() for unit in units]:
            print("Invalid unit. Please choose from the available units.")
            to_unit = input("Enter the target unit (choose from the list): ")
        value = float(input("Enter the value: "))
        result = convert(value, from_unit.lower(), to_unit.lower())
        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}\n")
        else:
            print("Invalid unit.\n")

    elif choice == '6':  # Quit
        break

    else:
        print("Invalid choice. Please try again.\n")
