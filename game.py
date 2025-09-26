# game.py

from abc import ABC, abstractmethod

class Weapon(ABC):
    """
    Абстрактный базовый класс для всего оружия.
    Определяет обязательный метод attack, который должны реализовать все подклассы.
    """
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    """
    Класс для оружия "Меч".
    """
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    """
    Класс для оружия "Лук".
    """
    def attack(self):
        return "Боец наносит удар из лука."

class Axe(Weapon):
    """
    Новый класс оружия "Топор", добавленный для демонстрации расширяемости.
    """
    def attack(self):
        return "Боец наносит мощный удар топором."

class Monster:
    """
    Класс, представляющий монстра.
    """
    def __init__(self, name="Монстр"):
        self.name = name

class Fighter:
    """
    Класс, представляющий бойца. Он может менять оружие и сражаться.
    """
    def __init__(self):
        # Поле для хранения объекта оружия. Изначально боец безоружен.
        self.weapon: Weapon = None

    def change_weapon(self, new_weapon: Weapon):
        """
        Метод для смены оружия бойца.
        """
        self.weapon = new_weapon
        weapon_name_map = {
            'Sword': 'меч',
            'Bow': 'лук',
            'Axe': 'топор'
        }
        # Получаем название оружия для вывода в консоль
        weapon_name = weapon_name_map.get(new_weapon.__class__.__name__, 'неизвестное оружие')
        print(f"Боец выбирает {weapon_name}.")

    def fight(self, monster: Monster):
        """
        Метод для демонстрации боя с монстром.
        Боец использует атаку своего текущего оружия.
        """
        if not self.weapon:
            print("Боец не вооружен и не может атаковать!")
            return
        
        # Благодаря полиморфизму, будет вызвана реализация метода для конкретного оружия.
        attack_message = self.weapon.attack()
        print(attack_message)
        print(f"{monster.name} побежден!")

# Основная часть программы для демонстрации работы классов
if __name__ == "__main__":
    # Создаем объекты
    monster = Monster()
    sword = Sword()
    bow = Bow()
    axe = Axe()
    fighter = Fighter()

    # Бой с мечом
    fighter.change_weapon(sword)
    fighter.fight(monster)
    print("-" * 20)

    # Бой с луком
    fighter.change_weapon(bow)
    fighter.fight(monster)
    print("-" * 20)
    
    # Бой с новым оружием - топором
    fighter.change_weapon(axe)
    fighter.fight(monster)