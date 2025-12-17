people = [
    {
        "name":"Shem",
        "house":"Kinoo"
    },
    {
        "name":"Caleb",
        "house":"muthure"
    },
    {
        "name":"Nicole",
        "house":"Co-operation"
    }
]

# def f(person):
#     return person["name"]
people.sort(key=lambda person: person["name"])
print(people)