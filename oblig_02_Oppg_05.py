# 5: Beregning av areal og omkrets
import math

def beregn_areal_og_omkrets(a, b):
    # Halvsirkelens radius
    r = a / 2

    # Arealet til halvsirkelen
    areal_halvsirkel = (math.pi * r**2) / 2

    # Arealet til trekanten
    areal_trekant = (a * b) / 2

    # Totalareal
    total_areal = areal_halvsirkel + areal_trekant

    # Omkrets: b + hypotenusen + halvsirkelens omkrets
    hypotenus = math.sqrt(a**2 + b**2)
    omkrets = b + hypotenus + math.pi * r

    return total_areal, omkrets

# Eksempel på bruk
a = 6  # Sett inn verdi for a
b = 8  # Sett inn verdi for b

areal, omkrets = beregn_areal_og_omkrets(a, b)
print(f"Arealet av figuren er: {areal:.2f}")
print(f"Den ytre omkretsen av figuren er: {omkrets:.2f}")
