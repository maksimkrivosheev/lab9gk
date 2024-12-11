# def calculate_shipping(country, weight):
#     if country == "USA":
#         if weight < 5:
#             return 10
#         else:
#             return 20
#     elif country == "Canada":
#         if weight < 5:
#             return 15
#         else:
#             return 25
#     else:
#         if weight < 5:
#             return 30
#         else:
#             return 50

def calculate_shipping(country, weight):
    shipping = {
        "USA": {True: 10, False: 20},
        "Canada": {True: 15, False: 25},
        "default": {True: 30, False: 50}
    }
    rule = shipping.get(country, shipping["default"])
    return rule[weight < 5]

