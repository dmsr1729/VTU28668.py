def calculate_total_cost(x, y):
    return x * y

t = int(input("Enter the number of test cases: "))
total_amount = 0

for _ in range(t):
    x, y = map(int, input().split())
    total_amount += calculate_total_cost(x, y)

print(total_amount)
