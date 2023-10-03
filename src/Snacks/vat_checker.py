def vat():
    try:
        user_input, value = eval(input("Enter price of an item and vat: "))
        if user_input > 0:
            print((value / 100) * user_input + user_input)

    except (TypeError, NameError, KeyError, KeyboardInterrupt, ZeroDivisionError):
        print("\nplease enter a valid number")
        vat()
    except NameError:
        print("Enter a valid number")
        vat()


if __name__ == '__main__':
    print(vat())
