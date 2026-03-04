from auto import Auto
import random
import statistics

auto1 = Auto("Toyota", "Corolla", 2015)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Audi", "E-tron", 2021)
auto4 = Auto("Ford", "Mustang", 2005)

print(auto1)
print(auto2)

auto1.gyorsit(300)
auto1.lassit(400)

autok = [auto1, auto2, auto3, auto4]
for auto in autok:
    print(auto)

print("\nGyorsit\n")
for auto in autok:
    auto.gyorsit(random.randint(30, 150))
    print(auto)

gyartasi_evek = [auto.gyartasi_ev for auto in autok]
kor = []
for year in gyartasi_evek:
    kor.append(2026 - int(year))
print(statistics.mean(kor))

for auto in autok:
    if auto.gyartasi_ev == min(gyartasi_evek):
        print(f"A legidösebb autó: {auto.marka} {auto.tipus} {2026-auto.gyartasi_ev}")
