from datetime import date



print("welcome to the interactive personal data collector")

print("")

name=(input("please enter your name: "))
age=int(input("please enter your age:"))
height=float(input("please enter your height in meter:"))
favourite_number =int(input("please enter your favourite number : "))

print(" ")

print("thank you! here is the information we collected :")

print("")
    
print (f"this is name {name} type :- {type(name)} adress :- {id(name)}")
print(f"this is age{age} type :-{type (age)} adress:- {id(age)}")
print(f"this is height{height} type :-{type (height)} adress :- {id(height)}")
print(f"this is favourite_number{favourite_number} type:-{type(favourite_number)} adress:-{id(favourite_number)}")

print("")

current_year= date.today().year
birth_year= current_year - age
print(f"your birth year is approximtely :{birth_year} based on age of {age}")
print("")
    
print("thank you for using the personal data collector. goodbye!")
