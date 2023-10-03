from menstrual.notification import Notification


class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.notifications = []
        self.length = 0

    def get_user_id(self):
        return self.user_id

    def add_user(self, notification_id, message):
        notification = Notification(notification_id, message)
        self.notifications.append(notification)

    def find_user(self, user_id):
        for notification in self.notifications:
            if notification.get_notification_id() == user_id:
                return notification
        raise ValueError("Invalid Id")

    def delete_user(self, notification_id):
        user_to_delete = None
        for notification in self.notifications:
            if notification.get_notification_id() == notification_id:
                user_to_delete = notification
                break
        if user_to_delete:
            self.notifications.remove(user_to_delete)
        else:
            raise ValueError("User not found")

    def update_user(self, notification_id, new_message):
        for notification in self.notifications:
            if notification.get_notification_id() == notification_id:
                notification.set_message(new_message)
                break

    def get_cycle_length(self, date):
        if date >= 21 or date <= 35:
            date = "normal"
            return date
        else:
            raise "Enter a date within the range"
        # return (first_date + second_date + third_date) / 3

    def ovulation_period(self, date):
        period = date / 2
        first_date = period - 1
        second_date = period - 2
        return second_date
