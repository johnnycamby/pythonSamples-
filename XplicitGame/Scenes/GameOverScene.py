__author__ = 'johnny'
import pygame
from XplicitGame.Scenes import Scene
from XplicitGame.Shared import *
from XplicitGame.HighScore import HighScore

class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)

        self.__playerName = ""
        self.__highScoreSprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)


    def render(self):

        self.getGame().screen.blit(self.__highScoreSprite, (50,50))


        self.clearText()
        self.addText("Your name: ", 300, 200, size=30)
        self.addText(self.__playerName, 420, 200, size=30)
        super(GameOverScene, self).render()

    def handleEvents(self, events):
        # pass events to parent
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    game = self.getGame()
                    HighScore().add(self.__playerName, game.getScore())
                    game.reset()
                    game.changeScene(GameConstants.HIGHSCORE_SCENE)

                elif event.key >= 65 and event.key <= 122:
                    self.__playerName += chr(event.key)

                if event.key == pygame.K_F1:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)


