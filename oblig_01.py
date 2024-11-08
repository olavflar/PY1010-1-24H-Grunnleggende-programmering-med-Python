# In
km_per_år = 10000  # Antall kjørte kilometer per år (du kan endre denne verdien)

# Kostnader
forsikring_elbil = 5000
forsikring_bensinbil = 7500
trafikkforsikringsavgift_per_dag = 8.38
antall_dager_per_år = 365
trafikkforsikringsavgift_aar = trafikkforsikringsavgift_per_dag * antall_dager_per_år

# Elbil kostnader
elbil_drivstoffbruk_kwh_per_km = 0.2
strompris_per_kwh = 2.0
elbil_drivstoffkostnad = km_per_år * elbil_drivstoffbruk_kwh_per_km * strompris_per_kwh
elbil_bomavgift = km_per_år * 0.1
elbil_totalkostnad = forsikring_elbil + trafikkforsikringsavgift_aar + elbil_drivstoffkostnad + elbil_bomavgift

# Bensinbil kostnader
bensinbil_drivstoffkostnad_per_km = 1.0
bensinbil_drivstoffkostnad = km_per_år * bensinbil_drivstoffkostnad_per_km
bensinbil_bomavgift = km_per_år * 0.3
bensinbil_totalkostnad = forsikring_bensinbil + trafikkforsikringsavgift_aar + bensinbil_drivstoffkostnad + bensinbil_bomavgift

# Kostnadsdifferanse
kostnadsdifferanse = bensinbil_totalkostnad - elbil_totalkostnad

# Utskrift av resultatene
print("Årlige totalkostnader:")
print(f"Elbil: {elbil_totalkostnad:.2f} kr")
print(f"Bensinbil: {bensinbil_totalkostnad:.2f} kr")
print(f"Kostnadsdifferanse (bensinbil - elbil): {kostnadsdifferanse:.2f} kr")