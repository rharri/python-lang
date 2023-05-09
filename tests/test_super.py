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


# Testing a class with single inheritance, multiple inheritance
# whose dependency (the is-a) needs to be mocked:
#   - super() mro                                                   *                                                   
#   - Python monkey patching                                        x
#   - pytest monkeypatching                                         x
#   - mocking                                                       *

# Testing a class with a has-a dependency:
#   - Duck typing                                                   *
#   - Python monkey patching                                        x
#   - pytest monkeypatching                                         x
#   - Protocols: structural subtyping                               *
#   - Subclass the dependency? (grab the entire inheritance tree)   *
#   - mocking                                                       *

# Testing sideffects:
#   - pytest --fixtures (e.g. capsys)
#   - pytest mock
