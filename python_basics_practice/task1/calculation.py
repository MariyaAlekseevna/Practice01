import math

def time_calculation(d_1, d_2, hhh, v_sand, nnn, theta1):
    xxx = math.tan(math.radians(theta1)) * d_1*3
    l_1 = math.sqrt(xxx ** 2 + (d_1*3) ** 2)
    l_2 = math.sqrt(((hhh*3) - xxx) ** 2 + d_2 ** 2)
    time = (l_1 + nnn * l_2) / (v_sand*5280/3600)
    return time