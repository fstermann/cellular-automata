from cellular_automata import CellularAutomata

# Create new cellular automata with rule 30
ca = CellularAutomata(30, 500, 255)
ca.create()

# Save it
ca.save()
