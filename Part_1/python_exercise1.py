# Exercise 1
# Calculate year of birth
import datetime

name = input("Hello, What is your name?")  #Gets User to input date
age = int(input("How old are You?")) #Gets user to input age
birth_year = (2021 - age) #since the current year is 2021 we minus that from age to get birth year

print(f"OMG {name}, you are {age} years old so you were born in {birth_year}")
# This isnt accurate because the person may be born later in the year so it will get their year of birth wrong.

