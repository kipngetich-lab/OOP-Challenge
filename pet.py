class Pet:
    def __init__(self, name, pet_type):
        # Initialize the pet with a name and type
        self.name = name  # Name of the pet
        self.pet_type = pet_type  # Type of the pet (e.g., dog, cat)
        self.hunger = 0  # Start full (0 means not hungry)
        self.energy = 10  # Start fully rested (10 means full energy)
        self.happiness = 5  # Neutral happiness level (scale from 0 to 10)
        self.tricks = []  # List to store tricks the pet has learned

    def eat(self):
        # Method for the pet to eat and reduce hunger
        if self.hunger > 0:  # Check if the pet is hungry
            self.hunger = max(0, self.hunger - 3)  # Decrease hunger by 3, but not below 0
            self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1, but not above 10
            print(f"{self.name} 🐾 is eating! Hunger is now {self.hunger}.")
        else:
            print(f"{self.name} 🐾 is not hungry!")  # Notify if the pet is not hungry

    def sleep(self):
        # Method for the pet to sleep and regain energy
        self.energy = min(10, self.energy + 5)  # Increase energy by 5, but not above 10
        print(f"{self.name} 💤 is sleeping! Energy is now {self.energy}.")

    def play(self):
        # Method for the pet to play, affecting energy, happiness, and hunger
        if self.energy >= 2:  # Check if the pet has enough energy to play
            self.energy = max(0, self.energy - 2)  # Decrease energy by 2, but not below 0
            self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2, but not above 10
            self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1, but not above 10
            print(f"{self.name} 🎉 is playing! Energy is now {self.energy}, happiness is {self.happiness}, hunger is {self.hunger}.")
        else:
            print(f"{self.name} 😴 doesn't have enough energy to play!")  # Notify if the pet is too tired to play

    def get_status(self):
        # Method to get the current status of the pet
        status = (f"Status of {self.name} ({self.pet_type}):\n"
                  f"Hunger: {self.hunger}/10\n"
                  f"Energy: {self.energy}/10\n"
                  f"Happiness: {self.happiness}/10")
        print(status)  # Print the status of the pet

    def train(self, trick):
        # Method for the pet to learn a new trick
        self.tricks.append(trick)  # Add the new trick to the list of tricks
        print(f"{self.name} learned a new trick: {trick}! 🎓")  # Notify that the trick has been learned

    def show_tricks(self):
        # Method to display all tricks the pet has learned
        if self.tricks:  # Check if there are any tricks learned
            tricks_list = ', '.join(self.tricks)  # Create a string of all tricks
            print(f"{self.name} knows the following tricks: {tricks_list}.")  # Print the list of tricks
        else:
            print(f"{self.name} hasn't learned any tricks yet.")  # Notify if no tricks have been learned
