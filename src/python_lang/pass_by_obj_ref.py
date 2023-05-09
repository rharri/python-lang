import copy as cp


class Animal:
    """Represents an Animal."""

    def __init__(self, name) -> None:
        """Initialize a new instance of Animal."""
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}: {id(self)}"


# Pass-by-value
# Pass a copy of the value (with a new memory address) to the function
# Argument modifications do not persist, since a copy is being modified
# If the argument value is a 'reference' to a mutable object, reassignment does
# not persist, but modification of attributes of the object do persist beyond
# function exit
# If the argument value is a pointer, reassignment and modifications do persist
# Languages: C, C++, Java, C#

# Pass-by-reference
# Pass the memory address of the value to the function
# Argument modifications persist beyond function exit
# Depending on the language, argument reassignment may or may not persist
# beyond the function exit (C++ doesn't allow it, C# does)
# Languages: C++, C#

# Pass-by-object-reference
# Create a new name in the function scope and bind it to object instance of
# the value. The argument name points to the object instance passed in.
# Rebinding the argument name to a new object instance does not persist
# If the argument name is bound to a mutable object, attribute modifications
# persist beyond function exit
# Languages: Python


# Passing by reference to avoid copying large objects
# Not required in Python since only the object reference is passed

# See: https://realpython.com/python-pass-by-reference
# Pass by reference can be simulated:
# - Use 'global' keyword
# - Return + reassign
# - Modify object attribute
# - Use dictionary, list
# - Use SimpleNamespace


def rebind_arg(x: Animal) -> None:
    # Rebinds x to a new Animal object
    x = Animal("Mountain Lion")
    print(f"x = {x}")


def mutate_tuple(x: tuple[int, int]) -> None:
    # Tuple's cannot be modified - immutable
    # x[1] = 42 raises a TypeError
    print(f"x = {x}")


def mutate_list(x: list[Animal]) -> None:
    # x is bound to the list instance passed as an argument
    # A new Animal object is created and assigned to an index of x
    # Modifying x modifies the original list
    x[1] = Animal("Mountain Lion")


def mutate_user_defined(x: Animal) -> None:
    # x is bound to the Animal instance passed as an argument
    # Modifying the attributes of x modifies the original Animal object
    x.name = "Mountain Lion"


def shallow_copy(original: list[Animal]) -> None:
    # Create a shallow copy of the list that is passed as an argument
    # Modifying the copy does not change list instance that was passed in
    copy = cp.copy(original)
    copy[1] = Animal("Mountain Lion")

    print(f"orig[2] = {original[2]}")
    print(f"copy[2] = {copy[2]}")


def deep_copy(original: list[Animal]) -> None:
    # Create a deep copy of the list that is passed as an argument
    # Modifying the copy does not change list instance that was passed in
    copy = cp.deepcopy(original)
    copy[1] = Animal("Mountain Lion")

    print(f"orig[2] = {original[2]}")
    print(f"copy[2] = {copy[2]}")


def return_new_reference(x: Animal) -> Animal:
    # x is bound to the Animal instance passed as an argument
    # Return a new object reference
    x = Animal("Mountain Lion")
    return x


if __name__ == "__main__":
    animal1 = Animal("Fox")
    print(f"animal1 = {animal1}")
    rebind_arg(animal1)
    print(f"animal1 = {animal1} (rebind in a function does not reflect back)")
    print(end="\n")

    point = (1, 5)
    print(f"point = {point}")
    mutate_tuple(point)
    print(f"point = {point} ('tuple' is immutable)")
    print(end="\n")

    animals1 = [Animal("Tiger"), Animal("Fox"), Animal("Lion")]
    print(f"animals1 = {animals1}")
    mutate_list(animals1)
    print(f"animals1 = {animals1} ('list' is mutable)")
    print(end="\n")

    animals2 = [Animal("Tiger"), Animal("Fox"), Animal("Lion")]
    print(f"animals2 = {animals2}")
    shallow_copy(animals2)
    print(f"animals2 = {animals1} (shallow copy refs the original objects)")
    print(end="\n")

    animals3 = [Animal("Tiger"), Animal("Fox"), Animal("Lion")]
    print(f"animals3 = {animals3}")
    deep_copy(animals3)
    print(f"animals3 = {animals3} (deep copy copies the original objects)")
    print(end="\n")

    animal2 = Animal("Fox")
    print(f"animal2 = {animal2}")
    mutate_user_defined(animal2)
    print(f"animal2 = {animal2} (user defined classes are mutable)")
    print(end="\n")

    animal3 = Animal("Fox")
    print(f"animal3 = {animal3}")
    animal3 = return_new_reference(animal3)
    print(f"animal3 = {animal3} (returned an object reference)")
