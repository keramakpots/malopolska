class State:
    nmb_of_instances = 0



    def __init__(self, name):
        State.nmb_of_instances += 1
        self.name = name
        self.in_s = []
        self.type = "województwo"


    def in_state(self, value):
        self.in_s.append(value)


class County:
    nmb_of_instances = 0


    def __init__(self, name, county_number):
        County.nmb_of_instances += 1
        self.name = name
        self.county_number = county_number
        self.in_c = []
        self.type = "powiat"


    def in_county(self, value):
        self.in_c.append(value)


class City_Community:
    nmb_of_instances = 0


    def __init__(self, name, county_number, community_number):
        City_Community.nmb_of_instances += 1
        self.name = name
        self.county_number = county_number
        self.community_number = community_number
        self.type = "gmina miejska"



class Village_Community:
    nmb_of_instances = 0


    def __init__(self, name, county_number, community_number):
        Village_Community.nmb_of_instances += 1
        self.name = name
        self.county_number = county_number
        self.community_number = community_number
        self.type = "gmina wiejska"


class City:
    nmb_of_instances = 0


    def __init__(self, name, county_number, community_number):
        City.nmb_of_instances += 1
        self.name = name
        self.county_number = county_number
        self.community_number = community_number
        self.type = "miasto"


class Village_square:
    nmb_of_instances = 0


    def __init__(self, name, county_number, community_number):
        Village_square.nmb_of_instances += 1
        self.name = name
        self.county_number = county_number
        self.community_number = community_number
        self.type = "obszar wiejski"


class City_Village_Community:
    nmb_of_instances = 0


    def __init__(self, name, county_number, community_number):
        City_Village_Community.nmb_of_instances += 1
        self.name = name
        self.county_number = county_number
        self.community_number = community_number
        self.type = "gmina miejsko-wiejska"

class Delegacy:
    nmb_of_instances = 0


    def __init__(self, name, county_number, community_number):
        Delegacy.nmb_of_instances += 1
        self.name = name
        self.county_number = county_number
        self.community_number = community_number
        self.type = "delegatura"
