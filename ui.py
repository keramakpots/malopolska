import os
from places import *
from tabulate import tabulate

class Ui:

    @classmethod
    def print_message(cls, message):
        """print simple info"""
        print(message)



    @classmethod
    def clear(cls):
        """clear screen"""

        os.system('cls' if os.name == 'nt' else 'clear')  # clear console

    @classmethod
    def get_input(cls, message):
        """gets input from user"""
        data = input(message)
        return data

    @classmethod
    def print_table(cls, table, title_list):
        """prints table"""
        Ui.clear()
        cell_size = list()

        for i, title in enumerate(title_list):
            cell_size.append(len(title))

        for items in table:
            for i, item in enumerate(items):
                try:
                    if cell_size[i] < len(str(item)):
                        cell_size[i] = len(str(item))
                except:
                    cell_size.append(len(str(item)))

        # how big table
        table_size = 1
        for dash in cell_size:
            table_size += (dash + 3)

        # printing table
        print('-' * table_size)

        for i, title in enumerate(title_list):
            if i == 0:
                print('|', end="")
            print(' {:{width}} |'.format(title, width=cell_size[i]), end="")

        print('\n' + '-' * table_size)

        for items in table:
            for i, item in enumerate(items):
                if i == 0:
                    print('|', end="")
                print(' {:{width}} |'.format(str(item), width=cell_size[i]), end="")
            print()

        print('-' * table_size)

    @classmethod
    def print_menu(cls, title, list_options, exit_message):
        """prints menu"""

        print(title)

        for i, menu_item in enumerate(list_options):
            print('({})'.format(i + 1), menu_item)

        print('(0)', exit_message)


    @classmethod
    def create_objects(cls, table):
        """It create's objects from a file"""
        x = 2
        state = State(table[1][4])
        while x < len(table):
            line = table[x]
            if line[5] == "powiat" or line[5] == "miasto na prawach powiatu":
                county = County(line[4], line[1])
                state.in_state(county)
            elif line[5] == "miasto":
                city = City(line[4], line[1], line[2])
                state.in_state(city)
            elif line[5] == "gmina miejska":
                city_community = City_Community(line[4], line[1], line[2])
                state.in_state(city_community)
            elif line[5] == "gmina wiejska":
                village_community = Village_Community(line[4], line[1], line[2])
                state.in_state(village_community)
            elif line[5] == "gmina miejsko-wiejska":
                city_village_community = City_Village_Community(line[4], line[1], line[2])
                state.in_state(city_village_community)
            elif line[5] == "obszar wiejski":
                village_square = Village_square(line[4], line[1], line[2])
                state.in_state(village_square)
            elif line[5] == "delegatura":
                delagacy = Delegacy(line[4], line[1], line[2])
                state.in_state(delagacy)
            x+=1

        for county in state.in_s:#adding community objects to a proper county
            if type(county) == County:
                for community in state.in_s:
                    if community.county_number == county.county_number and type(community) != County:
                        county.in_county(community)

        return state

    @classmethod
    def load_data(cls, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]
        return table