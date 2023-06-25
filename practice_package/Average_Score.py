n = int(input("how many element: "))
list1 = ()
for i in range(n):
    list1.append(int(input()))

sum_of_elements = sum(list1)
len_of_list = len(list1)
average = sum_of_elements/len_of_list
print("average: ", average
      )