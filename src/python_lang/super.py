import pprint

# Raymond Hettinger - Super considered super! - PyCon 2015

# Inheritance is a tool for code reuse

# Single inheritance is easy

# Multiple inheritance is easy, if the super classes have no overlapping
# methods

# Multiple inheritance with overlapping methods is hard
# C3 superclass linearization algorithm
# Put inheritance tree in a line
# Why? I want to "visit" each class in a particular fashion

# What is the problem with super()?

# super() in Python does not behave the same as in other programming
# languages

# In other languages...
# super() calls the parent class in single inheritance
# super() calls the parent classes in multiple inheritance

# Family Tree
class Adam(object): pass                    # noqa
class Eve(object): pass                     # noqa
class Philip(Adam, Eve): pass               # noqa

# -- At this point in time, Philip super() calls Adam and Eve

class Elizabeth2(Adam, Eve): pass           # noqa
class Charles3(Philip, Elizabeth2): pass    # noqa
class John(Adam, Eve): pass                 # noqa
class Frances(Adam, Eve): pass               # noqa
class Diane(John, Frances): pass             # noqa
class William(Charles3, Diane): pass        # noqa


# -- At this point in time, William's inheritance tree matters
# -- super() priortizes William's ancestors

pprint.pprint(William.mro())

# In Python, super() calls the parent and/or the ancestors of the children

# object
# |
# - Single inheritance
# |
# Adam

# Adam                   Eve
# |                      |
# - Multiple inheritance -
# |
# Philip

# Philip gets married to Elizabeth2
# Their inheritance trees are still seperate
# Philip and Elizabeth2 have a child: Charles3
# Their inheritance trees get joined

pprint.pprint(Charles3.mro())

# Charles3 ancestors tree gets merged into Philip's inheritance tree

# Interesting point: super() is dynamic, at one point Philip's super()
# called Adam, Eve -- When Charles3 was defined, Philip's super()
# now calls Elizabeth2 (whom may not have existed at the time either)

# Bad? super() should have been called next_in_line()

# Good! In any case, super makes the line for us!
# Good! super() is dynamic, no advance notice of who is next in line!

# Since you cannot know where super() will go next, future children
# will get to change where the line goes

# Dependency Injection:
# You order from a restaurant
# The restaurant uses a supplier
# The supplier matters to you; so make it part of the public API
# You tell the restaurant what supplier to use
# The supplier becomes a dependency

# Don't like the supplier?
# Subclass the restaurant and change it's base class
# Without breaking the public API (interface)


class BadSupplier:
    def __init__(self) -> None:
        print("Bad Supplier")


class GoodSupplier(BadSupplier):
    def __init__(self) -> None:
        print("Good Supplier")


class Restaurant(BadSupplier):
    def __init__(self) -> None:
        print("Restaurant")
        # BadSupplier.__init__()  # bad: hardwired dependency
        super().__init__()        # good: dynamic resolution


# The BadSupplier dependency is not hardwired since we are using
# super()

r = Restaurant()


class NewRestaurant(Restaurant, GoodSupplier):
    pass


# The inheritance tree is no longer determined by Restaurant
# It is now determined by its child: NewRestaurant

r = NewRestaurant()

# NewRestaurant causes Restaurant to call GoodSupplier instead of their
# parent BadSupplier

# IMPORTANT NOTE: The public API of Restaurant didn't changee

# Understanding super() in Python:
# Rename super() to next_in_line()
# Who makes the line? Python
# How can I see the line? Class.mro()
# How can I alter the line? Subclass and change the inherited base classes

# Algorithm:
# Children are called before their parents
# Parents get called in the listed order
