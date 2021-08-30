# import dont le root de l'import est le root du projet
from packA.packA import packA
from src.srcA.srcA import srcA

def main():
# Can be run using
# python3 -m src.main

# cannot be run using
# python3 src/main.py
    print(packA())
    print(srcA())

main()