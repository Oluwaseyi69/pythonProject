# from diary import diary
#
#
# class Diaries:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     diaries = []
#
#     def add_diary(self, username, password):
#         if self.username == username and self.password == password:
#             self.diaries.append(diary)
#
#         else:
#             raise
#
#
#     def find_by_username(self, username):
#         for entry in self.diaries:
#             if entry.get_username() == username:
#                 return entry
#
#         raise ValueError("Diary not found")
#
#
#
#
# class Diary:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
# class DiaryManager:
#     def __init__(self):
#         self.diaries = []
#
#     def add_diary(self, username, password):
#         diary = Diary(username, password)
#         self.diaries.append(diary)
#
#


from typing import List

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Diaries:
    def __init__(self):
        self.diaries = []

    def add_diary(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.username == username:
                return diary
        raise ValueError("Input a valid Diary")

    def delete_diary(self, username, password):
        diary = Diary(username, password)
        self.diaries.remove(diary)
