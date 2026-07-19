#Pytests are written with functions that use the operation, assert(). An assert is a commonly used debugging tool in Python that 
# allows programmers to include sanity checks in their code. They ensure certain conditions or assumptions hold true during runtime. 
# If the condition provided to assert() turns out to be false, it indicates a bug in the code, an exception is raised, and halts the program’s execution. 
# Typically, code provides an assert condition followed by an optional message. An example is: 

def divide(a, b):
	assert b != 0, "Cannot divide by zero"
	return a / b

# Pytest fixtures
# Fixtures are used to separate parts of code that only run for tests. 
# They are reusable pieces of test setups and teardown code that are shared across multiple tests. 
# Fixtures benefit developers by assisting in keeping their tests clean and avoiding code duplication. 
# Let’s look at an example of using a pytest in Python:

import pytest
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False


    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()


    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)


    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)