def is_pythagorean_triplet(a, b, c):
    x, y, z = sorted([a, b, c])
    return x*x + y*y == z*z


print(is_pythagorean_triplet(3, 4, 5))
print(is_pythagorean_triplet(3, 8, 5))  

 

