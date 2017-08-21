def slow_power(a, b):
   y = 1
   z = b
   while z > 0:
      y = y * a
      z = z - 1
   return y


def power(a, b):
   x = a
   y = 1
   z = b
   while z > 0:
      r = z % 2 # remainder of z / 2
      z = z // 2 # quotient of z / 2
      if r == 1:
         y = x * y
      x = x * x
   return y


