from ui import *
from places import *
import time

def options(state):
    """user choose options"""
    option = Ui.get_input("Choose option: ")
    if option == "1":
        list_statistic(state)
    elif option == "2":
        longest_city_names(state)
    elif option == "3":
        largest_county(state)
    elif option == "4":
        find_multiple_category_object(state)
    elif option == "5":
        advanced_search(state)
    elif option == "0":
        exit()
    else:
        Ui.print_message("Choose number 1 to 5 or 0 for exit")

def menu_start():
    """prints menu"""
    Ui.print_message("What would you like to do: ")
    options = ["List statistics", "Display 3 cities with longest names",
               "Display county's name with the largest number of communities",
               "Display locations, that belong to more than one category", "Advanced search"]
    Ui.print_menu("Main menu", options, "Exit program")

def list_statistic(state):
    """prints statistics about every element in state"""
    Ui.print_message(state.name)
    Ui.print_message("powiat"), Ui.print_message(County.nmb_of_instances)
    Ui.print_message("miasto"), Ui.print_message(City.nmb_of_instances)
    Ui.print_message("gmina wiejska"), Ui.print_message(Village_Community.nmb_of_instances)
    Ui.print_message("gmina miejska"), Ui.print_message(City_Community.nmb_of_instances)
    Ui.print_message("obszar wiejski"), Ui.print_message(Village_square.nmb_of_instances)
    Ui.print_message("delegatura"), Ui.print_message(Delegacy.nmb_of_instances)
    Ui.print_message("gmina miejsko-wiejska"), Ui.print_message(City_Village_Community.nmb_of_instances)

    time.sleep(5)

def largest_county(state):
    """find largest county"""
    amount_of_communities = 0
    for county in state.in_s:
        if type(county) == County:
            if len(county.in_c) > amount_of_communities:
                amount_of_communities = len(county.in_c)
                county_name = county.name
    Ui.print_message(county_name)

    time.sleep(5)

def longest_city_names(state):
    """finds three cities with longest names"""
    cities = []
    for city in state.in_s:
        if type(city) == City:
            cities.append(city.name)

    long_1 = cities[0]
    long_2 = cities[1]
    long_3 = cities[2]
    x = 3

    while x < len(cities):
        if len(long_1) < len(cities[x]):
            long_1 = cities[x]
        elif len(long_2) < len(cities[x]):
            long_2 = cities[x]
        elif len(long_3) < len(cities[x]):
            long_3 = cities[x]
        x += 1
    Ui.print_message(long_1)
    Ui.print_message(long_2)
    Ui.print_message(long_3)

    time.sleep(5)


def find_multiple_category_object(state):
    """finds multiple category locations"""
    locations = []
    x = 0
    while x < len(state.in_s)-1:
        if state.in_s[x].name == state.in_s[x+1].name:
            if state.in_s[x].name not in locations:
                locations.append(state.in_s[x].name)
        x += 1
    for location in locations:
        Ui.print_message(location)

    time.sleep(5)

def advanced_search(state):
    location = Ui.get_input("What are you looking for?: ")
    locations_with_given_name = []
    for place in state.in_s:
        if location == place.name:
            locations_with_given_name.append(place.name)
    Ui.print_message(locations_with_given_name)

def main():
    """initialized program"""
    state = Ui.create_objects(Ui.load_data('malopolska.csv'))
    while True:
        menu_start()
        try:
            options(state)
        except KeyError as err:
            Ui.print_message(err)

main()

if __name__ == '__main__':
    main()