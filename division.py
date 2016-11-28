# calced by euclidean_division
def euclidean(dividend, divisor):
    # calc division
    quotient = int(dividend) // int(divisor)
    # calc remainder
    remainder =  dividend - quotient * divisor

    if remainder < 0:
        # calc remainder
        remainder_inc =  dividend - (quotient + 1) * divisor
        remainder_dec =  dividend - (quotient - 1) * divisor

        if remainder_inc >= 0:
            quotient += 1
            remainder = remainder_inc
        else:
            quotient -= 1
            remainder = remainder_dec

    return {"quotient": int(quotient),
            "remainder": int(remainder)}
