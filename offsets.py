# Updated offsets for App ver. 1.03 Regulation ver. 1.04
offsets: tuple[int, list[int]] = {
    "current_hp": (0x1ACD758, [0x0, 0x3E8]),  # int
    "current_stamina": (0x1ACD758, [0x0, 0x3F8]),  # int
    "is_ingame": (0x1D06EB0, [0x60]),  # int
    "is_game_focused": (0x1D06EB0, [0x68]),  # int
    "time_played": (0x1D278F0, [0xA4]),  # int
    "souls": (0x1D278F0, [0x10, 0x94]),  # int
    "humanities": (0x1D278F0, [0x10, 0x84]),  # int
    "level": (0x1D278F0, [0x10, 0x90]),  # int
    "deaths": (0x1D278F0, [0x98]),  # int
    "equip_load": (0x1D26460, [0x3BC]),  # float
    "max_equip_load": (0x1D278F0, [0x10, 0x594]),  # float
    "vitality": (0x1D278F0, [0x10, 0x40]),  # int
    "attunement": (0x1D278F0, [0x10, 0x48]),  # int
    "endurance": (0x1D278F0, [0x10, 0x50]),  # int
    "strength": (0x1D278F0, [0x10, 0x58]),  # int
    "dexterity": (0x1D278F0, [0x10, 0x60]),  # int
    "resistance": (0x1D278F0, [0x10, 0x88]),  # int
    "intelligence": (0x1D278F0, [0x10, 0x68]),  # int
    "faith": (0x1D278F0, [0x10, 0x70]),  # int
    "r_weapon_1": (0x1D278F0, [0x10, 0x578]),  # int
    "r_weapon_2": (0x1D278F0, [0x10, 0x580]),  # int
    "l_weapon_1": (0x1D278F0, [0x10, 0x574]),  # int
    "l_weapon_2": (0x1D278F0, [0x10, 0x57C]),  # int
    "max_hp": (0x1D278F0, [0x10, 0x1C]),  # int
    "max_stamina": (0x1D278F0, [0x10, 0x38]),  # int
    "pos_x": (0x1ACD758, [0x28, 0x10]),  # float
    "pos_y": (0x1ACD758, [0x28, 0x18]),  # float
    "pos_z": (0x1ACD758, [0x28, 0x14]),  # float
    "poise": (0x1D278F0, [0x10, 0x5F4]),  # int
    "bleed_resist": (0x1D278F0, [0x10, 0x5EC]),  # int
    "poison_resist": (0x1D278F0, [0x10, 0x5E4]),  # int
    "curse_resist": (0x1D278F0, [0x10, 0x5F0]),  # int
    "item_discovery": (0x1D278F0, [0x10, 0x5FC]),  # int
    "attunement_slots": (0x1D26460, [0x3CC]),  # int
    "physical_defense": (0x1D278F0, [0x10, 0x570]),  # int
    "vs_strike": (0x1D278F0, [0x10, 0x5A0]),  # int
    "vs_slash": (0x1D278F0, [0x10, 0x59C]),  # int
    "vs_thrust": (0x1D278F0, [0x10, 0x5A4]),  # int
    "magical_defense": (0x1D278F0, [0x10, 0x584]),  # int
    "flame_defense": (0x1D278F0, [0x10, 0x5A8]),  # int
    "lightning_defense": (0x1D278F0, [0x10, 0x5AC]),  # int
}
