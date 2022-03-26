from __init__ import DarkSoulsRemastered
from pymem import Pymem
from offsets import offsets

from utils import get_pointer

# DarkSoulsRemastered().add_level(-1)
DarkSoulsRemastered().loop()

# pm = Pymem("DarkSoulsRemastered")
# module = pm.base_address

# hp_ptr = get_pointer(pm, base + offsets["current_hp"][0], offsets["current_hp"][1])
# hp_ptr = get_pointer(pm, base + offsets["current_hp"][0], offsets["current_hp"][1])
# hp_ptr = get_pointer(pm, module + offsets["r_weapon_1"][0], offsets["r_weapon_1"][1])
# hp = pm.read_int(hp_ptr)
# print(hp_ptr)
# print(hex(hp_ptr))
# print(f"{hp_ptr:X}")
# print(hp)
# print(souls)