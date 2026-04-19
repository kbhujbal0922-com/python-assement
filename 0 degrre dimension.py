# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


# Derived class (Child)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Override parent method
        print(f"{self.name} the {self.breed} barks!")


# Example usage
if __name__ == "__main__":
    animal = Animal("Generic Animal")
    dog = Dog("Buddy", "Golden Retriever")

    print("Parent class output:")
    animal.speak()

    print("\nChild class output:")
    dog.speak()
