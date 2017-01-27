import os
from places import *

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
    def print_table(cls):
        """prints table"""
        pass

    @classmethod
    def print_menu(cls, title, list_options, exit_message):
        """prints menu"""
        Ui.clear()

        print(title)

        for i, menu_item in enumerate(list_options):
            print('({})'.format(i + 1), menu_item)

        print('(0)', exit_message)


    @classmethod
    def create_objects(cls, table):
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
        for county in state.in_s:
            if type(county) == County:
                for community in state.in_s:
                    if community.county_number == county.county_number:
                        county.in_county(community)

        return state

    @classmethod
    def load_data(cls, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]
        return table