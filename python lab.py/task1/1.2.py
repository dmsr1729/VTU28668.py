def calculate_total_cost(x,y)
    return x*y
t = int(input("Enter number of test cases: "))

for _ in range(t):
    x, y = map(int, input().split())
    print(x // y)
