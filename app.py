from enum import Enum
from icecream import ic
import platform
import os
import json

FILE_NAME = 'dogs_list.json'
user_selection = ""
dogs_list = []


class Actions(Enum):
    EXIT = 1
    DISPLAY = 2
    ADD = 3
    DELETE = 4
    FIND = 5

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print("Welcome to the dogs list\nPlease type the desired action:")
    for action in Actions:
        print(f"{action.value} - {action.name}")
    return input("Your selection:\n")


def expanded_exit():
    ic("Goodbey")
    exit()
    
def add_dog():
    ic("Please input the following information:")
    dogs_list.append({"name": input("Dog's name\n"), "age": input("Dog's age\n"), "breed": input("Dog's breed\n")})
    save_dogs_to_file()
    clear_terminal()

def delete_dog():
    delete_input_name = input("Enter dog's name to delete\n")
    delete_input_age = input("Enter dog's age to delete\n")
    delete_input_breed = input("Enter dog's breed to delete\n")
    for dog in dogs_list:
        if dog["name"] == delete_input_name and dog["age"] == delete_input_age and dog["breed"] == delete_input_breed:
            dogs_list.remove(dog)
            clear_terminal()
            save_dogs_to_file()
            return ic("Dog removed from list")
    else:
        clear_terminal()
        return ic("Dog not found")

def display_dogs():
    if dogs_list == []:
        return ic("No data on dogs")
    else:
        for index, dog in enumerate(dogs_list):
            print(f"{index + 1}: name: {dog["name"]}, age: {dog["age"]}, breed: {dog["breed"]}.")

def find_dog():
    find_input_name = input("Enter dog's name to find\n")
    found = False
    for index, dog in enumerate(dogs_list):
        if dog["name"] == find_input_name:
            print(f"{index + 1}: name: {dog["name"]}, age: {dog["age"]}, breed: {dog["breed"]}")
            found = True
    if not found:
        ic("Dog not found")

def save_dogs_to_file():
    with open(FILE_NAME, 'w+') as f:
        json.dump(dogs_list, f, indent= 4)
        ic("File written successfully")

def load_dogs_from_file():
    global dogs_list
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            dogs_list = json.load(f)
            ic("File loaded successfully")
    else:
        ic("The file does not exist")


if __name__=="__main__":
    load_dogs_from_file()
    while True:
        try:
            user_selection = Actions(int(menu()))
            clear_terminal()
            if user_selection == Actions.EXIT: expanded_exit()
            elif user_selection == Actions.ADD: add_dog()
            elif user_selection == Actions.DELETE: delete_dog()
            elif user_selection == Actions.DISPLAY: display_dogs()
            elif user_selection == Actions.FIND: find_dog()
            else: print("Invalid Action")
        except ValueError:
            print("Invalid Action. Please enter a number between 1 and 5.")
