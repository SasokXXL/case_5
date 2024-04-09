import random

teams = []
events = [
        {"name": "Война", "money": 0, "people": 0, "army": 0, "faith": 0},
        {"name": "Нашествие зверей", "money": 0, "people": 0, "army": 0, "faith": 0},
        {"name": "Чума", "money": 0, "people": 0, "army": 0, "faith": 0},
        {"name": "Вторжение пришельцев", "money": 0, "people": 0, "army": 0, "faith": 0},
        {"name": "Восстание нежити", "money": 0, "people": 0, "army": 0, "faith": 0},
]

war = [
        {"name": "Победа в войне", "money": 500, "people": 500, "army": -250, "faith": 500},
        {"name": "Поражение в войне", "money": -650, "people": -500, "army": -600, "faith": -400},
]

animals = [
        {"name": "Звери были побеждены. Да воцарится ваше королевство на их трупах.", "money": 500, "people": 500, "army": -250, "faith": 500},
        {"name": "Звери не были побеждены", "money": -650, "people": -500, "army": -600, "faith": -400},
]

plague = [
        {"name": "Успешно оказано сопротивление", "money": 500, "people": 500, "army": -250, "faith": 500},
        {"name": "Коронавирус разбушевался не на шутку", "money": -650, "people": -500, "army": -600, "faith": -400},
]

nlo = [
        {"name": "Победа над пришельцами", "money": 500, "people": 500, "army": -250, "faith": 500},
        {"name": "Порожение в войне с пришельцами", "money": -650, "people": -500, "army": -600, "faith": -400},
]

nekr = [
        {"name": "Легионы нежити пали", "money": 500, "people": 500, "army": -250, "faith": 500},
        {"name": "Легионы нежити не пали", "money": -650, "people": -500, "army": -600, "faith": -400},
]


revents = [
    {"name": "Урожайный год: Урожай оказывается изобильным, добавляя деньги к казне.",\
     "money": 1000, "people": 0, "army": 0, "faith": 0},
    {"name": "Бунт: Недовольство народа приводит к бунту, уменьшая количество народа и вызывая потери в ресурсах.",\
     "money": -500, "people": -300, "army": -200, "faith": -10},
    {"name": "Победа в битве: Победа в важной битве приводит к увеличению численности армии и улучшению её обученности.",\
     "money": -200, "people": 300, "army": 150, "faith": 0},
    {"name": "Торговое соглашение: Удачное соглашение с торговцами приводит к увеличению доходов.",\
     "money": 800, "people": 0, "army": 0, "faith": 0},
    {"name": "Праздник: Организация праздника поднимает настроение народа, увеличивая их численность.",\
     "money": -300, "people": 400, "army": 0, "faith": 100},
    {"name": "Восстание врагов: Армия врагов нападает, требуя усиления обороны и снижая численность армии.", \
     "money": -500, "people": 0, "army": -250, "faith": -200},
    {
        "name": "Религиозный митинг: Успешное проведение религиозного мероприятия повышает веру народа и усиливает влияние церкви.", \
        "money": 0, "people": 250, "army": 0, "faith": 200},
    {"name": "Раскол: Раскол в церкви приводит к потере веры народа и снижению влияния церкви.", "money": 0,
     "people": 0, "army": 0, "faith": -300},
]

team1 = input('Введите название команды 1:')
team2 = input('Введите название команды 2:')
team3 = input('Введите название команды 3:')
teams.append(team1)
teams.append(team2)
teams.append(team3)
# деньги, люди, армия, вера
resources1 = {"money": 1000, "people": 1000, "army": 1000, "faith": 1000}
resources2 = {"money": 1000, "people": 1000, "army": 1000, "faith": 1000}
resources3 = {"money": 1000, "people": 1000, "army": 1000, "faith": 1000}


print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")


