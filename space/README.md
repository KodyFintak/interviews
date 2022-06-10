# space

### Build

```
python3 setup.py install
```


### Test
```
pytest 
```

running tests in Jetbrains IDE

> right click `tests` folder and click `Run Python Tests in ...`


### Problem
You work on Space Station 42 and are floating through space.

Given a list `all_space_centers` locations in range where `all_space_centers[i] = [xi, yi]` represents a point on the X-Y plane  and a `number_of_centers` we want to communicate too, return the `number_of_centers` closest space_centers from our location. Our location is always guaranteed as `(0,0)` 

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).


e.g.

- 
  - Given `all_space_centers = [ [1, 1] ]`
  - and `number_of_space_centers = 1`
  - the `closest_space_centers = [ [1, 1] ] `


-
    - Given `all_space_centers = [ [-1, 2], [3, 4], [1, 1] ]`
    - and `number_of_space_centers = 1`
    - the `closest_space_centers = [ [1, 1], [-1, 2] ]`
