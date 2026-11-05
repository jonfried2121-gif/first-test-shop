
def valid_number(number):
    try:
        if int(number) > 0 :
            return int(number)
    except ValueError:
        return
    return

def check_quantity():
    quantity = input("enter number of products you want")
    quantity = valid_number(quantity)
    return quantity

def check_product_id():
    product_id = input("enter id storage")
    product_id = valid_number(product_id)
    return product_id