# general recursive tower of hanoi solution with stacks

x = [4,3,2,1] # tower of n=4 for demo
y = []
z = []
print(x, y, z)

def hanoi(a, b, c, n):
    if n == 1:
        c.append(a.pop())
        print(x, y, z)
        return
    
    hanoi(a, c, b, n-1)
    hanoi(a, b, c, 1) # recurse to base case
    hanoi(b, a, c, n-1)

hanoi(x, y, z, 4)
