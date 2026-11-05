from validation import valid_number,check_product_id,check_quantity
from json_handling import next_id,in_stock,push_new_order,discount_manager,calculate_regular_price,percent_calculator
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

if __name__ == "__main__":
    print(start_order())


    











if __name__ == "__main__":
    print()
   

