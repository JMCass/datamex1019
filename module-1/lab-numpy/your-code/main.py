#1. Import the NUMPY package under the name np.
import numpy as np

#2. Print the NUMPY version and the configuration.
print(np.__version__)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a=np.random.random((2,3,5))

#4. Print a.
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b=np.ones((5,2,3))

#6. Print b.
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?
a.shape

#7. Do a and b have the same size? How do you prove that in Pythoncode?
#La matriz tiene una dimension 5X2X3 mientras que 'a' tiene 2X3X5
b.shape

#8. Are you able to add a and b? Why or why not?
#No porque tienen dimensiones diferentes las matrices

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c=b.reshape((2,3,5))

print(c)

a.shape

c.shape
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d=np.add(a, c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
#es el resultado de sumar elemento por elemento de las matrices a y c
print(d)

#12. Multiply a and c. Assign the result to e.
#la matriz e es resultado de multiplicar elementos por elemento de la matriz a y c
e=np.multiply(a,c)
print(e)

#13. Does e equal to a? Why or why not?

#Las matrices son iguales en tamaño, pero los resultados no serán los mismos

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max=d.max()
print(d_max)

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_min=d.min()
print(d_min)

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_mean=np.mean(d)
print(d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f=np.empty([2,3,5],int)
print(f)

#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
#If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
#If a value equals to d_mean, assign 50 to the corresponding value in f.
#Assign 0 to the corresponding value(s) in f for d_min in d.
#Assign 100 to the corresponding value(s) in f for d_max in d.
#In the end, f should have only the following values: 0, 25, 50, 75, and 100.
#Note: you don't have to use Numpy in this question.

for e in range(len(f)):
    for i in range(len(f[e])):
           for j in range(len(f[e][i])):
                if d_min < d[e][i][j] < d_mean:
                          f[e][i][j] = 25
                elif d_mean < d[e][i][j] < d_max:
                          f[e][i][j] = 75
                elif d[e][i][j] == d_mean:
                    f[e][i][j] = 50
                elif d[e][i][j] == d_min:
                    f[e][i][j] = 0
                elif d[e][i][j] == d_max:
                    f[e][i][j] = 100

#17. Print d and f. Do you have your expected f?
print(d)

#17. Print d and f. Do you have your expected f?
print(f)

#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
#("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
#array([[[ 'D',  'D',  'D',  'B',  'D'],
 #       [ 'D',  'D',  'B',  'B',  'B'],
  #      [ 'D',  'B',  'D',  'D',  'D']],
#
 #      [[ 'B',  'B',  'B',  'B',  'E'],
  #      [ 'D',  'D',  'D',  'D',  'D'],
 #       [ 'B',  'D',   'A',  'D', 'D']]])
#Again, you don't need Numpy in this question.
g = np.empty([2, 3, 5], str)

for e in range(len(g)):
    for i in range(len(g[e])):
        for j in range(len(g[e][i])):
            if d_min < d[e][i][j] < d_mean:
                g[e][i][j] = 'B'
            elif d_mean < d[e][i][j] < d_max:
                g[e][i][j] = 'D'
            elif d[e][i][j] == d_mean:
                g[e][i][j] = 'C'
            elif d[e][i][j] == d_min:
                g[e][i][j] = 'A'
            elif d[e][i][j] == d_max:
                g[e][i][j] = 'E'

print(g)
