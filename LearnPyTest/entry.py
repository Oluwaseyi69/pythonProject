class Entry:

    def __init__(self, id,title, body):
        self.__id = id
        self.__title = title
        self.__body = body

    @property
    def id(self):
        return self.id
    @id.setter
    def id (self, __id):
        self.id = __id

    def set_body(self, body):
        self.__body = body

    def set_title(self, title):
        self.__title = title

    def get_entry(self):
        return f'{self.__id} {self.__title} {self.__body}'

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body
