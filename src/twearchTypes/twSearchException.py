#Generic class to handle exceptions

import exceptions

class twSearchException(exceptions.Exception):
    def __init__(self, Message):
        self.__message = Message

    def __str__(self):
        print "", self.__message    
