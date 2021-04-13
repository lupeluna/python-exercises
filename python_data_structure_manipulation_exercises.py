students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# 1. How many students are there?

student_count = len(students)
print(f"There are {student_count} students")

# There are 14 Students


# 2. How many students prefer light coffee? For each type of coffee roast?

count_light = 0
for student in students:
    if student['coffee_preference'] == 'light':
        count_light += 1
print(count_light) 

# 3 students


# 3. How many types of each pet are there?

horses = []
dogs = []
cats = []
for student in students:
    pets = student ['pets']
    for species in pets:
        pet_species = species['species']
        if pet_species == 'horse':
            horses.append(pet_species)
        if pet_species == 'dog':
            dogs.append(pet_species)
        if pet_species == 'cat':
            cats.append(pet_species)
print(f'There are {len(cats)} cats')
print(f'There are {len(dogs)} dogs')
print(f'There are {len(horses)} horses')

#There are 11 cats
#There are 3 dogs
#There are 4 horses


# 4. How many grades does each student have? Do they all have the same number of grades?

for student in students:
    print(student['student'], 'has', len(student['grades']))

## They each have 4 grades


# 5. What is each student's grade average?

for student in students:
    print(student['student'], sum(student['grades']) / len(student['grades']))

# Ada Lovelace 78.5
# Thomas Bayes 83.5
# Marie Curie 73.25
#Grace Hopper 78.5
#Alan Turing 81.5
#Rosalind Franklin 80.75
#Elizabeth Blackwell 84.5
#Rene Descartes 88.75
#Ahmed Zewail 88.75
#Chien-Shiung Wu 82.5
#William Sanford Nye 81.5
#Carl Sagan 91.0
#Jane Goodall 79.0
#Richard Feynman 89.0



# 6. How many pets does each student have?

for student in students:
    print(student['student'], len(student['pets']))

#Ada Lovelace 1
#Thomas Bayes 0
#Marie Curie 1
#Grace Hopper 2
#Alan Turing 3
#Rosalind Franklin 0
#Elizabeth Blackwell 1
#Rene Descartes 2
#Ahmed Zewail 2
#Chien-Shiung Wu 1
#William Sanford Nye 2
#Carl Sagan 1
#Jane Goodall 1
#Richard Feynman 1


# 7. How many students are in web development? data science?

web = 0
data = 0
for student in students:
    if student['course'] == 'web development':
        web += 1
    if student['course'] == 'data science':
        data += 1
print(f'There are {web} students in web development')
print(f'There are {data} students in data science')
    
# There are 7 students in web development
# There are 7 students in data science


# 8. What is the average number of pets for students in web development?

n_students_web = 0
total_web_pets = 0
for student in students:
    if student['course'] == 'web development':
        n_students_web += 1
        total_web_pets += len(student['pets'])
print('Web Development students have an average of ', (total_web_pets / n_students_web), ' pets.')

# Web Development students have an average of  1.2857142857142858  pets.


# 9. What is the average pet age for students in data science?

total_ds_pet_age = 0
number_ds_pets = 0

for student in students:
    if student['course'] == 'data science':
        pets = student['pets']
        for pet in pets:
            total_ds_pet_age += pet['age']
            number_ds_pets += 1
print('The average pet age for students in Data Sceince is', total_ds_pet_age / number_ds_pets)
        
# The average pet age for students in Data Sceince is 5.444444444444445


# 10. What is most frequent coffee preference for data science students?

light = 0
medium = 0
dark = 0

for student in students:
    if student['course'] == 'data science':
        if student['coffee_preference'] == 'light':
            light_count += 1
        elif student['coffee_preference'] == 'medium':
            medium += 1
        elif student['coffee_preference'] == 'dark':
            dark += 1
            
coffee_choices = dict(light = light, medium = medium, dark = dark)
        
coffee_preference = max(coffee_choices, key=coffee_choices.get)

print('The most frequent coffee preference for data science students is', coffee_preference)

# The most frequent coffee preference for data science students is medium


# 11. What is the least frequent coffee preference for web development students?

light = 0
medium = 0
dark = 0

