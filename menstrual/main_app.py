from menstrual.user_class import User


def main():
    # Create a User instance
    user = User(1, "Seyi", "email@example.com", "password")

    while True:
        print("\nMenu:")
        print("1. Add Symptoms")
        print("2. Delete Symptoms")
        print("3. Update Symptoms")
        print("4. Get Cycle Length")
        print("5. Get Ovulation Period")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            notification_id = int(input("Enter Notification ID: "))
            message = input("Enter Message: ")
            user.add_user(notification_id, message)
            print("Notification added successfully!")

        elif choice == '2':
            notification_id = int(input("Enter Notification ID to delete: "))
            try:
                user.delete_user(notification_id)
                print("Notification deleted successfully!")
            except ValueError as error:
                print(error)

        elif choice == '3':
            notification_id = int(input("Enter Notification ID to update: "))
            message = input("Enter new Message: ")
            try:
                user.update_user(notification_id, message)
                print("Notification updated successfully!")
            except ValueError as error:
                print(error)

        elif choice == '4':
            date = int(input("Enter date:"))
            cycle_length = user.get_cycle_length(date)

            print(f"The cycle length is: {cycle_length}")

        elif choice == '5':
            date = int(input("Enter Date: "))
            ovulation_period = user.ovulation_period(date)
            print(f"The ovulation period is: {ovulation_period}")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please enter a valid option (1-6).")


if __name__ == "__main__":
    main()
