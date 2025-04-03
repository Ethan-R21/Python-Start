country = input("Enter a country: ")

if country.endswith("land"):
    print("You have entered a 'land' country. There are 9 in the world.")
elif country.endswith("stan"):
    print("You have entered a 'stan' country. There are 7 in the world.")
elif country.endswith("ia"):
    print("You have entered an 'ia' country. There are many in the world.")
else:
    print("This country has a different ending.")
