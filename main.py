# 1. Определение базового класса Animal
class Animal:
    def __init__(self, name, age):
        """Конструктор, задающий общие атрибуты: имя и возраст животного"""
        self.name = name
        self.age = age

    def make_sound(self):
        """Метод, который будет переопределен в подклассах"""
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self):
        """Общее поведение для всех животных: животные едят"""
        print(f"{self.name} ест.")

# 2. Создание подклассов Bird, Mammal и Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        """Добавляем атрибут размаха крыльев для птиц"""
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        """Переопределяем метод: звук птицы"""
        print(f"{self.name} чирикает.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        """Добавляем атрибут цвета меха для млекопитающих"""
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        """Переопределяем метод: звук млекопитающего"""
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        """Добавляем атрибут типа чешуи для рептилий"""
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        """Переопределяем метод: звук рептилии"""
        print(f"{self.name} шипит.")

# 3. Полиморфизм: функция, принимающая список животных и вызывающая make_sound для каждого
def animal_sound(animals):
    """Принимает список объектов типа Animal и вызывает метод make_sound для каждого"""
    for animal in animals:
        animal.make_sound()

# 4. Композиция: класс Zoo, который содержит животных и сотрудников
class Zoo:
    def __init__(self):
        """Конструктор создает пустые списки для животных и сотрудников"""
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        """Метод для добавления животного в зоопарк"""
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_employee(self, employee):
        """Метод для добавления сотрудника в зоопарк"""
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee.name}")

# 5. Создание классов для сотрудников ZooKeeper и Veterinarian
class ZooKeeper:
    def __init__(self, name):
        """Конструктор задает имя смотрителя зоопарка"""
        self.name = name

    def feed_animal(self, animal):
        """Метод для кормления животных"""
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        """Конструктор задает имя ветеринара"""
        self.name = name

    def heal_animal(self, animal):
        """Метод для лечения животных"""
        print(f"{self.name} лечит {animal.name}.")

# Дополнительно: сохранение информации о зоопарке в файл и загрузка данных
import pickle

def save_zoo(zoo, filename):
    """Функция для сохранения состояния зоопарка в файл с использованием pickle"""
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)
    print(f"Данные зоопарка сохранены в файл {filename}.")

def load_zoo(filename):
    """Функция для загрузки состояния зоопарка из файла"""
    with open(filename, 'rb') as f:
        zoo = pickle.load(f)
    print(f"Данные зоопарка загружены из файла {filename}.")
    return zoo

# Демонстрация работы программы

# Создаем объекты животных
parrot = Bird("Попугай", 2, 0.5)
lion = Mammal("Лев", 5, "Золотой")
snake = Reptile("Змея", 3, "Гладкая")

# Создаем зоопарк и добавляем животных
zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

# Полиморфизм: вызов make_sound для каждого животного
animal_sound(zoo.animals)

# Добавляем сотрудников в зоопарк
zookeeper = ZooKeeper("Иван")
vet = Veterinarian("Анна")
zoo.add_employee(zookeeper)
zoo.add_employee(vet)

# Смотритель кормит животных, ветеринар лечит
zookeeper.feed_animal(lion)
vet.heal_animal(snake)

# Сохраняем и загружаем состояние зоопарка
save_zoo(zoo, "zoo_data.pkl")
loaded_zoo = load_zoo("zoo_data.pkl")

# Проверка, что данные восстановлены
animal_sound(loaded_zoo.animals)
