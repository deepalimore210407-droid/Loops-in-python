# Even numbers
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# Sum of odd numbers
sum = 0
for i in range(1,11):
    if i % 2 != 0:
        sum += i

print("sum of odd numbers:", sum)

# Fibonacci
a = 0
b = 1
print("Fibonacci series between 0 to 50:")
print(a, end=" ")
print(b, end=" ")

while True:
    i = a + b
    if i > 50:
        break
    print(i, end=" ")
    a = b
    b = i

# String part
k = input("\nEnter the string: ")
result = ""

for i in range(len(k)):
    if i % 2 == 0:
        result += k[i]

print("result:", result)