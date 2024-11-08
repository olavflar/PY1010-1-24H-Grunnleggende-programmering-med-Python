""" Den første obligatoriske innlevering i PY1010 """

# Antall kjørte kilometer per år
km_per_år = 10000  

""" Kostnader for begge biler"""
trafikkforsikringsavgift_per_dag = 8.38
trafikkforsikringsavgift_år = 8.38 * 365

""" Kostnader for elbil """
forsikring_elbil = 5000
elbil_drivstoffbruk_kwh_per_km = 0.2
strompris_per_kwh = 2.0
elbil_bomavgift = km_per_år * 0.1
elbil_drivstoffkostnad = km_per_år * elbil_drivstoffbruk_kwh_per_km * strompris_per_kwh

# Elbil totalkostnad
elbil_totalkostnad = forsikring_elbil + trafikkforsikringsavgift_år + elbil_drivstoffkostnad + elbil_bomavgift

""" Her er en oversikt over kostnader som kun gjelder for bensinbil  """
forsikring_bensinbil = 7500
bensinbil_drivstoffkostnad_per_km = 1.0
bensinbil_drivstoffkostnad = km_per_år * bensinbil_drivstoffkostnad_per_km
bensinbil_bomavgift = km_per_år * 0.3

# Bensinbil totalkostnad
bensinbil_totalkostnad = forsikring_bensinbil + trafikkforsikringsavgift_år + bensinbil_drivstoffkostnad + bensinbil_bomavgift

# Kostnadsdifferanse
kostnadsdifferanse = bensinbil_totalkostnad - elbil_totalkostnad

# Utskrift av resultatene
print("Årlige totalkostnader:")
print(f"Elbil: {elbil_totalkostnad:.2f} kr")
print(f"Bensinbil: {bensinbil_totalkostnad:.2f} kr")
print(f"Kostnadsdifferanse (bensinbil - elbil): {kostnadsdifferanse:.2f} kr")