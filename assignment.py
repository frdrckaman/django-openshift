import pandas as pd

db = []
print("**** Product Menu ****")
print("1. Add Product")
print("2. Update Product")
print("3. Delete Product")
print("4. Search Product")
print("5. View Product")
print("6. Exit")
choice = input("Enter your choice:")


def AddProduct(produuct):
    db.append(produuct)

def ViewProduct():
    return db


def main(choice):
    if choice == '1':
        pid = input("Enter PID:")
        name = input("Enter Name:")
        quantity = input("Enter Quantity:")
        price = input("Enter Price:")

        product = {'pid': pid, 'name': name, 'quantity': quantity, 'price': price}

        AddProduct(product)


main(choice)
print(ViewProduct())


def UpdateProduct(pid):
    pass


def DeleteProduct(pid):
    pass


def SearchProduct(name):
    pass


def CheckPid(pid):
    pass
