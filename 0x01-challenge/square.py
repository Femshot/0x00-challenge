#!/usr/bin/python3
""" Defines a Square class """


class square():
    """ Documentation """
    width = 0

    def __init__(self, *args, **kwargs):
        """ Initialisation of square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ Perimeter of a square """
        return (self.width * 4)

    def __str__(self):
        """ Square instance string format """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=10)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
