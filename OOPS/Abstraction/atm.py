from abc import ABC, abstractmethod
class Electronics(ABC):
    @abstractmethod
    def play_video(self):
        pass
class Laptop(Electronics):
    def play_video(self):
        print("Press play button to play video on Laptop.")
class Mobile(Electronics):
    def play_video(self):
        print("Press play button to play video on Mobile.")
p=Laptop();
p.play_video();

m=Mobile();
m.play_video();