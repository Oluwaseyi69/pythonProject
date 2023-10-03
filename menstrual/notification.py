
class Notification:
    def __init__(self, notification_id, message):
        self.notification_id = notification_id
        self.message = message

    def get_notification_id(self):
        return self.notification_id

    def set_message(self, new_message):
        self.message = new_message
