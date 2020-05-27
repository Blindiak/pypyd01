class GotCharacter():
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        """if you die twice! you will be back !!! same terminator"""
        if self.is_alive:
            self.is_alive = False
        else:
            self.is_alive = True


class Lanister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lanister"
        self.house_words = "Miouuws ..."

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        """if you die twice! you will be back !!! same terminator"""
        if self.is_alive:
            self.is_alive = False
        else:
            self.is_alive = True
