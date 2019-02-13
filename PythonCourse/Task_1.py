
def prining_out_any_variables(name, age):
    print(name +" "+  age)

def printing_how_many_decades_user_lives(age):
    if(len(age)==1):
        print("This is your first decade on Earth!")
    else:
        print("You already live "+ age[0]+" decades!")

name = input("Enter your name here: ")
age = input("Please now enter your age: ")

prining_out_any_variables(name,age)

first_data= input("Please enter ANY data: ")
second_data= input("Please enter ANY data again: ")

prining_out_any_variables(first_data,second_data)

printing_how_many_decades_user_lives(age)

