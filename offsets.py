offsets: tuple[int, list[int]] = {
    "is_ingame": (0x1CF3CD0, [0x60]),  # int
    "is_game_focused": (0x1CF3CD0, [0x68]),  # int
    "character_name": (0x1D146E0, [0xDB8]),  # string
    "time_played": (0x1D146E0, [0xA4]),  # int
    "souls": (0x1D146E0, [0xDA4]),  # int
    "estus": (0x1D146E0, [0x10, 0xF2C]),  # int
    "humanities": (0x1D146E0, [0xD94]),  # int
    "level": (0x1D146E0, [0xDA0]),  # int
    "deaths": (0x1D146E0, [0x98]),  # int
    "equip_load": (0x1D13240, [0x3BC]),  # float
    "max_equip_load": (0x1D13240, [0x334]),  # float
    "next_level_req_souls": (0x1D13240, [0x3D4]),  # int
    "vitality": (0x1D146E0, [0xD50]),  # int
    "attunement": (0x1D146E0, [0xD58]),  # int
    "endurance": (0x1D146E0, [0xD60]),  # int
    "strength": (0x1D146E0, [0xD68]),  # int
    "dexterity": (0x1D146E0, [0xD70]),  # int
    "resistance": (0x1D146E0, [0xD98]),  # int
    "intelligence": (0x1D146E0, [0xD78]),  # int
    "faith": (0x1D146E0, [0xFE0]),  # int
    "r_weapon_1": (0x1D146E0, [0x10, 0x578]),  # int
    "r_weapon_2": (0x1D146E0, [0x10, 0x580]),  # int
    "l_weapon_1": (0x1D146E0, [0x10, 0x574]),  # int
    "l_weapon_2": (0x1D146E0, [0x10, 0x57C]),  # int
    "current_hp": (0x1D146E0, [0xD24]),  # int
    "max_hp": (0x1D146E0, [0xD2C]),  # int
    "pos_x": (0x1CFDC48, [0xBE0]),  # float
    "pos_y": (0x1CFDC48, [0xBE4]),  # float
    "pos_z": (0x1CFDC48, [0xBE8]),  # float
}