print("Сквозь века и целых 3 хода случилось огромное событие")
eventss = int(input('3 королевства собрались и после бурных дискуссий выбрали(выберите число от 1 до 5):'))
event = events[eventss - 1]
print(f"Событие: {event['name']}")
if eventss == 1:
    rand_input = int(input('Введите число от 1 до 2'))
    war_random = random.choice(war)
    print(f"Событие: {war_random['name']}")
    resources1["money"] += war_random["money"]
    resources1["people"] += war_random["people"]
    resources1["army"] += war_random["army"]
    resources1["faith"] += war_random["faith"]
    resources2["money"] += war_random["money"]
    resources2["people"] += war_random["people"]
    resources2["army"] += war_random["army"]
    resources2["faith"] += war_random["faith"]
    resources3["money"] += war_random["money"]
    resources3["people"] += war_random["people"]
    resources3["army"] += war_random["army"]
    resources3["faith"] += war_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 2:
    rand_input = int(input('Введите число от 1 до 2'))
    animals_random = random.choice(animals)
    print(f"Событие: {animals_random['name']}")
    resources1["money"] += animals_random["money"]
    resources1["people"] += animals_random["people"]
    resources1["army"] += animals_random["army"]
    resources1["faith"] += animals_random["faith"]
    resources2["money"] += animals_random["money"]
    resources2["people"] += animals_random["people"]
    resources2["army"] += animals_random["army"]
    resources2["faith"] += animals_random["faith"]
    resources3["money"] += animals_random["money"]
    resources3["people"] += animals_random["people"]
    resources3["army"] += animals_random["army"]
    resources3["faith"] += animals_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 3:
    rand_input = int(input('Введите число от 1 до 2'))
    plague_random = random.choice(plague)
    print(f"Событие: {plague_random['name']}")
    resources1["money"] += plague_random["money"]
    resources1["people"] += plague_random["people"]
    resources1["army"] += plague_random["army"]
    resources1["faith"] += plague_random["faith"]
    resources2["money"] += plague_random["money"]
    resources2["people"] += plague_random["people"]
    resources2["army"] += plague_random["army"]
    resources2["faith"] += plague_random["faith"]
    resources3["money"] += plague_random["money"]
    resources3["people"] += plague_random["people"]
    resources3["army"] += plague_random["army"]
    resources3["faith"] += plague_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 4:
    rand_input = int(input('Введите число от 1 до 2'))
    nlo_random = random.choice(nlo)
    print(f"Событие: {nlo_random['name']}")
    resources1["money"] += nlo_random["money"]
    resources1["people"] += nlo_random["people"]
    resources1["army"] += nlo_random["army"]
    resources1["faith"] += nlo_random["faith"]
    resources2["money"] += nlo_random["money"]
    resources2["people"] += nlo_random["people"]
    resources2["army"] += nlo_random["army"]
    resources2["faith"] += nlo_random["faith"]
    resources3["money"] += nlo_random["money"]
    resources3["people"] += nlo_random["people"]
    resources3["army"] += nlo_random["army"]
    resources3["faith"] += nlo_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 5:
    rand_input = int(input('Введите число от 1 до 2'))
    nekr_random = random.choice(nekr)
    print(f"Событие: {nekr_random['name']}")
    resources1["money"] += nekr_random["money"]
    resources1["people"] += nekr_random["people"]
    resources1["army"] += nekr_random["army"]
    resources1["faith"] += nekr_random["faith"]
    resources2["money"] += nekr_random["money"]
    resources2["people"] += nekr_random["people"]
    resources2["army"] += nekr_random["army"]
    resources2["faith"] += nekr_random["faith"]
    resources3["money"] += nekr_random["money"]
    resources3["people"] += nekr_random["people"]
    resources3["army"] += nekr_random["army"]
    resources3["faith"] += nekr_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')


print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")


