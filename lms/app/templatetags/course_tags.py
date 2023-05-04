from django import template
import math
register = template.Library()

@register.simple_tag
def discount_calculation(price, discount):
    if discount is None or discount is 0:
        return price
    sellprice = price
    sellprice = price - (price * discount/100)
    return math.floor(sellprice)

# @register.simple_tag
# def free_calculation(price, discount):
#     sellprice = price -(price * discount/100)
#     if discount is 100:
#         return sellprice