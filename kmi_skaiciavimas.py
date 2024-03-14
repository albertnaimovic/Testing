def kmi(weight, height):
    if weight <= 20 or weight >= 240:
        raise ValueError
    if height <= 0.40 or height >= 3.40:
        raise ValueError
    return round(weight / height**2, 1)