print("Сквозь века и целых 3 хода случилось огромное событие")
eventss = int(input('3 королевства собрались и после бурных дискуссий выбрали(выберите число от 1 до 5):'))
event = events[eventss - 1]
print(f"Событие: {event['name']}")
if eventss == 1:
    rand_input = int(input('Введите число от 1 до 2'))
    war_random = random.choice(war)
    print(f"Событие: {war_random['name']}")
    resources1["money"] += war_random["money"]
    resources1["people"] += war_random["people"]
    resources1["army"] += war_random["army"]
    resources1["faith"] += war_random["faith"]
    resources2["money"] += war_random["money"]
    resources2["people"] += war_random["people"]
    resources2["army"] += war_random["army"]
    resources2["faith"] += war_random["faith"]
    resources3["money"] += war_random["money"]
    resources3["people"] += war_random["people"]
    resources3["army"] += war_random["army"]
    resources3["faith"] += war_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 2:
    rand_input = int(input('Введите число от 1 до 2'))
    animals_random = random.choice(animals)
    print(f"Событие: {animals_random['name']}")
    resources1["money"] += animals_random["money"]
    resources1["people"] += animals_random["people"]
    resources1["army"] += animals_random["army"]
    resources1["faith"] += animals_random["faith"]
    resources2["money"] += animals_random["money"]
    resources2["people"] += animals_random["people"]
    resources2["army"] += animals_random["army"]
    resources2["faith"] += animals_random["faith"]
    resources3["money"] += animals_random["money"]
    resources3["people"] += animals_random["people"]
    resources3["army"] += animals_random["army"]
    resources3["faith"] += animals_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 3:
    rand_input = int(input('Введите число от 1 до 2'))
    plague_random = random.choice(plague)
    print(f"Событие: {plague_random['name']}")
    resources1["money"] += plague_random["money"]
    resources1["people"] += plague_random["people"]
    resources1["army"] += plague_random["army"]
    resources1["faith"] += plague_random["faith"]
    resources2["money"] += plague_random["money"]
    resources2["people"] += plague_random["people"]
    resources2["army"] += plague_random["army"]
    resources2["faith"] += plague_random["faith"]
    resources3["money"] += plague_random["money"]
    resources3["people"] += plague_random["people"]
    resources3["army"] += plague_random["army"]
    resources3["faith"] += plague_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 4:
    rand_input = int(input('Введите число от 1 до 2'))
    nlo_random = random.choice(nlo)
    print(f"Событие: {nlo_random['name']}")
    resources1["money"] += nlo_random["money"]
    resources1["people"] += nlo_random["people"]
    resources1["army"] += nlo_random["army"]
    resources1["faith"] += nlo_random["faith"]
    resources2["money"] += nlo_random["money"]
    resources2["people"] += nlo_random["people"]
    resources2["army"] += nlo_random["army"]
    resources2["faith"] += nlo_random["faith"]
    resources3["money"] += nlo_random["money"]
    resources3["people"] += nlo_random["people"]
    resources3["army"] += nlo_random["army"]
    resources3["faith"] += nlo_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 5:
    rand_input = int(input('Введите число от 1 до 2'))
    nekr_random = random.choice(nekr)
    print(f"Событие: {nekr_random['name']}")
    resources1["money"] += nekr_random["money"]
    resources1["people"] += nekr_random["people"]
    resources1["army"] += nekr_random["army"]
    resources1["faith"] += nekr_random["faith"]
    resources2["money"] += nekr_random["money"]
    resources2["people"] += nekr_random["people"]
    resources2["army"] += nekr_random["army"]
    resources2["faith"] += nekr_random["faith"]
    resources3["money"] += nekr_random["money"]
    resources3["people"] += nekr_random["people"]
    resources3["army"] += nekr_random["army"]
    resources3["faith"] += nekr_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')


print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")


