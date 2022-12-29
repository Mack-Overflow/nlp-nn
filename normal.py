import unicodedata

c_cedilla = "\u0043\u0327"
print(c_cedilla)

# Canonical decomposition followed by canonical comp
n = unicodedata.normalize('NFC', c_cedilla)
print(n)

# Normal form for compatibility
fancy_h_cidilla = "\u210B\u0327"
h_cidilla = "\u1e28"
print(fancy_h_cidilla == h_cidilla)
print(unicodedata.normalize('NFKC', fancy_h_cidilla) == h_cidilla)