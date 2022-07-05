from Animal import Animal
from animals.artiodactyls.Ram import Ram
from animals.artiodactyls.milkGivers.Cow import Cow
from animals.artiodactyls.milkGivers.Goat import Goat
from animals.birds.Chicken import Chicken
from animals.birds.Duck import Duck
from animals.birds.Goose import Goose
from animals.artiodactyls.MilkGivers import MilkGivers
from animals.Bird import Bird

if __name__ == '__main__':
    Animal.animals = [Goose("Серый", 3), Goose("Белый", 4), Cow("Манька", 100), Ram("Барашек", 50), Ram("Кудрявый", 55), Chicken("Ко-ко", 3),
                      Chicken("Кукареку", 2), Goat("Рога", 66), Goat("Копыта", 44), Duck("Кряква", 100500)]
    all_weight = 0
    most_weight_animal = Animal("", 0)
    for animal in Animal.animals:
        all_weight += animal.weight
        print(animal.name)
        print(animal.weight)
        animal.feed()
        if isinstance(animal, MilkGivers):
            animal.get_milk()
        elif isinstance(animal, Ram):
            animal.cut()
        elif isinstance(animal, Bird):
            animal.get_eggs()
        print()
        if most_weight_animal.weight < animal.weight:
            most_weight_animal = animal
    print(f"All weight is: {all_weight}")
    print(f"The fattest is: {most_weight_animal.name}. He's weight is: {most_weight_animal.weight}")