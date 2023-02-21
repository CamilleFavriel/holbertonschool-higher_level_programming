#!/usr/bin/python3
""" Rectangle Class that inherits from Base """
Base = __import__('base').Base

class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self.__height = value
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self.__y = value
