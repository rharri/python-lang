from threading import local, Thread


class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"My name is: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()


def f():
    # 'dog' attribute does not exist if this is a different thread
    # print(my_pet.dog) raises an error
    my_pet.dog = Dog("Bruce")
    log.append(my_pet.dog)


def g():
    print(my_pet.dog)
    my_pet.dog = Dog("Bruce")


if __name__ == "__main__":
    log: list[Dog] = []

    my_pet = local()
    my_pet.dog = Dog("Nino")
    print(my_pet.dog)

    thread = Thread(target=f)
    thread.start()
    thread.join()
    print(log[0])

    print(my_pet.dog)

    g()  # Runs from the main thread
    print(my_pet.dog)


# For more information:
# >>> import _threading_local
# >>> help(_threading_local)
