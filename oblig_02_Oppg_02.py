# 2: Klassefest; Beregne antall pizzaer som må kjøpes
import math

antall_elever = int(input("Skriv inn antall elever: "))
pizza_per_elev = 1 / 4  # Hver elev spiser 1/4 pizza
total_pizza = antall_elever * pizza_per_elev

# Runde opp til nærmeste hele pizza
pizzaer_å_kjøpe = math.ceil(total_pizza)

print(f"Det må handles inn {pizzaer_å_kjøpe} pizzaer til festen.")
