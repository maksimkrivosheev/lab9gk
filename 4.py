# def calculate_tax(income):
#     if income <= 10000:
#         return income * 0.1
#     elif income <= 20000:
#         return income * 0.15
#     else:
#         return income * 0.2

tax_stavka_nizkaya = 0.1
tax_stavka_srednya = 0.15
tax_stavka_vysokay = 0.2
rating_nizkiy = 10000
rating_sredny = 20000

def calculate_tax(income):
    if income <= rating_nizkiy:
        return income * tax_stavka_nizkaya
    elif income <= rating_sredny:
        return income * tax_stavka_srednya
    else:
        return income * tax_stavka_vysokay