print("Сквозь века и целых 3 хода случилось огромное событие")
eventss = int(input('3 королевства собрались и после бурных дискуссий выбрали(выберите число от 1 до 5):'))
event = events[eventss - 1]
print(f"Событие: {event['name']}")
if eventss == 1:
    rand_input = int(input('Введите число от 1 до 2'))
    war_random = random.choice(war)
    print(f"Событие: {war_random['name']}")
    resources1["money"] += war_random["money"]
    resources1["people"] += war_random["people"]
    resources1["army"] += war_random["army"]
    resources1["faith"] += war_random["faith"]
    resources2["money"] += war_random["money"]
    resources2["people"] += war_random["people"]
    resources2["army"] += war_random["army"]
    resources2["faith"] += war_random["faith"]
    resources3["money"] += war_random["money"]
    resources3["people"] += war_random["people"]
    resources3["army"] += war_random["army"]
    resources3["faith"] += war_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 2:
    rand_input = int(input('Введите число от 1 до 2'))
    animals_random = random.choice(animals)
    print(f"Событие: {animals_random['name']}")
    resources1["money"] += animals_random["money"]
    resources1["people"] += animals_random["people"]
    resources1["army"] += animals_random["army"]
    resources1["faith"] += animals_random["faith"]
    resources2["money"] += animals_random["money"]
    resources2["people"] += animals_random["people"]
    resources2["army"] += animals_random["army"]
    resources2["faith"] += animals_random["faith"]
    resources3["money"] += animals_random["money"]
    resources3["people"] += animals_random["people"]
    resources3["army"] += animals_random["army"]
    resources3["faith"] += animals_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 3:
    rand_input = int(input('Введите число от 1 до 2'))
    plague_random = random.choice(plague)
    print(f"Событие: {plague_random['name']}")
    resources1["money"] += plague_random["money"]
    resources1["people"] += plague_random["people"]
    resources1["army"] += plague_random["army"]
    resources1["faith"] += plague_random["faith"]
    resources2["money"] += plague_random["money"]
    resources2["people"] += plague_random["people"]
    resources2["army"] += plague_random["army"]
    resources2["faith"] += plague_random["faith"]
    resources3["money"] += plague_random["money"]
    resources3["people"] += plague_random["people"]
    resources3["army"] += plague_random["army"]
    resources3["faith"] += plague_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 4:
    rand_input = int(input('Введите число от 1 до 2'))
    nlo_random = random.choice(nlo)
    print(f"Событие: {nlo_random['name']}")
    resources1["money"] += nlo_random["money"]
    resources1["people"] += nlo_random["people"]
    resources1["army"] += nlo_random["army"]
    resources1["faith"] += nlo_random["faith"]
    resources2["money"] += nlo_random["money"]
    resources2["people"] += nlo_random["people"]
    resources2["army"] += nlo_random["army"]
    resources2["faith"] += nlo_random["faith"]
    resources3["money"] += nlo_random["money"]
    resources3["people"] += nlo_random["people"]
    resources3["army"] += nlo_random["army"]
    resources3["faith"] += nlo_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 5:
    rand_input = int(input('Введите число от 1 до 2'))
    nekr_random = random.choice(nekr)
    print(f"Событие: {nekr_random['name']}")
    resources1["money"] += nekr_random["money"]
    resources1["people"] += nekr_random["people"]
    resources1["army"] += nekr_random["army"]
    resources1["faith"] += nekr_random["faith"]
    resources2["money"] += nekr_random["money"]
    resources2["people"] += nekr_random["people"]
    resources2["army"] += nekr_random["army"]
    resources2["faith"] += nekr_random["faith"]
    resources3["money"] += nekr_random["money"]
    resources3["people"] += nekr_random["people"]
    resources3["army"] += nekr_random["army"]
    resources3["faith"] += nekr_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')


print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")



