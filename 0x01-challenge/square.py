#!/usr/bin/python3
""" Defines a Square class """


class square():
    """ Documentation """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialisation of square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of a square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Square instance string format """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
