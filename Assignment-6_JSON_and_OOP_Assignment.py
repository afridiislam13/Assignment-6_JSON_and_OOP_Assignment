# # Assignment 1
# #Task:1
#
# import json
#
# class Employee:
#     def __init__(self, name, dob, height, city, state):
#         self.name = name
#         self.dob = dob
#         self.height = height
#         self.city = city
#         self.state = state
#
# def read_employee_data(filename):
#     with open(filename, 'r') as file:
#         data = json.load(file)
#         employees_data = data['employees']
#
#     employees_list = []
#     for employee_data in employees_data:
#         employee = Employee(
#             employee_data['Name'],
#             employee_data['DOB'],
#             employee_data['Height'],
#             employee_data['City'],
#             employee_data['State']
#         )
#         employees_list.append(employee)
#
#     return employees_list
#
# if __name__ == "__main__":
#     employees_file = "employee.json"
#     employees_objects = read_employee_data(employees_file)
#
#     # Print the list of Employee objects
#     for employee in employees_objects:
#         print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")
#
#
# # Task:2
# import json
#
# indian_states_capitals = {
#     "West Bengal": "Kolkata",
#     "Assam": "Dispur",
#     "Bihar": "Patna",
#     "Gujarat": "Gandhinagar",
#     "Karnataka": "Bengaluru",
#     "Maharashtra": "Mumbai",
#     "Tamil Nadu": "Chennai"
# }
#
# # Write the dictionary to a JSON file
# with open("indian_states_capitals.json", "w") as file:
#     json.dump(indian_states_capitals, file)


# # Assignment 2
#
# class Dog:
#     def __init__(self, name, age, coat_color):
#         self.name = name
#         self.age = age
#         self.coat_color = coat_color
#
#     def description(self):
#         print(f"{self.name} is {self.age} years old.")
#
#     def get_info(self):
#         print(f"{self.name}'s coat color is {self.coat_color}.")
#
#
# class JackRussellTerrier(Dog):
#     def __init__(self, name, age, coat_color, weight):
#         super().__init__(name, age, coat_color)
#         self.weight = weight
#
#     def bark(self):
#         print(f"{self.name} is barking.")
#
#     def fetch(self):
#         print(f"{self.name} is fetching the ball.")
#
#
# class Bulldog(Dog):
#     def __init__(self, name, age, coat_color, height):
#         super().__init__(name, age, coat_color)
#         self.height = height
#
#     def snore(self):
#         print(f"{self.name} is snoring loudly.")
#
#     def sit(self):
#         print(f"{self.name} is sitting.")
#
#
# # Create objects of 'Dog', 'JackRussellTerrier', and 'Bulldog'
# dog = Dog("Max", 5, "Brown")
# jack = JackRussellTerrier("Jack", 2, "White and Brown", 8)
# bull = Bulldog("Bull", 3, "Fawn", 12)
#
# # Call methods from the 'Dog' class
# dog.description()
# dog.get_info()
#
# # Call methods from the 'JackRussellTerrier' class
# jack.description()
# jack.bark()
# jack.fetch()
#
# # Call methods from the 'Bulldog' class
# bull.description()
# bull.snore()
# bull.sit()
