import csv

capitals = {}
with open("C:/Users/ethan/Downloads/country-list.csv", newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    reader.fieldnames = [name.strip() for name in reader.fieldnames]

    for row in reader:
        country = row['Country'].strip().lower()
        capital = row['Capital'].strip()
        capitals[country] = capital

while True:
    country = input("Enter a country name (or 'exit' to quit): ").strip().lower()
    if country == 'exit':
        break
    capital = capitals.get(country)
    if capital:
        print(f"The capital of {country.title()} is {capital}.")
    else:
        print("Country not found.")
