person = {
    "Emri" : "Ylli",
    "Mbiemer": "Zeneli",
    "Kompania": "jCoders",
    "Titulli": "Programer",
    "Mosha": 15
}
emri = person["Emri"]
print(emri)

x = person.get("Emri")
print(x)

person["Titulli"] = "Programer"
print(person)

if "Kompania" in person:
    print("po eshte ne objekt")
else:
    print("jo nuk eshte ne objekt")