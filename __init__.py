from os import system
from time import sleep
from ReadWriteMemory import ReadWriteMemory, Process
from offsets import offsets


class GameState:
  INGAME = "In game"
  INGAME_UNFOCUSED = "In game (unfocused)"
  MENU = "In menu"
  NOT_INGAME = "Not in game"
  UNKNOWN = "Unknown"

class DarkSoulsRemastered:
  refresh_time_in_ms: int = 100
  rwm = ReadWriteMemory()
  game_attached = False
  process: Process
  base: int

  game_state: str = ""
  time_played: int = 0
  souls: int = 0
  estus: int = 0
  humanities: int = 0
  level: int = 0
  deaths: int = 0
  equip_load: int = 0
  max_equip_load: int = 0
  equip_load_percentage: float = 0.0
  next_level_req_souls: int = 0
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

  def __init__(self):
    self.attach()

  def attach(self):
    """
    Attach to the game
    """
    if not self.game_attached:
      try:
        self.process = self.rwm.get_process_by_name("DarkSoulsRemastered.exe")
        self.process.open()
        self.base = self.process.get_modules()[0]
        self.game_attached = True
      except Exception as e:
        self.game_attached = False

  def detach(self):
    """
    Detach from the game
    """
    if self.game_attached:
      self.process.close()
      self.game_attached = False

  def convert_time(self, time_in_ms: int) -> tuple[int, int, int, int]:
    """
    Convert time in milliseconds to hours, minutes, seconds, milliseconds

    :param time_in_ms: time in milliseconds
    :return: tuple of hours, minutes, seconds, milliseconds
    """
    time_in_seconds: int = time_in_ms / 1000
    hours: int = int(time_in_seconds / 3600)
    minutes: int = int((time_in_seconds - (hours * 3600)) / 60)
    seconds: int = int(time_in_seconds - (hours * 3600) - (minutes * 60))
    milliseconds: int = time_in_ms
    return hours, minutes, seconds, milliseconds

  def gameState(self):
    """
    Get the current game state

    :return: current game state
    """
    is_ingame_pointer = self.process.get_pointer(
        self.base + offsets["is_ingame"][0], offsets["is_ingame"][1])
    is_ingame = self.process.read(is_ingame_pointer)
    is_game_focused_pointer = self.process.get_pointer(
        self.base + offsets["is_game_focused"][0], offsets["is_game_focused"][1])
    is_game_focused = self.process.read(is_game_focused_pointer)
    if is_ingame == 1 and is_game_focused == 1:
      return GameState.INGAME
    elif is_ingame == 1 and is_game_focused == 0:
      return GameState.INGAME_UNFOCUSED
    elif is_ingame == 0:
      return GameState.NOT_INGAME
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
    time_played_pointer = self.process.get_pointer(
        self.base + offsets["time_played"][0], offsets["time_played"][1])
    time_played = self.process.read(time_played_pointer)
    return self.convert_time(time_played)

  def get_souls(self) -> int:
    """
    Get the current amount of souls
    """
    souls_pointer = self.process.get_pointer(
        self.base + offsets["souls"][0], offsets["souls"][1])
    souls = self.process.read(souls_pointer)
    return souls

  def add_souls(self, souls: int) -> bool:
    """
    Add souls to the current amount of souls

    :param souls: amount of souls to add
    :return: True if successful, False if not
    """
    souls_pointer = self.process.get_pointer(
        self.base + offsets["souls"][0], offsets["souls"][1])
    _souls = self.process.read(souls_pointer)
    _souls += souls
    return self.process.write(souls_pointer, _souls)

  def set_souls(self, souls: int) -> bool:
    """
    Set the current amount of souls

    :param souls: amount of souls to set
    :return: True if successful, False if not
    """
    souls_pointer = self.process.get_pointer(
        self.base + offsets["souls"][0], offsets["souls"][1])
    return self.process.write(souls_pointer, souls)

  def get_estus(self) -> int:
    """
    Get the current amount of estus
    """
    estus_pointer = self.process.get_pointer(
        self.base + offsets["estus"][0], offsets["estus"][1])
    estus = self.process.read(estus_pointer)
    return estus

  def add_estus(self, estus: int) -> bool:
    """
    Add estus to the current amount of estus

    :param estus: amount of estus to add
    :return: True if successful, False if not
    """
    estus_pointer = self.process.get_pointer(
        self.base + offsets["estus"][0], offsets["estus"][1])
    _estus = self.process.read(estus_pointer)
    _estus += estus
    return self.process.write(estus_pointer, _estus)

  def set_estus(self, estus: int) -> bool:
    """
    Set the current amount of estus

    :param estus: amount of estus to set
    :return: True if successful, False if not
    """
    estus_pointer = self.process.get_pointer(
        self.base + offsets["estus"][0], offsets["estus"][1])
    return self.process.write(estus_pointer, estus)

  def get_humanities(self) -> int:
    """
    Get the current amount of humanities
    """
    humanities_pointer = self.process.get_pointer(
        self.base + offsets["humanities"][0], offsets["humanities"][1])
    humanities = self.process.read(humanities_pointer)
    return humanities

  def add_humanities(self, humanities: int) -> bool:
    """
    Add humanities to the current amount of humanities

    :param humanities: amount of humanities to add
    :return: True if successful, False if not
    """
    humanities_pointer = self.process.get_pointer(
        self.base + offsets["humanities"][0], offsets["humanities"][1])
    _humanities = self.process.read(humanities_pointer)
    _humanities += humanities
    return self.process.write(humanities_pointer, _humanities)

  def set_humanities(self, humanities: int) -> bool:
    """
    Set the current amount of humanities

    :param humanities: amount of humanities to set
    :return: True if successful, False if not
    """
    humanities_pointer = self.process.get_pointer(
        self.base + offsets["humanities"][0], offsets["humanities"][1])
    return self.process.write(humanities_pointer, humanities)

  def get_level(self) -> int:
    """
    Get the current level
    """
    level_pointer = self.process.get_pointer(
        self.base + offsets["level"][0], offsets["level"][1])
    level = self.process.read(level_pointer)
    return level

  def add_level(self, level: int) -> bool:
    """
    Add level to the current level

    :param level: amount of level to add
    :return: True if successful, False if not
    """
    level_pointer = self.process.get_pointer(
        self.base + offsets["level"][0], offsets["level"][1])
    _level = self.process.read(level_pointer)
    _level += level
    return self.process.write(level_pointer, _level)

  def set_level(self, level: int) -> bool:
    """
    Set the current level

    :param level: amount of level to set
    :return: True if successful, False if not
    """
    level_pointer = self.process.get_pointer(
        self.base + offsets["level"][0], offsets["level"][1])
    return self.process.write(level_pointer, level)

  def get_deaths(self) -> int:
    """
    Get the current amount of deaths
    """
    deaths_pointer = self.process.get_pointer(
        self.base + offsets["deaths"][0], offsets["deaths"][1])
    deaths = self.process.read(deaths_pointer)
    return deaths

  def add_deaths(self, deaths: int) -> bool:
    """
    Add deaths to the current amount of deaths

    :param deaths: amount of deaths to add
    :return: True if successful, False if not
    """
    deaths_pointer = self.process.get_pointer(
        self.base + offsets["deaths"][0], offsets["deaths"][1])
    _deaths = self.process.read(deaths_pointer)
    _deaths += deaths
    return self.process.write(deaths_pointer, _deaths)

  def set_deaths(self, deaths: int) -> bool:
    """
    Set the current amount of deaths

    :param deaths: amount of deaths to set
    :return: True if successful, False if not
    """
    deaths_pointer = self.process.get_pointer(
        self.base + offsets["deaths"][0], offsets["deaths"][1])
    return self.process.write(deaths_pointer, deaths)

  def get_equip_load(self) -> int:
    """
    Get the current equip load
    """
    equip_load_pointer = self.process.get_pointer(
        self.base + offsets["equip_load"][0], offsets["equip_load"][1])
    equip_load = self.process.read(equip_load_pointer)
    return equip_load

  def get_max_equip_load(self) -> int:
    """
    Get the max equip load
    """
    max_equip_load_pointer = self.process.get_pointer(
        self.base + offsets["max_equip_load"][0], offsets["max_equip_load"][1])
    max_equip_load = self.process.read(max_equip_load_pointer)
    return max_equip_load

  #TODO: Search new offsets
  def get_equip_load_percentage(self) -> float:
    """
    Get the equip load percentage
    """
    equip_load = self.get_equip_load()
    max_equip_load = self.get_max_equip_load()
    return equip_load / max_equip_load

  def get_next_level_req_souls(self) -> int:
    """
    Get the next level req souls
    """
    next_level_req_souls_pointer = self.process.get_pointer(
        self.base + offsets["next_level_req_souls"][0], offsets["next_level_req_souls"][1])
    next_level_req_souls = self.process.read(next_level_req_souls_pointer)
    return next_level_req_souls

  def get_vitality(self) -> int:
    """
    Get the current vitality
    """
    vitality_pointer = self.process.get_pointer(
        self.base + offsets["vitality"][0], offsets["vitality"][1])
    vitality = self.process.read(vitality_pointer)
    return vitality

  def add_vitality(self, vitality: int) -> bool:
    """
    Add vitality to the current vitality

    :param vitality: amount of vitality to add
    :return: True if successful, False if not
    """
    vitality_pointer = self.process.get_pointer(
        self.base + offsets["vitality"][0], offsets["vitality"][1])
    _vitality = self.process.read(vitality_pointer)
    _vitality += vitality
    return self.process.write(vitality_pointer, _vitality)

  def set_vitality(self, vitality: int) -> bool:
    """
    Set the current vitality

    :param vitality: amount of vitality to set
    :return: True if successful, False if not
    """
    vitality_pointer = self.process.get_pointer(
        self.base + offsets["vitality"][0], offsets["vitality"][1])
    return self.process.write(vitality_pointer, vitality)

  def get_attunement(self) -> int:
    """
    Get the current attunement
    """
    attunement_pointer = self.process.get_pointer(
        self.base + offsets["attunement"][0], offsets["attunement"][1])
    attunement = self.process.read(attunement_pointer)
    return attunement

  def add_attunement(self, attunement: int) -> bool:
    """
    Add attunement to the current attunement

    :param attunement: amount of attunement to add
    :return: True if successful, False if not
    """
    attunement_pointer = self.process.get_pointer(
        self.base + offsets["attunement"][0], offsets["attunement"][1])
    _attunement = self.process.read(attunement_pointer)
    _attunement += attunement
    return self.process.write(attunement_pointer, _attunement)

  def set_attunement(self, attunement: int) -> bool:
    """
    Set the current attunement

    :param attunement: amount of attunement to set
    :return: True if successful, False if not
    """
    attunement_pointer = self.process.get_pointer(
        self.base + offsets["attunement"][0], offsets["attunement"][1])
    return self.process.write(attunement_pointer, attunement)

  def get_endurance(self) -> int:
    """
    Get the current endurance
    """
    endurance_pointer = self.process.get_pointer(
        self.base + offsets["endurance"][0], offsets["endurance"][1])
    endurance = self.process.read(endurance_pointer)
    return endurance

  def add_endurance(self, endurance: int) -> bool:
    """
    Add endurance to the current endurance

    :param endurance: amount of endurance to add
    :return: True if successful, False if not
    """
    endurance_pointer = self.process.get_pointer(
        self.base + offsets["endurance"][0], offsets["endurance"][1])
    _endurance = self.process.read(endurance_pointer)
    _endurance += endurance
    return self.process.write(endurance_pointer, _endurance)

  def set_endurance(self, endurance: int) -> bool:
    """
    Set the current endurance

    :param endurance: amount of endurance to set
    :return: True if successful, False if not
    """
    endurance_pointer = self.process.get_pointer(
        self.base + offsets["endurance"][0], offsets["endurance"][1])
    return self.process.write(endurance_pointer, endurance)

  def get_strength(self) -> int:
    """
    Get the current strength
    """
    strength_pointer = self.process.get_pointer(
        self.base + offsets["strength"][0], offsets["strength"][1])
    strength = self.process.read(strength_pointer)
    return strength

  def add_strength(self, strength: int) -> bool:
    """
    Add strength to the current strength

    :param strength: amount of strength to add
    :return: True if successful, False if not
    """
    strength_pointer = self.process.get_pointer(
        self.base + offsets["strength"][0], offsets["strength"][1])
    _strength = self.process.read(strength_pointer)
    _strength += strength
    return self.process.write(strength_pointer, _strength)

  def set_strength(self, strength: int) -> bool:
    """
    Set the current strength

    :param strength: amount of strength to set
    :return: True if successful, False if not
    """
    strength_pointer = self.process.get_pointer(
        self.base + offsets["strength"][0], offsets["strength"][1])
    return self.process.write(strength_pointer, strength)

  def get_dexterity(self) -> int:
    """
    Get the current dexterity
    """
    dexterity_pointer = self.process.get_pointer(
        self.base + offsets["dexterity"][0], offsets["dexterity"][1])
    dexterity = self.process.read(dexterity_pointer)
    return dexterity

  def add_dexterity(self, dexterity: int) -> bool:
    """
    Add dexterity to the current dexterity

    :param dexterity: amount of dexterity to add
    :return: True if successful, False if not
    """
    dexterity_pointer = self.process.get_pointer(
        self.base + offsets["dexterity"][0], offsets["dexterity"][1])
    _dexterity = self.process.read(dexterity_pointer)
    _dexterity += dexterity
    return self.process.write(dexterity_pointer, _dexterity)

  def set_dexterity(self, dexterity: int) -> bool:
    """
    Set the current dexterity

    :param dexterity: amount of dexterity to set
    :return: True if successful, False if not
    """
    dexterity_pointer = self.process.get_pointer(
        self.base + offsets["dexterity"][0], offsets["dexterity"][1])
    return self.process.write(dexterity_pointer, dexterity)

  def get_resistance(self) -> int:
    """
    Get the current resistance
    """
    resistance_pointer = self.process.get_pointer(
        self.base + offsets["resistance"][0], offsets["resistance"][1])
    resistance = self.process.read(resistance_pointer)
    return resistance

  def add_resistance(self, resistance: int) -> bool:
    """
    Add resistance to the current resistance

    :param resistance: amount of resistance to add
    :return: True if successful, False if not
    """
    resistance_pointer = self.process.get_pointer(
        self.base + offsets["resistance"][0], offsets["resistance"][1])
    _resistance = self.process.read(resistance_pointer)
    _resistance += resistance
    return self.process.write(resistance_pointer, _resistance)

  def set_resistance(self, resistance: int) -> bool:
    """
    Set the current resistance

    :param resistance: amount of resistance to set
    :return: True if successful, False if not
    """
    resistance_pointer = self.process.get_pointer(
        self.base + offsets["resistance"][0], offsets["resistance"][1])
    return self.process.write(resistance_pointer, resistance)

  def get_intelligence(self) -> int:
    """
    Get the current intelligence
    """
    intelligence_pointer = self.process.get_pointer(
        self.base + offsets["intelligence"][0], offsets["intelligence"][1])
    intelligence = self.process.read(intelligence_pointer)
    return intelligence

  def add_intelligence(self, intelligence: int) -> bool:
    """
    Add intelligence to the current intelligence

    :param intelligence: amount of intelligence to add
    :return: True if successful, False if not
    """
    intelligence_pointer = self.process.get_pointer(
        self.base + offsets["intelligence"][0], offsets["intelligence"][1])
    _intelligence = self.process.read(intelligence_pointer)
    _intelligence += intelligence
    return self.process.write(intelligence_pointer, _intelligence)

  def set_intelligence(self, intelligence: int) -> bool:
    """
    Set the current intelligence

    :param intelligence: amount of intelligence to set
    :return: True if successful, False if not
    """
    intelligence_pointer = self.process.get_pointer(
        self.base + offsets["intelligence"][0], offsets["intelligence"][1])
    return self.process.write(intelligence_pointer, intelligence)

  def get_faith(self) -> int:
    """
    Get the current faith
    """
    faith_pointer = self.process.get_pointer(
        self.base + offsets["faith"][0], offsets["faith"][1])
    faith = self.process.read(faith_pointer)
    return faith

  def add_faith(self, faith: int) -> bool:
    """
    Add faith to the current faith

    :param faith: amount of faith to add
    :return: True if successful, False if not
    """
    faith_pointer = self.process.get_pointer(
        self.base + offsets["faith"][0], offsets["faith"][1])
    _faith = self.process.read(faith_pointer)
    _faith += faith
    return self.process.write(faith_pointer, _faith)

  def set_faith(self, faith: int) -> bool:
    """
    Set the current faith

    :param faith: amount of faith to set
    :return: True if successful, False if not
    """
    faith_pointer = self.process.get_pointer(
        self.base + offsets["faith"][0], offsets["faith"][1])
    return self.process.write(faith_pointer, faith)

  def get_r_weapon_1(self) -> int:
    """
    Get the current right weapon 1
    """
    r_weapon_1_pointer = self.process.get_pointer(
        self.base + offsets["r_weapon_1"][0], offsets["r_weapon_1"][1])
    r_weapon_1 = self.process.read(r_weapon_1_pointer)
    return r_weapon_1

  def get_r_weapon_2(self) -> int:
    """
    Get the current right weapon 2
    """
    r_weapon_2_pointer = self.process.get_pointer(
        self.base + offsets["r_weapon_2"][0], offsets["r_weapon_2"][1])
    r_weapon_2 = self.process.read(r_weapon_2_pointer)
    return r_weapon_2

  def get_l_weapon_1(self) -> int:
    """
    Get the current left weapon 1
    """
    l_weapon_1_pointer = self.process.get_pointer(
        self.base + offsets["l_weapon_1"][0], offsets["l_weapon_1"][1])
    l_weapon_1 = self.process.read(l_weapon_1_pointer)
    return l_weapon_1

  def get_l_weapon_2(self) -> int:
    """
    Get the current left weapon 2
    """
    l_weapon_2_pointer = self.process.get_pointer(
        self.base + offsets["l_weapon_2"][0], offsets["l_weapon_2"][1])
    l_weapon_2 = self.process.read(l_weapon_2_pointer)
    return l_weapon_2
  # endregion

  def read_memory(self):
    """
    Read the memory
    """
    self.game_state = self.gameState()
    if self.game_state == GameState.INGAME or self.game_state == GameState.INGAME_UNFOCUSED:
      self.time_played = self.get_time_played()
      self.souls = self.get_souls()
      self.estus = self.get_estus()
      self.humanities = self.get_humanities()
      self.level = self.get_level()
      self.deaths = self.get_deaths()
      self.equip_load = self.get_equip_load()
      self.max_equip_load = self.get_max_equip_load()
      self.equip_load_percentage = self.get_equip_load_percentage() #TODO: Search for the correct offset
      self.next_level_req_souls = self.get_next_level_req_souls()
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

  def print_memory(self):
    print(f"--- Game Attached: {self.game_attached} ---")
    if self.game_attached:
      print(f"Game state: {self.game_state}")
      if self.game_state == GameState.INGAME or self.game_state == GameState.INGAME_UNFOCUSED:
        print(
            f"time_played: {self.time_played[3]}ms, {self.time_played[0]}h {self.time_played[1]}m {self.time_played[2]}s")
        print(f"Souls: {self.souls}")
        print(f"Estus: {self.estus}")
        print(f"Humanities: {self.humanities}")
        print(f"Level: {self.level}")
        print(f"Deaths: {self.deaths}")
        print(f"Equip Load: {self.equip_load}")
        print(f"Max Equip Load: {self.max_equip_load}")
        print(f"Equip Load Percentage: {self.equip_load_percentage}%") #TODO: Search for the correct offset
        print(f"Next Level Req Souls: {self.next_level_req_souls}")
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

  def start(self):
    self.attach()
    if self.game_attached:
      self.read_memory()
    self.print_memory()
    self.detach()

  def loop(self):
    """
    Start the main loop
    """
    try:
      while True:
        self.start()
        sleep(self.refresh_time_in_ms / 1000)
        system("cls")
    except KeyboardInterrupt:
      self.detach()
      print("\nExiting...")
      exit(1)



# DarkSoulsRemastered().add_level(-1)
DarkSoulsRemastered().loop()