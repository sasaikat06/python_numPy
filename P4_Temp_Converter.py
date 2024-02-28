def ferenheit_to_kelvin(ferenheit):
    kelvin = ((5*ferenheit - 160)+(273*9))/9
    return kelvin

def ferenheit_to_celcius(ferenheit):
    celcius = (5*ferenheit - 160)/9
    return celcius

def kelvin_to_ferenheit(kelvin):
    ferenheit = ((9*kelvin-273)+160)/5
    return ferenheit

def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273
    return celcius 

def celcius_to_ferenheit(celcius):
    ferenheit = (9*celcius - 160)/5
    return ferenheit 

def celcius_to_kelvin(celcius):
    kelvin = celcius + 273
    return kelvin





while True:
    print("\n Temperature Converter")
    print("1. Ferenheit to Kelvin")
    print("2. Ferenheit to Celcius")
    print("3. Kelvin to Ferenheit")
    print("4. Kelvin to Celcius")
    print("5. Celcius to Ferenheit")
    print("6. Celcius to Kelvin")
    print("7. None of them")

    choice = input("Select your choice (1-7)")

    if choice == "7":
        print("Get Lost!")
        break

    temperature = float(input("Enter the temperature : "))
    if choice == "1":
        print(f"{temperature} Ferenheit is equal to {ferenheit_to_kelvin(temperature):.2f} Kelvin")
        break

    elif choice == "2":
        print(f"{temperature} Ferenheit is equal to {ferenheit_to_celcius(temperature):.2f} Celcius")
        break

    elif choice == "3":
        print(f"{temperature} Kelvin is equal to {kelvin_to_ferenheit(temperature):.2f} Ferenheit")
        break
    elif choice == "4":
        print(f"{temperature} Kelvin is equal to {kelvin_to_celcius(temperature):.2f} Celcius")
        break

    elif choice == "5":
        print(f"{temperature} Celcius is equal to {celcius_to_ferenheit(temperature):.2f} Ferenheit")
        break

    elif choice == "6":
        print(f"{temperature} Celcius is equal to {celcius_to_kelvin(temperature):.2f} Kelvin")
        break

    else:
        print("You are nonsence")
        break



