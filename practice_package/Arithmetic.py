total_input = 0
product = 1
largest = 0
smallest = 0

for x in range(1, 5):

     number = int(input("Enter a number: "))
     total_input += number
     product *= number
     if number>largest:
         largest = number
     if number < smallest:
        smallest = number
     average = total_input / x
print("Sum    Average    Product    Smallest    Largest")
print(total_input,"\t\t", average,"\t\t",   product,"\t\t", smallest,"\t\t", largest,"\t\t")



# for x in range (1, 10):
#     print()
#     for y in range (1, 9):
#         print(f"{x} x {y} = {x*y}", end="\t\t")