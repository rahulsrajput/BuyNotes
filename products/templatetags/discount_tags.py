from django import template
import math

register = template.Library()

@register.simple_tag
def discountPrice(price,discount):
    if discount is None or discount is 0:
        return price
    
    sellPrice = price
    sellPrice = price - (price * discount/100)
    return math.floor(sellPrice)
