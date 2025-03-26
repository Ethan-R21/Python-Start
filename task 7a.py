foods = ["Pizza", "Burger", "Pasta", "Sushi", "Tacos"]

print(" ".join(foods))

for food in foods:
    print(food)

print(foods[0], foods[4])

countries = []


while True:
  country = input("Enter a country ending in 'land' (or type 'finish' to stop): ")
  if country.lower() == "finish":
    break  
    
    countries.append(country)
print("Countries entered:", countries)
