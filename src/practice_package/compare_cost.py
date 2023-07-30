weight1 = int(input("Enter weight1: "))
price1 = float(input("Enter price1: "))
weight2 = int(input("Enter weight2: "))
price2 = float(input("Enter price2: "))

package_1 = weight1 / price1
package_2 = weight2 / price2

if package_1 > package_2:
    print("Package 1 has a better price")
else:
    print("Package 2 has a better price")
