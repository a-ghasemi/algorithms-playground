class Window():
    Deep = 100
    def __init__(self, width = 100, height = 100):
        self.width = width
        self.height = height

    def print(self):
        print(self.__dict__)

    @staticmethod
    def create():
        return Window(10,20)

    @classmethod
    def copy(cls):
        return cls()


inst1 = Window.create()
inst1.print()
inst2 = Window.copy()
inst2.print()
