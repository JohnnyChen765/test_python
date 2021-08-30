from random import randint, shuffle

Proposition = bool


class Ange:
    nature: str

    def __init__(self) -> None:
        pass

    def call(self, p: Proposition) -> bool:
        pass


class Verite(Ange):
    def __init__(self) -> None:
        super().__init__()
        self.nature = "V"

    def call(self, p: Proposition) -> bool:
        return p


class Menteur(Ange):
    def __init__(self) -> None:
        super().__init__()
        self.nature = "M"

    def call(self, p: Proposition) -> bool:
        return not p


class Random(Ange):
    def __init__(self) -> None:
        super().__init__()
        self.nature = "R"

    def call(self, p: Proposition) -> bool:
        return bool(randint(0, 1))


class Jeu:
    A: Ange
    B: Ange
    C: Ange

    counter: int = 0

    def __init__(self) -> None:
        players = [Verite(), Menteur(), Random()]
        shuffle(players)
        self.A, self.B, self.C = players

    def propose(self, p: )
