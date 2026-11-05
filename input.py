from validation import valid_number,check_product_id,check_quantity
from json_handling import next_id,in_stock,push_new_order,discount_manager,calculate_regular_price,percent_calculator,read_json,search_json,change_to_close
def start_order():
    product_id = check_product_id()
    if not product_id:
        return "please enter a valid number"
    if not in_stock(product_id):
        return "please enter item id in stock"
    quantity = check_quantity()
    if not quantity:
        return "the quantity number is not valid"
    order_id = next_id()
    push_new_order(order_id,product_id,quantity)
    before = calculate_regular_price(product_id,quantity)
    after = before * discount_manager(before)
    percent = percent_calculator(before)
    print(f"the price before discount is {before}, percent of discount is{percent}, and after discount is {after}")


def feature2__menu():
    print("""what do you want to do
    1. view all orders
    2. view order by id
    3. close order
    4. add another item to order""")
    pick = input("enter your pick")
    pick = valid_number()
    if not pick:
        return "error : please pick a number"
    if pick > 4:
        return "error: please pick a number in the scale"
    if pick == 1:
        show_all_orders()
    if pick ==2:
        search_by_id()
    if pick == 3:
        change_status()
    


def show_all_orders():
    all_orders = read_json()
    for order in all_orders:
        print(order)

def search_by_id():
    id = check_product_id()
    if not id:
        return "please enter a valid number"
    order = search_json(id)
    print(order)
    return

def change_status():
    id = check_product_id()
    if not id:
        return "please enter a valid number"
    res = change_to_close(id)
    print(res)
    return

def add_item():
    order_id = input("enter the order id")
    order_id = valid_number()
    if not order_id:
        return "no such order"
    product_id = check_product_id()
    if not product_id:
        return "please enter a valid number"
    if not in_stock(product_id):
        return "please enter item id in stock"
    quantity = check_quantity()
    if not quantity:
        return "the quantity number is not valid"
    
    
    








if __name__ == "__main__":
    print(change_status())     


    












   

