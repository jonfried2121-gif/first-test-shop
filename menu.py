import logging

def menu():
    print("======= ORDER MENU =======")
    print("""
    1.Create order
    2. Show all orders
    3. Find order by id
    4. Close order
    5. Show sales report
    0. Exit""")
    while True:
        try:
            pick = int(input("Choose option"))
        except ValueError:
            print("please enter a number")
menu()