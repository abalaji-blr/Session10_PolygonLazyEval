from functools import lru_cache
from polygon import RegConvexPolygon

class PolygonIterator:
  '''
  This is a polygon iterator class.
  This will yields a polygon.
  '''
  def __init__(self, num_vertices, cmn_radius):
    if (num_vertices < 3):
      raise ValueError('number of vertices should be greater than 3.')
    self._num_vert = num_vertices
    self._radius = cmn_radius
    self._idx = 3

  def __iter__(self):
    return(self)

  def __next__(self):
    if self._idx > self._num_vert:
      raise StopIteration
    else:
      polygon = RegConvexPolygon(self._idx, self._radius)
      self._idx += 1
      return polygon



class Polygons:
  '''
  Updating the max efficiency property as lazy property.
  '''
  def __init__(self, num_vertices, cmn_radius):
    if num_vertices < 3:
      raise ValueError('The number of vertices should be atleast 3.')
    self._num_vert = num_vertices
    self._radius   = cmn_radius
    self._max_efficiency_polygon = None

  def __iter__(self):
    return PolygonIterator(self._num_vert, self._radius)

  def __repr__(self):
    txt = 'Polygon with {} vertices and {} as circumradius.'.format(self._num_vert,
                                                                    self._radius
                                                                    )
    return(txt)

  def __len__(self):
    return(self._num_vertices - 2)
  
  @property
  def max_efficiency(self):
    if self._max_efficiency_polygon is None:
      sorted_polygons = sorted(PolygonIterator(self._num_vert, self._radius),
                                key=lambda p: p.area / p.perimeter,
                                reverse=True)
      self._max_efficiency_polygon = sorted_polygons[0]

      return(self._max_efficiency_polygon)