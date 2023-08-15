# # def geo_zones(state):
# zones= {
#     "NORTH_CENTRAL": ["FCT", "Benue", "Kogi", "Kwara" "Nasarawa" "Niger" "Plateau"],
#     "NORTH_EAST": ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
#     "NORTH_WEST": ["Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"],
#     "SOUTH_EAST": ["Abia", "Anambra", "Ebonyi", " Enugu", "Imo"],
#     "SOUTH_SOUTH": ["Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers"],
#     "SOUTH_WEST": ["Ekiti", "Lagos", " Osun", "Ondo", "Ogun", "Oyo"]
#     }
#
# #     for zones, state in geo_zones.__str__():
# #         for y in zones:
# #             if y == state:
# #                 return zones
# #
# #
# # geo_zones = (input("enter state"))
# # zones = geo_zones
# # print(zones)
#
from enum import Enum


class GeoZones(Enum):

        NORTH_CENTRAL = "FCT", "Benue", "Kogi", "Kwara" "Nasarawa" "Niger" "Plateau",
        NORTH_EAST= ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"],
        NORTH_WEST= ["Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"],
        SOUTH_EAST = "Abia", "Anambra", "Ebonyi", " Enugu", "Imo",
        SOUTH_SOUTH = "Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers",
        SOUTH_WEST=  "Ekiti", "Lagos", " Osun", "Ondo", "Ogun", "Oyo"
def user_choice():
    user_input = input("Enter a state: ")

    if user_input.capitalize() in GeoZones.SOUTH_WEST.value:
        print("SOUTH WEST")
    elif user_input.capitalize() in GeoZones.SOUTH_SOUTH.value:
        print("SOUTH SOUTH")
    elif user_input.capitalize() in GeoZones.SOUTH_EAST.value:
        print("SOUTH EAST")
    elif user_input.capitalize() in GeoZones.NORTH_WEST.value:
        print("NORTH WEST")
    elif user_input.capitalize() in GeoZones.NORTH_CENTRAL.value:
        print("NORTH CENTRAL")
    elif user_input.capitalize() in GeoZones.NORTH_EAST.value:
        print("NORTH EAST")
    else:
        print("Invalid state")
        user_choice()

user_choice()
