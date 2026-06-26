import random
import time

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.knowledge = 0
        self.sanity = 100
        self.satiety = 100
        self.health = 100
        self.anxiety = 0
        self.day = 0
        self.food = 100

    def get_knowledge(self):
        if self.anxiety > 50:
            self.knowledge = self.knowledge + 5

    def have_anxiety(self):
        if self.day < 5:
            self.anxiety = self.anxiety + 20
        elif self.day > 5:
            self.anxiety = self.anxiety + 20 * self.day

    def eat(self, found):
        if self.food <= 0:
            if found:
                print("You have found food! Congratulations!")
                self.satiety = self.satiety + 40
                self.health = self.health + 20
                self.anxiety = self.anxiety - 10
            else:
                self.satiety = self.satiety - 20
                self.health = self.health - 20
                self.anxiety = self.anxiety + 10

    def see_entity(self, will_be_seen):
        if will_be_seen:
            self.sanity = self.sanity - 20
            self.anxiety = self.anxiety + 10
            self.knowledge = self.knowledge + 10
        else:
            print("Next time I'll get you!")

    def is_alive(self):
        if self.satiety <= 0:
            print("You died of hunger(Wheres your waisttt)")
            return False
        if self.health <= 0:
            print("Das gute ist, du musst keine Steuern mehr bezahlen :D yay")
            return False
        if self.sanity <= 0:
            print("ho, ho, ho. you went insane.")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        return True

    def days_indexes(self, day):
        day_title = f"Today is the {day}. of {self.name} life."
        print(f"{day_title:*^50}\n")

        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}\n")
        print(f"anxiety - {self.anxiety}")
        print(f"Satiety - {self.satiety}")
        print(f"sanity - {self.sanity}")
        print(f"knowledge - {self.knowledge}")
        print(f"health - {self.health}")

human = Human("retard")

for day in range(1, 365):
    if not human.live(day):
        break
    random_boolean = random.choice([True, False])
    random_activity = random.randint(1, 4)
    if random_activity == 1:
        human.eat(random_boolean)
    elif random_activity == 2:
        human.see_entity(random_boolean)
    elif random_activity == 3:
        human.get_knowledge()
    else:
        human.have_anxiety()
    human.days_indexes(day)
    time.sleep(3)







