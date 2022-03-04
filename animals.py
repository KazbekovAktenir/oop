class Dog:
    def __init__(self, weight, voiceText):
        self.weight = weight
        self.voiceText = voiceText

    def voice(self):
        print(f"{self.voiceText}")


rex = Dog(25, "gaf gaf!")
rex.voice()


class Cat:
    def __init__(self, height, text):
        self.height = height
        self.text = text

    def voice(self):
        print(f"{self.text}")


tom = Cat(120, "meow")
tom.voice()


class Cow:
    def __init__(self, milk, voiceCow):
        self.milk = milk
        self.voiceCow = voiceCow

    def voice(self):
        print(f"{self.voiceCow}")


mumu = Cow(10, "muuu")
mumu.voice()


class Bear:
    def __init__(self, bearCub, voiceBear):
        self.bearCub = bearCub
        self.voiceBear = voiceBear

    def voice(self):
        print(f"{self.voiceBear}")


balu = Bear(4, "aaa")
balu.voice()
