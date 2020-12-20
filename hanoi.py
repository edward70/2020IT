# general recursive tower of hanoi solution with stacks

def solve(n):
    # stacks xyz
    x = list(reversed(range(1, n + 1)))
    y = []
    z = []
    print(x, y, z)

    def hanoi(a, b, c, n2 = n):
        if n2 == 1:
            c.append(a.pop())
            print(x, y, z)
            return
        
        hanoi(a, c, b, n2 - 1)
        hanoi(a, b, c, 1) # recurse to base case
        hanoi(b, a, c, n2 - 1)

    hanoi(x, y, z)

solve(4) # n=4 for demo
