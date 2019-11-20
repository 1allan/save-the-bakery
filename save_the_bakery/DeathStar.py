from Asteroid import Asteroid

class DeathStar(Asteroid):

    def __init__(self, position):
        Asteroid.__init__(position)
    
    def update(self):
        self.rect.top -= 5
        screen.blit(self.image, self.rect)