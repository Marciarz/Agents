import pygame
import cards_operations

pygame.init()
clock = pygame.time.Clock()
clock.tick(120)
window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Agent")
pink = (99, 92, 107)
green = (20, 200, 20)
red = (255, 87, 20)
black = (10, 10, 10)
blue = (70, 125, 227)
brown = (122, 105, 35)
white = (255, 255, 255)
window.fill(pink)

class Rect(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color,card_instance):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.word = card_instance.word
        self.card_id = card_instance.card_id
        self.agent = card_instance.agent
        self.visible = card_instance.visible
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.SysFont("Arial", 25)
        self.textSurf = self.font.render(self.word, 1, white)
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.width = width
        self.height = height
        self.W = W
        self.H = H
        self.update_text()
        pygame.display.update()
    def update_text(self):
        self.image.blit(self.textSurf, [self.width / 2 - self.W / 2, self.height / 2 - self.H / 2])

    def change_value(self):
        if self.agent == 'red':
            self.image.fill(red)
        elif self.agent == 'blue':
            self.image.fill(blue)
        elif self.agent == 'black':
            self.image.fill(black)
        else:
            self.image.fill(brown)
        self.update_text()
        pygame.display.update()

run = True
all_cards = cards_operations.Generating_cards(25)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    rects = pygame.sprite.Group()

    i = 0
    x = 250
    y = 50
    while i < 25:
        i += 1
        card = Rect(x, y, 175, 125, green, all_cards[i])
        rects.add(card)
        if i % 5 == 0:
            y += 150
            x = 250
        else:
            x += 200

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        clicked_sprite = [s for s in rects if s.rect.collidepoint(pos)][0]
        clicked_sprite.change_value()
        rects.draw(window)

    rects.draw(window)

if __name__ == "__main__":
    number_of_cards = 25