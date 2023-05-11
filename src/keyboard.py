from src.item import Item


class Mix:
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value
        if not self.__language in ['EN', 'RU']:
            raise AttributeError("AttributeError: property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, Mix):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)


# print(Keyboard.__mro__)
# #
kb = Keyboard('Dark Project KD87A', 9600, 5)
print(kb.__repr__())
# kb.change_lang().change_lang()
