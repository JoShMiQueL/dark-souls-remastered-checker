import logging
from os import system
from time import sleep
from pymem import Pymem, logger, exception, process
from offsets import offsets
from utils import get_pointer, convert_time
from websocket_server import WebsocketServer
import json


class GameState:
  INGAME = "In game"
  INGAME_UNFOCUSED = "In game (unfocused)"
  MENU = "In menu"
  UNKNOWN = "Unknown"


class DarkSoulsRemastered:
  refresh_time_in_ms: int = 100
  m = Pymem()
  server: WebsocketServer
  game_attached = False
  module = None
  base: int = 0

  game_state: str = ""
  time_played: int = 0
  souls: int = 0
  humanities: int = 0
  level: int = 0
  deaths: int = 0
  equip_load: float = 0.0
  max_equip_load: float = 0.0
  equip_load_percentage: int = 0
  vitality: int = 0
  attunement: int = 0
  endurance: int = 0
  strength: int = 0
  dexterity: int = 0
  resistance: int = 0
  intelligence: int = 0
  faith: int = 0
  r_weapon_1: int = 0
  r_weapon_2: int = 0
  l_weapon_1: int = 0
  l_weapon_2: int = 0
  current_hp: int = 0
  max_hp: int = 0
  pos_x: float = 0.0
  pos_y: float = 0.0
  pos_z: float = 0.0
  current_stamina: int = 0
  max_stamina: int = 0
  poise: int = 0
  bleed_resist: int = 0
  poison_resist: int = 0
  curse_resist: int = 0
  item_discovery: int = 0
  attunement_slots: int = 0
  physical_defense: int = 0
  vs_strike: int = 0
  vs_slash: int = 0
  vs_thrust: int = 0
  magical_defense: int = 0
  flame_defense: int = 0
  lightning_defense: int = 0

  def __init__(self):
    logger.setLevel(logging.INFO)

  def attach(self):
    """
    Attach to the game
    """
    try:
      self.m.open_process_from_name("DarkSoulsRemastered")
      self.module = process.module_from_name(self.m.process_handle, "DarkSoulsRemastered.exe")
      if not hasattr(self.module, "lpBaseOfDll"):
        raise exception.ProcessNotFound("DarkSoulsRemastered.exe")
      self.base = self.module.lpBaseOfDll
      self.game_attached = True
    except exception.ProcessNotFound as e:
      self.game_attached = False

  def detach(self):
    """
    Detach from the game
    """
    if self.game_attached:
      self.m.close_process()
      self.game_attached = False

  def gameState(self):
    """
    Get the current game state

    :return: current game state
    """
    is_ingame_pointer = get_pointer(self.m,
                                    self.base + offsets["is_ingame"][0], offsets["is_ingame"][1])
    is_ingame = self.m.read_int(is_ingame_pointer)
    is_game_focused_pointer = get_pointer(self.m,
                                          self.base + offsets["is_game_focused"][0], offsets["is_game_focused"][1])
    is_game_focused = self.m.read_int(is_game_focused_pointer)
    if is_ingame == 1 and is_game_focused == 1:
      return GameState.INGAME
    elif is_ingame == 1 and is_game_focused == 0:
      return GameState.INGAME_UNFOCUSED
    elif is_ingame == 196608:
      return GameState.MENU
    else:
      return GameState.UNKNOWN

  # region Stats
  def get_time_played(self):
    """
    Get the current time played

    :return: tuple of hours, minutes, seconds, milliseconds
    """
    time_played_pointer = get_pointer(self.m,
                                      self.base + offsets["time_played"][0], offsets["time_played"][1])
    time_played = self.m.read_int(time_played_pointer)
    return time_played

  def get_souls(self) -> int:
    """
    Get the current amount of souls
    """
    souls_pointer = get_pointer(self.m,
                                self.base + offsets["souls"][0], offsets["souls"][1])
    souls = self.m.read_int(souls_pointer)
    return souls

  def add_souls(self, souls: int) -> bool:
    """
    Add souls to the current amount of souls

    :param souls: amount of souls to add
    :return: True if successful, False if not
    """
    souls_pointer = get_pointer(self.m,
                                self.base + offsets["souls"][0], offsets["souls"][1])
    _souls = self.m.read_int(souls_pointer)
    _souls += souls
    return self.process.write(souls_pointer, _souls)

  def set_souls(self, souls: int) -> bool:
    """
    Set the current amount of souls

    :param souls: amount of souls to set
    :return: True if successful, False if not
    """
    souls_pointer = get_pointer(self.m,
                                self.base + offsets["souls"][0], offsets["souls"][1])
    return self.process.write(souls_pointer, souls)

  def get_humanities(self) -> int:
    """
    Get the current amount of humanities
    """
    humanities_pointer = get_pointer(self.m,
                                     self.base + offsets["humanities"][0], offsets["humanities"][1])
    humanities = self.m.read_int(humanities_pointer)
    return humanities

  def add_humanities(self, humanities: int) -> bool:
    """
    Add humanities to the current amount of humanities

    :param humanities: amount of humanities to add
    :return: True if successful, False if not
    """
    humanities_pointer = get_pointer(self.m,
                                     self.base + offsets["humanities"][0], offsets["humanities"][1])
    _humanities = self.m.read_int(humanities_pointer)
    _humanities += humanities
    return self.process.write(humanities_pointer, _humanities)

  def set_humanities(self, humanities: int) -> bool:
    """
    Set the current amount of humanities

    :param humanities: amount of humanities to set
    :return: True if successful, False if not
    """
    humanities_pointer = get_pointer(self.m,
                                     self.base + offsets["humanities"][0], offsets["humanities"][1])
    return self.process.write(humanities_pointer, humanities)

  def get_level(self) -> int:
    """
    Get the current level
    """
    level_pointer = get_pointer(self.m,
                                self.base + offsets["level"][0], offsets["level"][1])
    level = self.m.read_int(level_pointer)
    return level

  def add_level(self, level: int) -> bool:
    """
    Add level to the current level

    :param level: amount of level to add
    :return: True if successful, False if not
    """
    level_pointer = get_pointer(self.m,
                                self.base + offsets["level"][0], offsets["level"][1])
    _level = self.m.read_int(level_pointer)
    _level += level
    return self.process.write(level_pointer, _level)

  def set_level(self, level: int) -> bool:
    """
    Set the current level

    :param level: amount of level to set
    :return: True if successful, False if not
    """
    level_pointer = get_pointer(self.m,
                                self.base + offsets["level"][0], offsets["level"][1])
    return self.process.write(level_pointer, level)

  def get_deaths(self) -> int:
    """
    Get the current amount of deaths
    """
    deaths_pointer = get_pointer(self.m,
                                 self.base + offsets["deaths"][0], offsets["deaths"][1])
    deaths = self.m.read_int(deaths_pointer)
    return deaths

  def add_deaths(self, deaths: int) -> bool:
    """
    Add deaths to the current amount of deaths

    :param deaths: amount of deaths to add
    :return: True if successful, False if not
    """
    deaths_pointer = get_pointer(self.m,
                                 self.base + offsets["deaths"][0], offsets["deaths"][1])
    _deaths = self.m.read_int(deaths_pointer)
    _deaths += deaths
    return self.process.write(deaths_pointer, _deaths)

  def set_deaths(self, deaths: int) -> bool:
    """
    Set the current amount of deaths

    :param deaths: amount of deaths to set
    :return: True if successful, False if not
    """
    deaths_pointer = get_pointer(self.m,
                                 self.base + offsets["deaths"][0], offsets["deaths"][1])
    return self.process.write(deaths_pointer, deaths)

  def get_equip_load(self) -> float:
    """
    Get the current equip load
    """
    equip_load_pointer = get_pointer(self.m,
                                     self.base + offsets["equip_load"][0], offsets["equip_load"][1])
    equip_load = self.m.read_float(equip_load_pointer)
    return float(f"{equip_load:.2f}")

  def get_max_equip_load(self) -> float:
    """
    Get the max equip load
    """
    max_equip_load_pointer = get_pointer(self.m,
                                         self.base + offsets["max_equip_load"][0], offsets["max_equip_load"][1])
    max_equip_load = self.m.read_float(max_equip_load_pointer)
    return float(f"{max_equip_load:.2f}")

  def get_equip_load_percentage(self) -> float:
    """
    Get the equip load percentage
    """
    equip_load = self.get_equip_load()
    max_equip_load = self.get_max_equip_load()
    return float(f"{equip_load / max_equip_load * 100:.2f}")

  def get_vitality(self) -> int:
    """
    Get the current vitality
    """
    vitality_pointer = get_pointer(self.m,
                                   self.base + offsets["vitality"][0], offsets["vitality"][1])
    vitality = self.m.read_int(vitality_pointer)
    return vitality

  def add_vitality(self, vitality: int) -> bool:
    """
    Add vitality to the current vitality

    :param vitality: amount of vitality to add
    :return: True if successful, False if not
    """
    vitality_pointer = get_pointer(self.m,
                                   self.base + offsets["vitality"][0], offsets["vitality"][1])
    _vitality = self.m.read_int(vitality_pointer)
    _vitality += vitality
    return self.process.write(vitality_pointer, _vitality)

  def set_vitality(self, vitality: int) -> bool:
    """
    Set the current vitality

    :param vitality: amount of vitality to set
    :return: True if successful, False if not
    """
    vitality_pointer = get_pointer(self.m,
                                   self.base + offsets["vitality"][0], offsets["vitality"][1])
    return self.process.write(vitality_pointer, vitality)

  def get_attunement(self) -> int:
    """
    Get the current attunement
    """
    attunement_pointer = get_pointer(self.m,
                                     self.base + offsets["attunement"][0], offsets["attunement"][1])
    attunement = self.m.read_int(attunement_pointer)
    return attunement

  def add_attunement(self, attunement: int) -> bool:
    """
    Add attunement to the current attunement

    :param attunement: amount of attunement to add
    :return: True if successful, False if not
    """
    attunement_pointer = get_pointer(self.m,
                                     self.base + offsets["attunement"][0], offsets["attunement"][1])
    _attunement = self.m.read_int(attunement_pointer)
    _attunement += attunement
    return self.process.write(attunement_pointer, _attunement)

  def set_attunement(self, attunement: int) -> bool:
    """
    Set the current attunement

    :param attunement: amount of attunement to set
    :return: True if successful, False if not
    """
    attunement_pointer = get_pointer(self.m,
                                     self.base + offsets["attunement"][0], offsets["attunement"][1])
    return self.process.write(attunement_pointer, attunement)

  def get_endurance(self) -> int:
    """
    Get the current endurance
    """
    endurance_pointer = get_pointer(self.m,
                                    self.base + offsets["endurance"][0], offsets["endurance"][1])
    endurance = self.m.read_int(endurance_pointer)
    return endurance

  def add_endurance(self, endurance: int) -> bool:
    """
    Add endurance to the current endurance

    :param endurance: amount of endurance to add
    :return: True if successful, False if not
    """
    endurance_pointer = get_pointer(self.m,
                                    self.base + offsets["endurance"][0], offsets["endurance"][1])
    _endurance = self.m.read_int(endurance_pointer)
    _endurance += endurance
    return self.process.write(endurance_pointer, _endurance)

  def set_endurance(self, endurance: int) -> bool:
    """
    Set the current endurance

    :param endurance: amount of endurance to set
    :return: True if successful, False if not
    """
    endurance_pointer = get_pointer(self.m,
                                    self.base + offsets["endurance"][0], offsets["endurance"][1])
    return self.process.write(endurance_pointer, endurance)

  def get_strength(self) -> int:
    """
    Get the current strength
    """
    strength_pointer = get_pointer(self.m,
                                   self.base + offsets["strength"][0], offsets["strength"][1])
    strength = self.m.read_int(strength_pointer)
    return strength

  def add_strength(self, strength: int) -> bool:
    """
    Add strength to the current strength

    :param strength: amount of strength to add
    :return: True if successful, False if not
    """
    strength_pointer = get_pointer(self.m,
                                   self.base + offsets["strength"][0], offsets["strength"][1])
    _strength = self.m.read_int(strength_pointer)
    _strength += strength
    return self.process.write(strength_pointer, _strength)

  def set_strength(self, strength: int) -> bool:
    """
    Set the current strength

    :param strength: amount of strength to set
    :return: True if successful, False if not
    """
    strength_pointer = get_pointer(self.m,
                                   self.base + offsets["strength"][0], offsets["strength"][1])
    return self.process.write(strength_pointer, strength)

  def get_dexterity(self) -> int:
    """
    Get the current dexterity
    """
    dexterity_pointer = get_pointer(self.m,
                                    self.base + offsets["dexterity"][0], offsets["dexterity"][1])
    dexterity = self.m.read_int(dexterity_pointer)
    return dexterity

  def add_dexterity(self, dexterity: int) -> bool:
    """
    Add dexterity to the current dexterity

    :param dexterity: amount of dexterity to add
    :return: True if successful, False if not
    """
    dexterity_pointer = get_pointer(self.m,
                                    self.base + offsets["dexterity"][0], offsets["dexterity"][1])
    _dexterity = self.m.read_int(dexterity_pointer)
    _dexterity += dexterity
    return self.process.write(dexterity_pointer, _dexterity)

  def set_dexterity(self, dexterity: int) -> bool:
    """
    Set the current dexterity

    :param dexterity: amount of dexterity to set
    :return: True if successful, False if not
    """
    dexterity_pointer = get_pointer(self.m,
                                    self.base + offsets["dexterity"][0], offsets["dexterity"][1])
    return self.process.write(dexterity_pointer, dexterity)

  def get_resistance(self) -> int:
    """
    Get the current resistance
    """
    resistance_pointer = get_pointer(self.m,
                                     self.base + offsets["resistance"][0], offsets["resistance"][1])
    resistance = self.m.read_int(resistance_pointer)
    return resistance

  def add_resistance(self, resistance: int) -> bool:
    """
    Add resistance to the current resistance

    :param resistance: amount of resistance to add
    :return: True if successful, False if not
    """
    resistance_pointer = get_pointer(self.m,
                                     self.base + offsets["resistance"][0], offsets["resistance"][1])
    _resistance = self.m.read_int(resistance_pointer)
    _resistance += resistance
    return self.process.write(resistance_pointer, _resistance)

  def set_resistance(self, resistance: int) -> bool:
    """
    Set the current resistance

    :param resistance: amount of resistance to set
    :return: True if successful, False if not
    """
    resistance_pointer = get_pointer(self.m,
                                     self.base + offsets["resistance"][0], offsets["resistance"][1])
    return self.process.write(resistance_pointer, resistance)

  def get_intelligence(self) -> int:
    """
    Get the current intelligence
    """
    intelligence_pointer = get_pointer(self.m,
                                       self.base + offsets["intelligence"][0], offsets["intelligence"][1])
    intelligence = self.m.read_int(intelligence_pointer)
    return intelligence

  def add_intelligence(self, intelligence: int) -> bool:
    """
    Add intelligence to the current intelligence

    :param intelligence: amount of intelligence to add
    :return: True if successful, False if not
    """
    intelligence_pointer = get_pointer(self.m,
                                       self.base + offsets["intelligence"][0], offsets["intelligence"][1])
    _intelligence = self.m.read_int(intelligence_pointer)
    _intelligence += intelligence
    return self.process.write(intelligence_pointer, _intelligence)

  def set_intelligence(self, intelligence: int) -> bool:
    """
    Set the current intelligence

    :param intelligence: amount of intelligence to set
    :return: True if successful, False if not
    """
    intelligence_pointer = get_pointer(self.m,
                                       self.base + offsets["intelligence"][0], offsets["intelligence"][1])
    return self.process.write(intelligence_pointer, intelligence)

  def get_faith(self) -> int:
    """
    Get the current faith
    """
    faith_pointer = get_pointer(self.m,
                                self.base + offsets["faith"][0], offsets["faith"][1])
    faith = self.m.read_int(faith_pointer)
    return faith

  def add_faith(self, faith: int) -> bool:
    """
    Add faith to the current faith

    :param faith: amount of faith to add
    :return: True if successful, False if not
    """
    faith_pointer = get_pointer(self.m,
                                self.base + offsets["faith"][0], offsets["faith"][1])
    _faith = self.m.read_int(faith_pointer)
    _faith += faith
    return self.process.write(faith_pointer, _faith)

  def set_faith(self, faith: int) -> bool:
    """
    Set the current faith

    :param faith: amount of faith to set
    :return: True if successful, False if not
    """
    faith_pointer = get_pointer(self.m,
                                self.base + offsets["faith"][0], offsets["faith"][1])
    return self.process.write(faith_pointer, faith)

  def get_r_weapon_1(self) -> int:
    """
    Get the current right weapon 1
    """
    r_weapon_1_pointer = get_pointer(self.m,
                                     self.base + offsets["r_weapon_1"][0], offsets["r_weapon_1"][1])
    r_weapon_1 = self.m.read_int(r_weapon_1_pointer)
    return r_weapon_1

  def get_r_weapon_2(self) -> int:
    """
    Get the current right weapon 2
    """
    r_weapon_2_pointer = get_pointer(self.m,
                                     self.base + offsets["r_weapon_2"][0], offsets["r_weapon_2"][1])
    r_weapon_2 = self.m.read_int(r_weapon_2_pointer)
    return r_weapon_2

  def get_l_weapon_1(self) -> int:
    """
    Get the current left weapon 1
    """
    l_weapon_1_pointer = get_pointer(self.m,
                                     self.base + offsets["l_weapon_1"][0], offsets["l_weapon_1"][1])
    l_weapon_1 = self.m.read_int(l_weapon_1_pointer)
    return l_weapon_1

  def get_l_weapon_2(self) -> int:
    """
    Get the current left weapon 2
    """
    l_weapon_2_pointer = get_pointer(self.m,
                                     self.base + offsets["l_weapon_2"][0], offsets["l_weapon_2"][1])
    l_weapon_2 = self.m.read_int(l_weapon_2_pointer)
    return l_weapon_2

  def get_current_hp(self) -> int:
    """
    Get the current hp
    """
    current_hp_pointer = get_pointer(self.m,
                                     self.base + offsets["current_hp"][0], offsets["current_hp"][1])
    current_hp = self.m.read_int(current_hp_pointer)
    return current_hp

  def get_max_hp(self) -> int:
    """
    Get the max hp
    """
    max_hp_pointer = get_pointer(self.m,
                                 self.base + offsets["max_hp"][0], offsets["max_hp"][1])
    max_hp = self.m.read_int(max_hp_pointer)
    return max_hp

  def get_pos_x(self) -> float:
    """
    Get the current x position
    """
    pos_x_pointer = get_pointer(self.m,
                                self.base + offsets["pos_x"][0], offsets["pos_x"][1])
    pos_x = self.m.read_float(pos_x_pointer)
    return pos_x

  def get_pos_y(self) -> float:
    """
    Get the current y position
    """
    pos_y_pointer = get_pointer(self.m,
                                self.base + offsets["pos_y"][0], offsets["pos_y"][1])
    pos_y = self.m.read_float(pos_y_pointer)
    return pos_y

  def get_pos_z(self) -> float:
    """
    Get the current z position
    """
    pos_z_pointer = get_pointer(self.m,
                                self.base + offsets["pos_z"][0], offsets["pos_z"][1])
    pos_z = self.m.read_float(pos_z_pointer)
    return pos_z

  def get_current_stamina(self) -> int:
    """
    Get the current stamina
    """
    current_stamina_pointer = get_pointer(self.m,
                                          self.base + offsets["current_stamina"][0], offsets["current_stamina"][1])
    current_stamina = self.m.read_int(current_stamina_pointer)
    return current_stamina

  def get_max_stamina(self) -> int:
    """
    Get the max stamina
    """
    max_stamina_pointer = get_pointer(self.m,
                                      self.base + offsets["max_stamina"][0], offsets["max_stamina"][1])
    max_stamina = self.m.read_int(max_stamina_pointer)
    return max_stamina

  def get_attunement_slots(self) -> int:
    """
    Get the current attunement slots
    """
    attunement_slots_pointer = get_pointer(self.m,
                                           self.base + offsets["attunement_slots"][0], offsets["attunement_slots"][1])
    attunement_slots = self.m.read_int(attunement_slots_pointer)
    return attunement_slots
  
  def get_poise(self) -> int:
    """
    Get the current poise
    """
    poise_pointer = get_pointer(self.m,
                                self.base + offsets["poise"][0], offsets["poise"][1])
    poise = self.m.read_int(poise_pointer)
    return poise
  
  def get_bleed_resist(self) -> int:
    """
    Get the current bleed resist
    """
    bleed_resist_pointer = get_pointer(self.m,
                                       self.base + offsets["bleed_resist"][0], offsets["bleed_resist"][1])
    bleed_resist = self.m.read_int(bleed_resist_pointer)
    return bleed_resist
  
  def get_poison_resist(self) -> int:
    """
    Get the current poison resist
    """
    poison_resist_pointer = get_pointer(self.m,
                                        self.base + offsets["poison_resist"][0], offsets["poison_resist"][1])
    poison_resist = self.m.read_int(poison_resist_pointer)
    return poison_resist
  
  def get_curse_resist(self) -> int:
    """
    Get the current curse resist
    """
    curse_resist_pointer = get_pointer(self.m,
                                       self.base + offsets["curse_resist"][0], offsets["curse_resist"][1])
    curse_resist = self.m.read_int(curse_resist_pointer)
    return curse_resist

  def get_item_discovery(self) -> int:
    """
    Get the current item discovery
    """
    item_discovery_pointer = get_pointer(self.m,
                                         self.base + offsets["item_discovery"][0], offsets["item_discovery"][1])
    item_discovery = self.m.read_int(item_discovery_pointer)
    return item_discovery
  
  def get_physical_defense(self) -> int:
    """
    Get the current physical defense
    """
    physical_defense_pointer = get_pointer(self.m,
                                           self.base + offsets["physical_defense"][0], offsets["physical_defense"][1])
    physical_defense = self.m.read_int(physical_defense_pointer)
    return physical_defense

  def get_vs_strike(self) -> int:
    """
    Get the current vs strike
    """
    vs_strike_pointer = get_pointer(self.m,
                                    self.base + offsets["vs_strike"][0], offsets["vs_strike"][1])
    vs_strike = self.m.read_int(vs_strike_pointer)
    return vs_strike
  
  def get_vs_slash(self) -> int:
    """
    Get the current vs slash
    """
    vs_slash_pointer = get_pointer(self.m,
                                   self.base + offsets["vs_slash"][0], offsets["vs_slash"][1])
    vs_slash = self.m.read_int(vs_slash_pointer)
    return vs_slash
  
  def get_vs_thrust(self) -> int:
    """
    Get the current vs thrust
    """
    vs_thrust_pointer = get_pointer(self.m,
                                    self.base + offsets["vs_thrust"][0], offsets["vs_thrust"][1])
    vs_thrust = self.m.read_int(vs_thrust_pointer)
    return vs_thrust
  
  def get_magical_defense(self) -> int:
    """
    Get the current magical defense
    """
    magical_defense_pointer = get_pointer(self.m,
                                          self.base + offsets["magical_defense"][0], offsets["magical_defense"][1])
    magical_defense = self.m.read_int(magical_defense_pointer)
    return magical_defense
  
  def get_flame_defense(self) -> int:
    """
    Get the current flame defense
    """
    flame_defense_pointer = get_pointer(self.m,
                                        self.base + offsets["flame_defense"][0], offsets["flame_defense"][1])
    flame_defense = self.m.read_int(flame_defense_pointer)
    return flame_defense

  def get_lightning_defense(self) -> int:
    """
    Get the current lightning defense
    """
    lightning_defense_pointer = get_pointer(self.m,
                                            self.base + offsets["lightning_defense"][0], offsets["lightning_defense"][1])
    lightning_defense = self.m.read_int(lightning_defense_pointer)
    return lightning_defense
  # endregion

  def _new_client(self, client, server: WebsocketServer):
    while True:
      object = {
          "game_attached": self.game_attached,
      }
      if self.game_attached:
        object = {
            "game_attached": self.game_attached,
            "game_state": self.game_state,
        }
      if self.game_attached and (self.game_state == GameState.INGAME or self.game_state == GameState.INGAME_UNFOCUSED):
        object = {
            "game_attached": self.game_attached,
            "game_state": self.game_state,
            "stats": {
                "time_played": {
                    "hours": convert_time(self.time_played)[0],
                    "minutes": convert_time(self.time_played)[1],
                    "seconds": convert_time(self.time_played)[2],
                    "milliseconds": self.time_played,
                },
                "souls": self.souls,
                "humanities": self.humanities,
                "level": self.level,
                "deaths": self.deaths,
                "equip_load": self.equip_load,
                "max_equip_load": self.max_equip_load,
                "equip_load_percentage": self.equip_load_percentage,
                "vitality": self.vitality,
                "attunement": self.attunement,
                "endurance": self.endurance,
                "strength": self.strength,
                "dexterity": self.dexterity,
                "resistance": self.resistance,
                "intelligence": self.intelligence,
                "faith": self.faith,
                "r_weapon_1": self.r_weapon_1,
                "r_weapon_2": self.r_weapon_2,
                "l_weapon_1": self.l_weapon_1,
                "l_weapon_2": self.l_weapon_2,
                "current_hp": self.current_hp,
                "max_hp": self.max_hp,
                "pos_x": self.pos_x,
                "pos_y": self.pos_y,
                "pos_z": self.pos_z,
                "current_stamina": self.current_stamina,
                "max_stamina": self.max_stamina,
                "poise": self.poise,
                "bleed_resist": self.bleed_resist,
                "poison_resist": self.poison_resist,
                "curse_resist": self.curse_resist,
                "item_discovery": self.item_discovery,
                "attunement_slots": self.attunement_slots,
                "physical_defense": self.physical_defense,
                "vs_strike": self.vs_strike,
                "vs_slash": self.vs_slash,
                "vs_thrust": self.vs_thrust,
                "magical_defense": self.magical_defense,
                "flame_defense": self.flame_defense,
                "lightning_defense": self.lightning_defense,
            }
        }
      server.send_message(client, json.dumps(object))
      sleep(self.refresh_time_in_ms / 1000)

  def read_memory(self):
    """
    Read the memory
    """
    try:
      self.game_state = self.gameState()
    except exception.MemoryReadError as e:
      self.game_state = GameState.UNKNOWN
    if self.game_state == GameState.INGAME or self.game_state == GameState.INGAME_UNFOCUSED:
      self.time_played = self.get_time_played()
      self.souls = self.get_souls()
      self.humanities = self.get_humanities()
      self.level = self.get_level()
      self.deaths = self.get_deaths()
      self.equip_load = self.get_equip_load()
      self.max_equip_load = self.get_max_equip_load()
      self.equip_load_percentage = self.get_equip_load_percentage()
      self.vitality = self.get_vitality()
      self.attunement = self.get_attunement()
      self.endurance = self.get_endurance()
      self.strength = self.get_strength()
      self.dexterity = self.get_dexterity()
      self.resistance = self.get_resistance()
      self.intelligence = self.get_intelligence()
      self.faith = self.get_faith()
      self.r_weapon_1 = self.get_r_weapon_1()
      self.r_weapon_2 = self.get_r_weapon_2()
      self.l_weapon_1 = self.get_l_weapon_1()
      self.l_weapon_2 = self.get_l_weapon_2()
      self.current_hp = self.get_current_hp()
      self.max_hp = self.get_max_hp()
      self.pos_x = self.get_pos_x()
      self.pos_y = self.get_pos_y()
      self.pos_z = self.get_pos_z()
      self.current_stamina = self.get_current_stamina()
      self.max_stamina = self.get_max_stamina()
      self.poise = self.get_poise()
      self.bleed_resist = self.get_bleed_resist()
      self.poison_resist = self.get_poison_resist()
      self.curse_resist = self.get_curse_resist()
      self.item_discovery = self.get_item_discovery()
      self.attunement_slots = self.get_attunement_slots()
      self.physical_defense = self.get_physical_defense()
      self.vs_strike = self.get_vs_strike()
      self.vs_slash = self.get_vs_slash()
      self.vs_thrust = self.get_vs_thrust()
      self.magical_defense = self.get_magical_defense()
      self.flame_defense = self.get_flame_defense()
      self.lightning_defense = self.get_lightning_defense()

  def print_memory(self):
    print(f"--- Game Attached: {self.game_attached} ---")
    if self.game_attached:
      print(f"Game state: {self.game_state}")
      if self.game_state == GameState.INGAME or self.game_state == GameState.INGAME_UNFOCUSED:
        print(
            f"time_played: {self.time_played}ms, {convert_time(self.time_played)[0]}h {convert_time(self.time_played)[1]}m {convert_time(self.time_played)[2]}s")
        print(f"Souls: {self.souls}")
        print(f"Humanities: {self.humanities}")
        print(f"Level: {self.level}")
        print(f"Deaths: {self.deaths}")
        print(f"Equip Load: {self.equip_load}")
        print(f"Max Equip Load: {self.max_equip_load}")
        print(f"Equip Load Percentage: {self.equip_load_percentage}%")
        print(f"Vitality: {self.vitality}")
        print(f"Attunement: {self.attunement}")
        print(f"Endurance: {self.endurance}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Resistance: {self.resistance}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Faith: {self.faith}")
        print(f"Right Weapon 1: {self.r_weapon_1}")
        print(f"Right Weapon 2: {self.r_weapon_2}")
        print(f"Left Weapon 1: {self.l_weapon_1}")
        print(f"Left Weapon 2: {self.l_weapon_2}")
        print(f"Current HP: {self.current_hp}")
        print(f"Max HP: {self.max_hp}")
        print(f"Position X: {self.pos_x}")
        print(f"Position Y: {self.pos_y}")
        print(f"Position Z: {self.pos_z}")
        print(f"Current Stamina: {self.current_stamina}")
        print(f"Max Stamina: {self.max_stamina}")
        print(f"Poise: {self.poise}")
        print(f"Bleed Resist: {self.bleed_resist}")
        print(f"Poison Resist: {self.poison_resist}")
        print(f"Curse Resist: {self.curse_resist}")
        print(f"Item Discovery: {self.item_discovery}")
        print(f"Attunement Slots: {self.attunement_slots}")
        print(f"Physical Defense: {self.physical_defense}")
        print(f"VS Strike: {self.vs_strike}")
        print(f"VS Slash: {self.vs_slash}")
        print(f"VS Thrust: {self.vs_thrust}")
        print(f"Magical Defense: {self.magical_defense}")
        print(f"Flame Defense: {self.flame_defense}")
        print(f"Lightning Defense: {self.lightning_defense}")

  def start(self):
    self.attach()
    if self.game_attached:
      self.read_memory()
    self.print_memory()

  def loop(self):
    """
    Start the main loop
    """
    try:
      self.server = WebsocketServer(host="localhost", port=9001)
      self.server.set_fn_new_client(self._new_client)
      self.server.run_forever(threaded=True)
      while True:
        self.start()
        sleep(self.refresh_time_in_ms / 1000)
        system("cls")
    except KeyboardInterrupt:
      self.detach()
      print("\nExiting...")
      exit(1)
