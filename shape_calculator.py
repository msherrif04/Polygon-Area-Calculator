class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height 

  def __str__(self):
    string =  (f"Rectangle(width={self.width}, height={self.height})")
    return string

  def set_width(self, width):
    self.width = width
    return True

  def set_height(self, height):
    self.height = height
    return True

  def get_area(self):
    area = self.height * self.width
    return area 

  def get_perimeter(self):
    perimeter = 2* self.width + 2*self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    picture = str()
    if self.width > 50 or self.height > 50: return "Too big for picture."
    columns = self.width
    rows = self.height
    
    for i in range(rows):
     for j in range(columns):
       if j != columns - 1:
         picture += "*"
       else:
         picture += "*\n"
    return picture

  def get_amount_inside(self,shape2):
    parent_area = self.get_area()
    child_area = shape2.get_area()
    amount_inside = parent_area//child_area
    return amount_inside

    
class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    
  def __str__(self):
    string =  (f"Square(side={self.height})")
    return string

  def set_side(self, side):
    self.width = side
    self.height = side
    print (self.width, self.height)
    return True

  def set_width(self,side):
    self.width = side
    self.height = side
    return True
    
  def set_height(self, side):
    self.width = side
    self.height = side
    return True

