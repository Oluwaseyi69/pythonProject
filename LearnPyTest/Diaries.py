from typing import List

from LearnPyTest.Diary import Diary


# class Diary:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

class Diaries:
    def __init__(self):
        self.diaries = []

    def add_diary(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary
        raise ValueError("Input a valid Diary")

    def delete_diary(self, username, password):
        diary = Diary(username, password)
        self.diaries.remove(diary)
