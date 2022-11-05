class Rectangle:
  width = 0
  height = 0
  
  #initialize class with specific width and height
  def __init__(self,wid,hei):
    self.width = wid
    self.height = hei
  
  #set width
  def set_width(self,wid):
    self.width = wid
  
  #set height
  def set_height(self,hei):
    self.height = hei
  
  #get area value
  def get_area(self):
    area = self.width * self.height
    return area
  
  #get perimeter value   
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter
  
  #get diagonal of the shape
  def get_diagonal(self):
    diagonal=(self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  #get the picture of the shape
  def get_picture(self):
    string=[]
    if(self.width>=50 | self.height>=50):
      string.append("Too big for picture.")
    else:
      for i in range(0,self.height):
        for j in range(0,self.width):
          string.append("*")
        string.append("\n")
    str = ''.join(string)
    return str

  # Takes another shape (square or rectangle) as an argument. 
  # Returns the number of times the passed in shape could fit inside the shape (with no rotations).
  def get_amount_inside(self,object):
    ins = self.get_area()
    area = object.get_area()
    modulo = ins % area
    res = (ins - modulo) / area
    return res

  #print width and height
  def __repr__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

class Square(Rectangle):
    width=0
    height=0
    def __init__(self,wid):
      self.width=wid
      self.height=wid
  
    def __repr__(self):
      return "Square(side="+str(self.width)+")"  

    def set_side(self,side):
      self.width=side
      self.height=side

    def set_width(self,side):
      self.width=side
      self.height=side

    def set_height(self,side):
      self.width=side
      self.height=side
