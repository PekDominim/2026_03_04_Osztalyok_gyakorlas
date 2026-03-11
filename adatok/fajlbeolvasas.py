autok = []
with open("autok/lista.txt", "r", encoding="utf-8") as f:
    next(f)
    for sor in f:
        adatok = sor.strip().slpit(",")
        if len(adatok) >= 4:
            marka, típus
