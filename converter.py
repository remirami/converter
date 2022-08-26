
def converterCtoF():
    while True:
        try:
            f = 1.8
            c = float(input("Insert number: "))
            fahrenheit = (float(f) * c + 32)
            fahrenheit_format = "{:.2f}".format(fahrenheit)
            print("Temperature is: ", fahrenheit_format,"F")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def converterFtoC():
    while True:
        try:
            c = 1.8
            f = float(input("Insert number: "))
            celsius = (float(f - 32) / c)
            celsius_format = "{:.2f}".format(celsius)
            print("Temperature is:", celsius_format,"C")
            break
        except ValueError:
            print("That is not a proper value! Try again.")
 
def convertmphToKmh():
    while True:
        try:
            m = 1.609
            s = float(input("Give the mph: "))
            k = (float(m) * s)
            kmh_format = "{:.2f}".format(k)
            print("Your speed is: ", kmh_format, "km/h")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def convertkmhToMph():
    while True:
        try:
            m = 0.621
            s = float(input("Give the kmh: "))
            k = (float(s) * m)
            mph_format = "{:.2f}".format(k)
            print("Your speed is: ", mph_format, "mp/h")
            break
        except ValueError:
            print("That is not a proper value! Try again.")
def convertInchToCm():
    while True:
        try:
            i = 2.54
            s = float(input("Give inches: "))
            k = (float(i) * s)
            inch_format = "{:.2f}".format(k)
            print(inch_format, "cm")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def convertCmtoInch():
    while True:
        try:
            c = 0.3937
            s = float(input("Give centimeters: "))
            k = (float(s) * c)
            cm_format = "{:.2f}".format(k)
            print(cm_format, "")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def convertFttoCm():
    while True:
        try:
            f = 30.48
            s = float(input("Give ft amount: "))
            k = (float(f) * s)
            ft_format = "{:.2f}".format(k)
            print(ft_format, "cm")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def convertCmtoFt():
    while True:
        try:
            c = 0.032808399
            s = float(input("Give cm amount: "))
            k = (float(c) * s)
            cmft_format = "{:.2f}".format(k)
            print(cmft_format, "ft")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def convertFttoInch():
    while True:
        try:
            f = 12
            s = float(input("Give ft: "))
            k = (float(f) * s)
            ftin_format = "{:.2f}".format(k)
            print(ftin_format, "inch")
            break
        except ValueError:
            print("That is not a proper value! Try again.")
    
def convertInchtoFt():
    while True:
        try:
            i = 0.0833333333
            s = float(input("Give inches: "))
            k = (float(s) * i)
            inft_format = "{:.2f}".format(k)
            print(inft_format, "ft")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def convertCuptoDl():
    while True:
        try:
            c = 2.36588237
            s = float(input("Give cup(s): "))
            k = (float(s) * c)
            cup_format = "{:.2f}".format(k)
            print(cup_format, "Dl")
            break
        except ValueError:
            print("That is not a proper value! Try again.")
 
def convertDltoCup():
    while True:
        try:
            d = 0.422675284
            s = float(input("Give Deciliter(s): "))
            k = (float(s) * d)
            dl_format = "{:.2f}".format(k)
            print(dl_format, "Cups")
            break
        except ValueError:
            print("That is not a proper value! Try again.")
def convertLbstoKg():
    while True:
        try:
            l = 0.45359237
            s = float(input("Give lbs amount: "))
            k = (float(s) * l)
            lbs_format = "{:.2f}".format(k)
            print(lbs_format, "kg")
            break
        except ValueError:
            print("That is not a proper value! Try again.")

def convertKgtoLbs():
    while True:
        try:
            kg = 2.20462262
            s = float(input("Give kilogram amount: "))
            k = (float(s) * kg)
            kg_format = "{:.2f}".format(k)
            print(kg_format, "lbs")
            break
        except ValueError:
            print("That is not a proper value! Try again.")
print("/////////////////////////")
print("/////////////////////////")


while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Miles to Kilometers")
    print("4. Kilometers to Miles")
    print("5. Inches to Centimeters")
    print("6. Centimeters to Inches")
    print("7. Feet to Centimeters")
    print("8. Centimeters to Feet")
    print("9. Feet to Inches")
    print("10. Inches to Feet")
    print("11. Cup to Deciliter")
    print("12. Deciliter to Cup")
    print("13. Pounds to Kilograms")
    print("14. Kilograms to Pounds")
    print("15. Exit")

    print("/////////////////////////")
    print("/////////////////////////")

    try:
        choice = int(input("Choose what you wanna do: "))
   
        if choice == 1:
            print("You chose convert Celsius to Fahrenheit")
            converterCtoF()
        elif choice == 2:
            print("You chose convert Fahrenheit to Celsius")
            converterFtoC()
        elif choice == 3:
            print("You chose convert Miles to Kilometers")
            convertmphToKmh()
        elif choice == 4:
            print("You chose convert Kilometers to Miles")
            convertkmhToMph()
        elif choice == 5:
            print("You chose convert Inches to Centimeters")
            convertInchToCm()
        elif choice == 6:
            print("You chose convert Centimeters to Inches")
            convertCmtoInch()
        elif choice == 7:
            print("You chose convert Feet to Centimeters")
            convertFttoCm()
        elif choice == 8:
            print("You chose convert Centimeters to Feet")
            convertCmtoFt()
        elif choice == 9:
            print("You chose convert Feet to Inches")
            convertFttoInch()
        elif choice == 10:
            print("You chose convert Inches to Feet")
            convertInchtoFt()
        elif choice == 11:
            print("You chose convert Cup(s) to Deciliter")
            convertCuptoDl()
        elif choice == 12:
            print("You chose convert Deciliter to Cups")
            convertDltoCup()
        elif choice == 13:
            print("You chose convert Pounds to Kilograms")
            convertLbstoKg()
        elif choice == 14:
            print("You chose convert Kilograms to Pounds")
            convertKgtoLbs()
        else:
            break
    except ValueError:
        print("That is not a proper value! Try again.")