import diary as diary
import diary

from LearnPyTest.entry import Entry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__list_of_entries = []

    def lock_diary(self):
        var = self.is_locked == True

    def is_locked(self):
        return self.is_locked

    # def lock_diary(self):
    #     pass

    def unlocked_diary(self, password):
        self.validate_password(password)

    def validate_password(self, password):
        if self.password == password:
            return
        else:
            raise ValueError("Input correct information")

    def create_new_entry(self, title, body):
        entry = Entry(self.__generate_id(), title, body)
        self.__list_of_entries.append(entry)

    def find_entry_by_id(self, id):
        for entry in self.__list_of_entries:
            if entry.get_id() == id:
                return entry
        raise ValueError("Diary Not Found")

    def __generate_id(self):
        return len(self.__list_of_entries) + 1

    def delete_entry(self, id):
        entry = self.find_entry_by_id(id)
        self.__list_of_entries.remove(entry)

    def get_username(self):
        return self.username
