import json
from products import products
def next_id():
    all_id = read_json()
    print(all_id)
    if not all_id:
        return 1
    return all_id[len(all_id)-1]["id"] + 1

def in_stock(id):
    for product in products:
        if product["id"] == id:
            return True
    return

def push_new_order(id,item_list):
    order ={"id":id,"items":item_list,"total":calculate_total_with_discount(item_list) * discount_manager(calculate_total_with_discount(item_list)),"status":"open"}
    all_orders = read_json()
    all_orders.append(order)
    write_to_json(all_orders)
    return


     

    
def calculate_total_with_discount(item_list):
    total_price = 0
    for item in item_list:
        for product in products:
            if item["product_id"] ==product["id"]:
                total_price += product["price"] * item["quantity"]
    return total_price


def discount_manager(price):
    if price < 300:
        return 1.0
    if price > 300 and price < 700:
        return 0.95
    if price > 700 and price < 1500:
        return 0.90
    if price > 1500:
        return 0.85

def read_json():
    with open("order.json","r") as json_file:
        text = json.load(json_file)
        return text

def write_to_json(text):
    with open("order.json","w") as json_file:
        json.dump(text,json_file,indent=2)
        return
def percent_calculator(price):
    return 100 -(discount_manager(price) *100)

def search_json(id):
    all_orders = read_json()
    for order in all_orders:
        if order["id"] == id:
            return order
    return "no such order"

def change_to_close(id):
    all_orders = read_json()
    for order in all_orders:
        if order["id"] == id:
            if order["status"] == "open":
                order["status"] = "closed"
                print(order)
                write_to_json(all_orders)
                return "done"
            return "error: cant change from close to open"
    return"no such order"

def change_quantity(order_id,product_id,new_quantity):
    all_orders = read_json()
    for order in all_orders:
        if order["id"] == order_id:
            if order["status"] == "open":
                product_list = order["items"]
                for product in product_list:
                    
                    if product["product_id"] == product_id:
                        product["quantity"] += new_quantity
                order["total"] = calculate_total_with_discount(order["items"]) * discount_manager(calculate_total_with_discount(order["items"]))
                write_to_json(all_orders)
                return "changes done"
            return 
        
def number_of_orders():
    all_orders = read_json()
    return len(all_orders)

def expensive_order():
    expensive = sorted_orders()
    return expensive[0]

def top_three_orders():
    orders = sorted_orders()
    return orders[0:3]


def sorted_orders():
    all_orders = read_json()
    orders_list_sorted = sorted(all_orders, key= lambda k:(k["total"]))
    return orders_list_sorted

def print_order(order:dict):
    for key,val in order.items():
        if isinstance(val,list):
            for product in val:
                print(f"product id: {product["product_id"]},quantity: {product["quantity"]}")
        else:
            print(key, val)
    return

def print_orders(orders:list):
    for order in orders:
        print_order(order)
    return


                

        


if __name__ == "__main__":
    print(expensive_order())
