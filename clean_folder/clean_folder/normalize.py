import re
from pathlib import Path



CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "u", "ja", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    
def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    s_name = Path(name).suffix
    t_name = t_name.removesuffix(s_name)

    t_name = re.sub(r'\W', '_', t_name)
    t_name = t_name + s_name
    return t_name





