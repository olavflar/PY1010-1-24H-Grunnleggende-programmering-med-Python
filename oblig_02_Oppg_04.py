# 4a: Opprette dictionary
data = {
    "Norge": {"hovedstad": "Oslo", "innbyggere": 0.634},
    "Italia": ["Roma", 2.873],
    "England": {"hovedstad": "London", "innbyggere": 8.982},
    "Frankrike": {"hovedstad": "Paris", "innbyggere": 2.161},
    "Tyskland": {"hovedstad": "Berlin", "innbyggere": 3.769},
}

print("Dictionary 'data' er opprettet.")

# 4b: Skriv in land
land = input("Skriv inn et land (f.eks. England): ").capitalize()

if land in data:
    hovedstad = data[land]["hovedstad"]
    innbyggere = data[land]["innbyggere"]
    print(f"{hovedstad} er hovedstaden i {land}, og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
    print(f"Beklager, informasjon om {land} finnes ikke i dictionaryen.")

# 4c: Legge til nytt land
nytt_land = input("Skriv inn et nytt land: ").capitalize()
hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}: ")
innbyggere = float(input(f"Skriv inn antall innbyggere (i mill.) i {hovedstad}: "))

# Oppdatere dictionaryen
data[nytt_land] = {"hovedstad": hovedstad, "innbyggere": innbyggere}
print(f"Oppdatert dictionary: {data}")