for student in students:
    if student['course'] == 'web development':
        if student['coffee_preference'] == 'light':
            light += 1
        elif student['coffee_preference'] == 'medium':
            medium += 1
        elif student['coffee_preference'] == 'dark':
            dark += 1
            
coffee_choices = dict(light = light, medium = medium, dark = dark)
        
coffee_preference = min(coffee_choices, key=coffee_choices.get)

print('The least frequent coffee preference for web development students is', coffee_preference)

# The least frequent coffee preference for web development students is light



# 12. What is the average grade for students with at least 2 pets?

average_grade = 0
student_count = 0

for student in students:
    if len(student['pets']) >= 2:
        average_grade += sum(student['grades']) / len(student['grades'])
        student_count += 1
print(average_grade / student_count)

# 83.8 students


# 13. How many students have 3 pets?

three_pets = 0
for student in students:
    if len(student['pets']) >= 3:
        three_pets += 1
print(three_pets)

# 1 student


# 14. What is the average grade for students with 0 pets?

stu_0_pets = 0
avg_grade = 0
for student in students:
    if len(student['pets']) == 0:
        avg_grade += sum(student['grades']) / len(student['grades'])
        stu_0_pets += 1
print(f'The average grade for students with 0 pets is {avg_grade / stu_0_pets}')

# The average grade for students with 0 pets is 82.125



# 15. What is the average grade for web development students? data science students?

web_avg_grades = 0
ds_avg_grades = 0
ds_grades = 0
wd_grades = 0
for student in students:
    if student['course'] == 'data science':
        ds_avg_grades += sum(student['grades']) / len(student['grades'])
        ds_grades += 1
    if student['course'] == 'web development':
        web_avg_grades += sum(student['grades']) / len(student['grades'])
        wd_grades += 1
print(f'The average grade for web development is {web_avg_grades / wd_grades}')        
print(f'The average grade for data sceince is {ds_avg_grades / ds_grades}')

#The average grade for web development is 81.17857142857143
#The average grade for data sceince is 84.67857142857143


# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?

avg_grade_range = 0
num_dark_coffee = 0
for student in students:
    if student['coffee_preference'] == 'dark':
        avg_grade_range += max(student['grades']) - min(student['grades'])
        num_dark_coffee += 1
print(f'The average grade range for dark coffee drinkers is {avg_grade_range / num_dark_coffee}')

# The average grade range for dark coffee drinkers is 28.8



# 17. What is the average number of pets for medium coffee drinkers?

avg_pets_med_coff = 0
med_coffee_drinkers = 0
for student in students:
    if student['coffee_preference'] == 'medium':
        avg_pets_med_coff += len(student['pets'])
        med_coffee_drinkers += 1
print(f'The average number of pets for medium coffee drinkers is {avg_pets_med_coff / med_coffee_drinkers}')

# The average number of pets for medium coffee drinkers is 1.1666666666666667



# 18. What is the most common type of pet for web development students?

num_pets_wd_stu = {}
for student in students:
    if student['course'] == 'web development':
        for pet in student['pets']:
            if pet['species'] not in num_pets_wd_stu:
                num_pets_wd_stu[pet['species']] = 1
            else: 
                num_pets_wd_stu[pet['species']] += 1
most_common_pet = ''
curr_most = 0
for pet,count in num_pets_wd_stu.items():
    if count > curr_most:
        curr_most = count
        most_common_pet = pet
(f'The most common type of pet for web develpment is {most_common_pet}')

# 'The most common type of pet for web develpment is horse'



# 19. What is the average name length?

avg_name_len = 0
for student in students:
    avg_name_len += len(student['student'])
print(f'The average name length is {avg_name_len / len(students)}')

#  The average name length is 13.642857142857142



# 20. What is the highest pet age for light coffee drinkers?

highest_pet_age = 0
light_coffee = 0
for student in students:
    if student['coffee_preference'] == 'light':
        for pet in student['pets']:
            if pet['age'] >= highest_pet_age:
                highest_pet_age = pet['age']
print(f'The highest pet age for light coffee drinkers is {highest_pet_age}')

#  The highest pet age for light coffee drinkers is 8

