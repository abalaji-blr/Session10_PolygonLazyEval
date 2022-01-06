import math

class RegConvexPolygon:
  '''
  Class which describes the regular convex polygon.
  Regular Convex polygon follows the below rules:
  1. All sides are equal length.
  2. All interior angles are less than 180 degrees.

  This class implements the following as python properties:
  1. num_vertices (n)
  2. circumradius (R)
  3. interior_angle
  4. edge_length
  5. apothem
  6. area
  7. perimeter

  Make sure the properties are lazily evaluated.
  '''
  def __init__(self, num_vertices, circumradius):
    self._num_vertices = num_vertices
    self._circumradius = circumradius

    # we want to do lazy evaluation of these properties.
    self._interior_angle = None
    self._edge_length = None
    self._apothem = None
    self._area = None
    self._perimeter = None


  @property
  def num_vertices(self):
    return(self._num_vertices)

  @property
  def circumradius(self):
    return(self._circumradius)

  @property
  def interior_angle(self):
    if self._interior_angle is None:
      self._interior_angle = (self._num_vertices - 2) * (180 / self._num_vertices)
    return(self._interior_angle)

  @property
  def edge_length(self):
    if self._edge_length is None:
      self._edge_length = 2 * self._circumradius * math.sin(math.pi / self._num_vertices)
    return(self._edge_length)

  @property
  def apothem(self):
    if self._apothem is None:
      self._apothem = self._circumradius * math.cos(math.pi / self._num_vertices)
    return(self._apothem)

  @property
  def area(self):
    if self._area is None:
      self._area = (1/2) * self._num_vertices * self.edge_length * self.apothem
    return(self._area)

  @property
  def perimeter(self):
    if self._perimeter is None:
      self._perimeter = self._num_vertices * self.edge_length
    return(self._perimeter)

  def __repr__(self):
    return(f'Regular Convex Polygon with {self._num_vertices} vertices and {self._circumradius} circumradius')

  def __eq__(self, other):
    if isinstance(other, RegConvexPolygon) == False:
      raise TypeError('Invalid type of object passed.')

    return(self._num_vertices == other.num_vertices and self._circumradius == other.circumradius)

  def __gt__(self, other):
    if isinstance(other, RegConvexPolygon) == False:
      raise TypeError('Invalid type of object passed.')

    return( self._num_vertices > other.num_vertices)