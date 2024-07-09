# pylint: disable=too-few-public-methods missing-module-docstring


class Shape:

    """
    A base class for different shape.

    Attributes:
    color(str): the color of the shape.
    name(str): the name of the shape.
    """

    def __init__(self, color, name):
        """
        Initialize the Shape with a color and a name

        Args:
            color(str): the color of the shape.
            name(str): the name of the shape.
        """
        self.color = color
        self.name = name


    def say_name(self):
        """
        Return a string stating the name of the shape.

        Returns:
            str: A string stating the name of the shape.
        """
        return f"My name is {self.name}."


class Rectangle(Shape):
    """
    A class to represent a rectangle, inherited from Shape.

    Attributes:
        color (str): The color of the rectangle.
        name (str): The name of the rectangle.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, color, name, width, height):

        """
        Initialize the Rectangle with a color, name, width, and height.

        Args:
            color (str): The color of the rectangle.
            name (str): The name of the rectangle.
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):

        """
        Return a string stating the name of the rectangle.

        Returns:
            str: A string stating the name of the rectangle.
        """

        return f"My name is {self.name} and I am a rectangle."

    def area(self):

        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):

        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """

        return (self.width + self.height) * 2


class Circle(Shape):

    """
    A class to represent a circle, inherited from Shape.

    Attributes:
        color (str): The color of the circle.
        name (str): The name of the circle.
        radius (float): The radius of the circle.
    """

    def __init__(self, color, name, radius):

        """
        Initialize the Circle with a color, name, and radius.

        Args:
            color (str): The color of the circle.
            name (str): The name of the circle.
            radius (float): The radius of the circle.
        """

        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """
        Return a string stating the name of the circle.

        Returns:
            str: A string stating the name of the circle.
        """
        return f"My name is {self.name} and I am a circle."


    def area(self):

        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """

        return 3.14*(self.radius**2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter (circumference) of the circle.
        """

        return 2*3.14*self.radius
