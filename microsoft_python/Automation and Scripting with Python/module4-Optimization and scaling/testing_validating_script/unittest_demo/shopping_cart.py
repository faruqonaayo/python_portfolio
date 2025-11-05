def calculate_discount(price, discount_percentage):
    """
    Calculate the discounted price.

    :param price: Original price of the item
    :param discount_percentage: Discount percentage to be applied
    :return: Discounted price
    :rtype: float
    :raises ValueError: If discount_percentage is not between 0 and 100
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    discount_amount = (discount_percentage / 100) * price
    discounted_price = price - discount_amount
    return round(discounted_price, 2)
