import pygame
from card import Card
import cards_operations
from map import Generate_map

pink = (99, 92, 107)
green = (20, 200, 20)
red = (255, 87, 20)
black = (10, 10, 10)
blue = (70, 125, 227)
brown = (122, 105, 35)
white = (255, 255, 255)
light_blue = (0, 102, 153)

class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, card_instance):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.word = card_instance.word
        self.card_id = card_instance.card_id
        self.agent = card_instance.agent
        self.is_reset = card_instance.is_reset
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

def Cards_reset(game_number):
    all_cards = cards_operations.Generating_cards(25)
    reset_button = Card(26, 'RESET', 'grey', True)
    all_cards_rect = pygame.sprite.Group()

    i = 0
    x = 250
    y = 50

    while i < 25:
        i += 1
        card = Rect(x, y, 175, 125, green, all_cards[i])
        all_cards_rect.add(card)
        if i % 5 == 0:
            y += 150
            x = 250
        else:
            x += 200

    map = []
    row = []

    for card_object in all_cards_rect:
        if len(row) == 5:
            map.append(row)
            row = []
            row.append(card_object.agent)
        else:
            row.append(card_object.agent)
    map.append(row)

    Generate_map(map, game_number)

    all_cards_rect.add(Rect(650, 800, 175, 70, light_blue, reset_button))
    return all_cards_rect


def Run_game():
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(120)

    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Agent")
    window.fill(pink)
    game_number = 1
    rects = Cards_reset(game_number)

    rects.draw(window)
    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprite = [s for s in rects if s.rect.collidepoint(pos)]
                if clicked_sprite != []:
                    if clicked_sprite[0].is_reset:
                        game_number += 1
                        rects = Cards_reset(game_number)
                        rects.draw(window)
                        pygame.display.update()
                    else:
                        clicked_sprite[0].change_value()
                        rects.draw(window)


        rects.draw(window)
        pygame.display.update()
