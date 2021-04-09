# 1. Write the code to take a string and produce a dictionary out of that 
# string such that the output looks like the following: Some thoughts:

truck = "toyota tacoma"

truck.split()

make = truck.split()
model = truck.split()[1]

truck = {
    "make": "toyota"
    "model": "tacoma"
}

print(truck)


# 2.  Write the code that takes a dictionary containing make/model for a 
# vehicle and capitalizes the first character of the make and the model:


for vehicle in truck:
    truck[‘make’] = truck[‘make’].capitalize()
    truck[‘model’] = truck[‘model’].capitalize()
print(truck)


# 3. Create a list of 3 dictionaries where each dictionary represents a 
# vehicle, as above Write the code that operates on that list of 
# dictionaries in order to uppercase the entire make and model values.

def dict(car1, car2, car3):
    return car1.title, car2.title, car3.title

    trucks = [
        {
            "make": "Toyota"
            "model": "Tacoma" 
        },
        {
            "make": "Mazda"
            "model": "Rx7"
        }
        {
            "make": "Toyota"
            "model": "mr2"
        }
    ]
truck["make"] = truck["make"].upper()
truck["model"] = truck["model"].upper()

for truck in trucks:
    truck["make"] = truck["make"].upper()
    truck["model"] = truck["model"].upper()

trucks