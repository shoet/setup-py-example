from ._base import MyBase

class MyManager(MyBase):
    def __init__(self) -> None:
        super().__init__()

    def call(self):
        print(self.__class__)