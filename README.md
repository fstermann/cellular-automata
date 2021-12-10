# cellular_automata
Basic Cellular Automata.

## Setup
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt


## Example
    from cellular_automata import CellularAutomata

    # Create new cellular automata with rule 30
    ca = CellularAutomata(30, 500, 255)
    ca.create()

    # Save it 
    ca.save()
