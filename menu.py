import logging
from input import start_order,show_all_orders,search_by_id,change_status,report
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
        if pick == 2:
            show_all_orders()
        if pick == 3:
            search_by_id()
        if pick == 4:
            change_status()
        if pick == 5:
            report()
        if pick == 0:
            break

menu()
