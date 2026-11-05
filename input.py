from validation import valid_number,check_product_id,check_quantity
from json_handling import next_id,in_stock,push_new_order,discount_manager,percent_calculator,read_json,search_json,change_to_close,calculate_total_with_discount,change_quantity,number_of_orders,expensive_order,top_three_orders,print_order,print_orders
def start_order():
    item_list =[]
    while True:
        product_id = check_product_id()
        if not product_id:
            return "please enter a valid number"
        if not in_stock(product_id):
            return "please enter item id in stock"
        quantity = check_quantity()
        if not quantity:
            return "the quantity number is not valid"
        item_list.append({"product_id":product_id,"quantity":quantity})
        next_item = input("do yo uwant to add another item yes/no")
        if next_item == "yes":
            continue
        elif next_item =="no":
            break
        else:
            print("no valid answer")
            break
            
    order_id = next_id()
    push_new_order(order_id,item_list)
    before = calculate_total_with_discount(item_list)
    after = before * discount_manager(before)
    percent = percent_calculator(before)
    print(f"the price before discount is {before}, percent of discount is{percent}, and after discount is {after}")

    


def show_all_orders():
    all_orders = read_json()
    for order in all_orders:
        print_order(order)
    return

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
    order_id = valid_number(order_id)
    if not order_id:
        return "no such order"
    product_id = check_product_id()
    if not product_id:
        return "please enter a valid number"
    if not in_stock(product_id):
        return "please enter item id in stock"
    quantity = check_quantity()
    if quantity:
        res = change_quantity(order_id,product_id,quantity)
    else:
        return "invalid number"
    if res:
        return res
    return "the order is closed"


def report():
    orders = read_json()
    if not orders:
        return "no orders yet"
    number_orders = number_of_orders()
    most_expensive = expensive_order()
    expensive_list = top_three_orders()
    print(number_orders)
    print_order(most_expensive)
    print_orders(expensive_list)
    return

 

    
    
    








if __name__ == "__main__":
    print((start_order()))     


    












   

