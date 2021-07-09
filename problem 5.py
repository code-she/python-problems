#The provided code stub reads and integer, , from STDIN. For all non-negative integers i<n, print i^2 .
 #The range() function

#The range function is a built in function that returns a series of numbers. At a minimum, it needs one integer parameter.

#Given one parameter,n , it returns integer values from 0 to n-1 . For example, range(5) returns the numbers 0  through 4  in sequence.
#Finally, you can add an increment value as the third argument. For example, range(5, -1, -1) produces the descending sequence from 5 through 0 and range(0, 5, 2) produces 0,2 ,4
 #. If you are going to provide a step value, you must also include a start value.

 if __name__ == '__main__':
    n = int(input())
    n<=1 and n>=20

for i in range(0,n):
    print(i*i)
    
