from python_lang.super import BadSupplier, Restaurant


class MockSupplier(BadSupplier):
    def __init__(self) -> None:
        print("Mock Supplier")


# In essence we are telling Restaurant to use MockSupplier
class MockedRestaurant(Restaurant, MockSupplier):
    pass


def test_restaurant(capsys):
    MockedRestaurant()
    assert "Mock Supplier" in capsys.readouterr().out.split("\n")


m = MockedRestaurant()


# Testing a class with single inheritance, multiple inheritance     Side Effects
# whose dependency (the is-a) needs to be mocked:
#   - super() mro                                                       *                                                   
#   - pytest monkeypatching                                             *?
#   - pytest-mock                                                       *

# Testing a class with a has-a dependency:
#   - Duck typing                                                       *
#   - pytest monkeypatching                                             *?
#   - Protocols: structural subtyping                                   *
#   - Subclass the dependency? (grab the entire inheritance tree)       *
#   - pytest-mock                                                       *

# Testing side effects:
#   - pytest --fixtures (e.g. capsys)
#   - pytest-mock
