import math

def get_xxx(theta1, d_1):
    xxx = math.tan(math.radians(theta1)) * d_1 * 3
    return xxx

def get_l_1 (xxx, d_1):
    l_1 = math.sqrt(xxx ** 2 + (d_1 * 3) ** 2)
    return l_1

def get_l_2 (hhh, xxx, d_2):
    l_2 = math.sqrt(((hhh * 3) - xxx) ** 2 + d_2 ** 2)
    return l_2

def get_time (l_1, nnn, l_2, v_sand):
    time = (l_1 + nnn * l_2) / (v_sand*5280/3600)
    return time