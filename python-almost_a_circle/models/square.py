#!/usr/bin/python3
"""class Square that inherites from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {size}"
    
    @property
    def size(self):
        return self.width
    
    