from typing import List
from pymem import Pymem

# Thanks to vsantiago113 for inspire this function - https://bit.ly/3qAUc31
def get_pointer(pm: Pymem, base_address: hex, offsets: List[hex] = ()) -> int:
  """
  Get a pointer to a memory address.

  :param pm: Pymem instance.
  :param base_address: Base address.
  :param offsets: Offsets to the address.
  :return: Pointer to the address.
  """
  _base_address = pm.read_int(base_address)
  if offsets:
    for offset in offsets:
      if offset != offsets[-1]:
        _base_address = pm.read_int(_base_address + offset)
      else:
        _base_address = _base_address + offset
  return _base_address