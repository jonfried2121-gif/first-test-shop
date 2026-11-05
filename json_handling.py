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

def push_new_order(id,item_id,quantity):
    order ={"id":id,"items":[{"product_id":item_id,"quantity":quantity}],"total":calculate_total_with_discount(item_id,quantity),"status":"open"}
    all_orders = read_json()
    all_orders.append(order)
    write_to_json(order)
    return

def calculate_regular_price(item_id,quantity):
     for item in products:
            if item["id"] == item_id:
                return item["price"] * quantity

    
def calculate_total_with_discount(item_id,quantity):
    for item in products:
        if item["id"] == item_id:
            befor_discount = item["price"] * quantity
            finall_price = befor_discount*discount_manager(befor_discount)
            return finall_price

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

if __name__ == "__main__":
    print(next_id())