print(f"Ход {team1} команды")
print(f"Ресурсы команды:{resources1}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources1["money"] += revent["money"]
resources1["people"] += revent["people"]
resources1["army"] += revent["army"]
resources1["faith"] += revent["faith"]
print(resources1)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team2} команды")
print(f"Ресурсы команды:{resources2}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources2["money"] += revent["money"]
resources2["people"] += revent["people"]
resources2["army"] += revent["army"]
resources2["faith"] += revent["faith"]
print(resources2)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")
print(f"Ход {team3} команды")
print(f"Ресурсы команды:{resources3}")
turn = int(input("Введите число от 1 до 20:"))
revent = random.choice(revents)
print(f"Событие: {revent['name']}")
resources3["money"] += revent["money"]
resources3["people"] += revent["people"]
resources3["army"] += revent["army"]
resources3["faith"] += revent["faith"]
print(resources3)
end = input("Ход завершен. Для продолжения нажмите ENTER")
print("-------------------------------------------------------------")


print("Сквозь века и целых 3 хода случилось огромное событие")
eventss = int(input('3 королевства собрались и после бурных дискуссий выбрали(выберите число от 1 до 5):'))
event = events[eventss - 1]
print(f"Событие: {event['name']}")
if eventss == 1:
    rand_input = int(input('Введите число от 1 до 2'))
    war_random = random.choice(war)
    print(f"Событие: {war_random['name']}")
    resources1["money"] += war_random["money"]
    resources1["people"] += war_random["people"]
    resources1["army"] += war_random["army"]
    resources1["faith"] += war_random["faith"]
    resources2["money"] += war_random["money"]
    resources2["people"] += war_random["people"]
    resources2["army"] += war_random["army"]
    resources2["faith"] += war_random["faith"]
    resources3["money"] += war_random["money"]
    resources3["people"] += war_random["people"]
    resources3["army"] += war_random["army"]
    resources3["faith"] += war_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 2:
    rand_input = int(input('Введите число от 1 до 2'))
    animals_random = random.choice(animals)
    print(f"Событие: {animals_random['name']}")
    resources1["money"] += animals_random["money"]
    resources1["people"] += animals_random["people"]
    resources1["army"] += animals_random["army"]
    resources1["faith"] += animals_random["faith"]
    resources2["money"] += animals_random["money"]
    resources2["people"] += animals_random["people"]
    resources2["army"] += animals_random["army"]
    resources2["faith"] += animals_random["faith"]
    resources3["money"] += animals_random["money"]
    resources3["people"] += animals_random["people"]
    resources3["army"] += animals_random["army"]
    resources3["faith"] += animals_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 3:
    rand_input = int(input('Введите число от 1 до 2'))
    plague_random = random.choice(plague)
    print(f"Событие: {plague_random['name']}")
    resources1["money"] += plague_random["money"]
    resources1["people"] += plague_random["people"]
    resources1["army"] += plague_random["army"]
    resources1["faith"] += plague_random["faith"]
    resources2["money"] += plague_random["money"]
    resources2["people"] += plague_random["people"]
    resources2["army"] += plague_random["army"]
    resources2["faith"] += plague_random["faith"]
    resources3["money"] += plague_random["money"]
    resources3["people"] += plague_random["people"]
    resources3["army"] += plague_random["army"]
    resources3["faith"] += plague_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 4:
    rand_input = int(input('Введите число от 1 до 2'))
    nlo_random = random.choice(nlo)
    print(f"Событие: {nlo_random['name']}")
    resources1["money"] += nlo_random["money"]
    resources1["people"] += nlo_random["people"]
    resources1["army"] += nlo_random["army"]
    resources1["faith"] += nlo_random["faith"]
    resources2["money"] += nlo_random["money"]
    resources2["people"] += nlo_random["people"]
    resources2["army"] += nlo_random["army"]
    resources2["faith"] += nlo_random["faith"]
    resources3["money"] += nlo_random["money"]
    resources3["people"] += nlo_random["people"]
    resources3["army"] += nlo_random["army"]
    resources3["faith"] += nlo_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')
elif eventss == 5:
    rand_input = int(input('Введите число от 1 до 2'))
    nekr_random = random.choice(nekr)
    print(f"Событие: {nekr_random['name']}")
    resources1["money"] += nekr_random["money"]
    resources1["people"] += nekr_random["people"]
    resources1["army"] += nekr_random["army"]
    resources1["faith"] += nekr_random["faith"]
    resources2["money"] += nekr_random["money"]
    resources2["people"] += nekr_random["people"]
    resources2["army"] += nekr_random["army"]
    resources2["faith"] += nekr_random["faith"]
    resources3["money"] += nekr_random["money"]
    resources3["people"] += nekr_random["people"]
    resources3["army"] += nekr_random["army"]
    resources3["faith"] += nekr_random["faith"]
    print(f'Ресурсы команды {team1}:{resources1}')
    print(f'Ресурсы команды {team2}:{resources2}')
    print(f'Ресурсы команды {team3}:{resources3}')
    print('---------------------------------------------')

score1 = resources1["money"] + resources1["people"] + resources1["army"] + resources1["faith"]
score2 = resources2["money"] + resources2["people"] + resources2["army"] + resources2["faith"]
score3 = resources3["money"] + resources3["people"] + resources3["army"] + resources3["faith"]

if score1 > score2 and score1 > score3:
    print(f'Победила команда {team1}!!!???')
elif score2 > score1 and score2 > score3:
    print(f'Победила команда {team2}!!!???')
else:
    print(f'Победила команда {team3}!!!???')
