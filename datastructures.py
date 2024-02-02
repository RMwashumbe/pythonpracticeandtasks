# list data structure, it is ordered and changeable
cars = ["Mercedes", "Nissan", "Toyota", "Range Rover"]
cars[1] = "Subaru"
cars.append("Mitsubishi")
cars.insert(2,"BMW")
cars.pop()
cars.sort()
cars.copy()
print(cars)

# this is a tuple, ordered. It is unchangeable
fruits = ("Mangoes", "Oranges", "Pineapples", "Avocado")
fruits.count(fruits)
my_tuple = (fruits)
count = len(my_tuple)
print(count)

#sets datastructures
countries = {"Kenya", "Uganda", "Tanzania", "Burundi", "Ethiopia"}
print(countries)

#dictionaries
matunda = {
    "amount" : 40,
    "jina" : "Ndizi",
    "rangi": "Yellow",
}
matunda["size"] = "Large"
matunda.pop("rangi")
print(matunda)