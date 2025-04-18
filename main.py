from pet import Pet


def main():
    # Create a pet object
    my_pet = Pet(name="Buddy", pet_type="Dog")
    print(f"Creating pet: {my_pet.name} ({my_pet.pet_type})")
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    # Show current status
    print(f"{my_pet.name}'s current status: ")
    my_pet.get_status()

    # Training tricks
    my_pet.train("Roll Over")
    my_pet.train("Shake Hands")
    my_pet.train("Shake Hands")  # Trying to learn same trick twice

    # Show learned tricks
    my_pet.show_tricks()

    # Edge case: try to play when energy is 0
    my_pet.energy = 0  # Manually set energy to 0 for testing
    my_pet.play()


if __name__ == "__main__":
    main()
