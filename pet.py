class Pet:
    def __init__(self, name, pet_type):
        # Initialize the pet with a name and type
        self.name = name  # Name of the pet
        self.pet_type = pet_type  # Type of the pet (e.g., dog, cat)
        self.hunger = 5  # Initial hunger level
        self.energy = 5  # Initial energy level
        self.happiness = 5  # Initial happiness level
        self.tricks = []  # List to store tricks the pet has learned

    def eat(self):
        # Method for the pet to eat and reduce hunger
        if self.hunger > 0:  # Check if the pet is hungry
            self.hunger = max(0, self.hunger - 3)  # Decrease hunger by 3, but not below 0
            self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1, but not above 10
            print(f"{self.name} 🐾 is eating.....")
        else:
            print(f"{self.name} 🐾 is not hungry!")  # Notify if the pet is not hungry

    def sleep(self):
        # Method for the pet to sleep and regain energy
        self.energy = min(10, self.energy + 5)  # Increase energy by 5, but not above 10
        print(f"{self.name} 💤 is sleeping.....")

    def play(self):
        # Method for the pet to play, affecting energy, happiness, and hunger
        if self.energy >= 2:  # Check if the pet has enough energy to play
            self.energy = max(0, self.energy - 2)  # Decrease energy by 2, but not below 0
            self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2, but not above 10
            self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1, but not above 10
            print(f"{self.name} 🎉 is playing.....")
        else:
            print(f"{self.name} 😴 doesn't have enough energy to play!")  # Notify if the pet is too tired to play

    def get_status(self):
        # Method to get the current status of the pet
        status = (f"Hunger: {self.hunger}\n"
                  f"Energy: {self.energy}\n"
                  f"Happiness: {self.happiness}")
        print(status)  # Print the status of the pet

    def train(self, trick):
        # Method for the pet to learn a new trick
        if trick not in self.tricks:
            self.tricks.append(trick)  # Add the new trick to the list of tricks
        else:
            print(f"{self.name}({self.pet_type} ) already knows '{trick}'!")

    def show_tricks(self):
        # Method to display all tricks the pet has learned
        if self.tricks:  # Check if there are any tricks learned
            print(f"{self.name} knows the following tricks: {self.tricks}.")  # Print the list of tricks
        else:
            print(f"{self.name} hasn't learned any tricks yet.")  # Notify if no tricks have been learned
