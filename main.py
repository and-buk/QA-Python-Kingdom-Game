import random
from typing import Optional
from typing import Tuple

monster_counter = 0
hp = 20
attack = 10


def get_event() -> str:
    """Случайным образом выбираем одно игровое событие."""
    return random.choice(("sword", "apple", "monster"))


def get_user_input(event: str) -> Optional[int]:
    """В зависимости от текущего игрового события получаем от пользователя корректное действие."""
    decision = None
    while True:
        try:
            if event == "sword":
                decision = int(
                    input(
                        f"У рыцаря {attack}! 1 - Взять новый меч. 2 - Оставить на месте. "
                    )
                )
                if decision > 2 or decision < 1:
                    raise ValueError()
            elif event == "monster":
                decision = int(
                    input(
                        f"У рыцаря {hp} жизней, сила атаки {attack}! 1 - Атаковать. 2 - Отступить. "
                    )
                )
                if decision > 2 or decision < 1:
                    raise ValueError()
        except ValueError:
            print("Неккоректный ввод! Значение должно быть 1 или 2! Повторите ввод!")
        else:
            break
    return decision


def create_monster() -> Tuple[int, int]:
    """Создаём чудовище с произвольным значением уровня здоровья и силы атаки."""
    monster_hp = random.randint(1, 20)
    monster_attack = random.randint(1, 20)
    return monster_hp, monster_attack


def game() -> None:
    """Обеспечиваем игровой процесс в соответствии с заданным игровым сценарием."""
    global attack, monster_counter, hp
    journey = True
    while journey:
        event = get_event()
        if event == "sword":
            sword_power = random.randint(10, 20)
            print(f"Найден MEЧ! Сила атаки меча {sword_power}.")
            decision = get_user_input(event)
            if decision == 1:
                attack = sword_power
            elif decision == 2:
                pass
            continue
        elif event == "apple":
            health_bonus = random.randint(1, 10)
            hp = hp + health_bonus
            print(
                f"Вы нашли яблочко здоровья! +{health_bonus} к здоровью героя. У героя {hp} жизней."
            )
            continue
        elif event == "monster":
            monster_hp, monster_attack = create_monster()
            print(
                f"БОЙ! Вы встретили чудовище. Жизней {monster_hp}. Сила атаки {monster_attack}."
            )
            decision = get_user_input(event)
            if decision == 1:
                while monster_hp > 0 and hp > 0:
                    monster_hp = monster_hp - attack
                    hp = hp - monster_attack
                    if hp > 0 and monster_hp > 0:
                        print(
                            f"БОЙ! Чудовище ранено! Осталось жизней {monster_hp}. Сила атаки {monster_attack}."
                        )
                        decision = get_user_input(event)
                        if decision == 1:
                            monster_hp = monster_hp - attack
                            hp = hp - monster_attack
                        elif decision == 2:
                            break
                if hp <= 0 and monster_hp <= 0:
                    print("ПОРАЖЕНИЕ")
                    break
                if hp <= 0:
                    print("ПОРАЖЕНИЕ")
                    break
                monster_counter += 1
            elif decision == 2:
                continue
        if monster_counter == 10:
            print("ПОБЕДА")
            journey = False
    quit()


if __name__ == "__main__":
    game()
