number: int(input("enter number: "))
list1 = []
for i in range(20):
    list1.append(int(input()))

sum_of_elements = sum(list1)
average = sum_of_elements / number
print("Average: ", average)