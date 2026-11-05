import logging
from input import start_order,show_all_orders,search_by_id,change_status,report
logging.basicConfig(level=logging.info(format = "%(asctime)s%(levelname)s%(message)s"))

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
        if pick == 1:
            start_order()
            logging.info("the user is edditing a new order")
        if pick == 2:
            show_all_orders()
            logging.info("user wants to see al orders")
        if pick == 3:
            search_by_id()
            logging.info("user wants to search by id")
        if pick == 4:
            change_status()
            logging.info("user wants to change status")
        if pick == 5:
            report()
            logging.info("user wants to see report")
        if pick == 0:
            break

menu()
