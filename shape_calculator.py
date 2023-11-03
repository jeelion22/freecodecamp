class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            length = "*" * self.width + "\n"
            picture = self.height * length
            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, instance):
        amount = self.get_area() // instance.get_area()
        return amount

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_side):
        self.side = new_side
        self.set_width(new_side)
        self.set_height(new_side)

    def __str__(self):
        return f"Square(side={self.width})"
