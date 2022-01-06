# Iterables, Iterators and Lazy Evaluation

### Iterables:

Every collection in python is an *iterable*.

**Sequences** are always *iterable*; as are objects implementing ***getitem*** method that takes 0 based indexes.

**objects** which implements ***iter*** method returning an **iterator** are **iterables**.

### Iterators:

**Iterators** are internally used to support:

- for loops
- Collection types construction and extension
- Looping over text files line by line
- List, dict, and set comprehensions
- Tuple unpacking
- Unpacking actual parameters with * in function calls

The standard **interface** for an interator has two methods:

1. **next**
   - Returns the next available item.
   - Raises **StopIteration** when no more items.
2. **iter**
   - Returns *self*.

### What is a generator function in Python?

Any function which has **yield** statement is called as **generator** function.

**Generators** are nothing but **iterators** that **produces** the value of the expression passed to **yield**.

When the body of the generator function completes, the generator object raises **StopIteration**

### Yield From

When there are multiple generators are involved to produce / yield values, one way to implement is using nested for loop. Another way it to replace the inner-loop with **yield from**.

### Generator Expression

The Generator Expression looks more like list comprehension but it is **enclosed in parentheses** rather than the square brackets.

The genertor expressions produces a **generator**. Generator in turn is a **iterator**.

---

### About Assignment

* Implement **Polygon** and evaluate the methods lazily.

  ```
  Help on class RegConvexPolygon in module polygon:
  
  class RegConvexPolygon(builtins.object)
   |  RegConvexPolygon(num_vertices, circumradius)
   |  
   |  Class which describes the regular convex polygon.
   |  Regular Convex polygon follows the below rules:
   |  1. All sides are equal length.
   |  2. All interior angles are less than 180 degrees.
   |  
   |  This class implements the following as python properties:
   |  1. num_vertices (n)
   |  2. circumradius (R)
   |  3. interior_angle
   |  4. edge_length
   |  5. apothem
   |  6. area
   |  7. perimeter
   |  
   |  Make sure the properties are lazily evaluated.
   |  
   |  Methods defined here:
   |  
   |  __eq__(self, other)
   |      Return self==value.
   |  
   |  __gt__(self, other)
   |      Return self>value.
   |  
   |  __init__(self, num_vertices, circumradius)
   |      Initialize self.  See help(type(self)) for accurate signature.
   |  
   |  __repr__(self)
   |      Return repr(self).
   |  
   |  ----------------------------------------------------------------------
   |  Data descriptors defined here:
   |  
   |  __dict__
   |      dictionary for instance variables (if defined)
   |  
   |  __weakref__
   |      list of weak references to the object (if defined)
   |  
   |  apothem
   |  
   |  area
   |  
   |  circumradius
   |  
   |  edge_length
   |  
   |  interior_angle
   |  
   |  num_vertices
   |  
   |  perimeter
   |  
   |  ----------------------------------------------------------------------
   |  Data and other attributes defined here:
   |  
   |  __hash__ = None
  ```

  * **PolygonIterator**

    ```
    class PolygonIterator(builtins.object)
     |  PolygonIterator(num_vertices, cmn_radius)
     |  
     |  This is a polygon iterator class.
     |  This will yields a polygon.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, num_vertices, cmn_radius)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |  
     |  __next__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    ```

    

  * **Polygons**

    ```
    class Polygons(builtins.object)
     |  Polygons(num_vertices, cmn_radius)
     |  
     |  Updating the max efficiency property as lazy property.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, num_vertices, cmn_radius)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |  
     |  __len__(self)
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  max_efficiency
    ```

    
