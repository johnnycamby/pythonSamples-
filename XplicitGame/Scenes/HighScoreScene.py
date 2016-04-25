__author__ = 'johnny'

import pygame
from XplicitGame.Scenes import Scene
from XplicitGame.HighScore import HighScore
from XplicitGame.Shared.GameConstants import GameConstants


class HighScoreScene(Scene):

    def __init__(self, game):
        super(HighScoreScene, self).__init__(game)
        self.__highScoreSprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self):
        self.getGame().screen.blit(self.__highScoreSprite, (50,50))
        self.clearText()


        highScore = HighScore()

        x = 350
        y = 100

        for score in highScore.getScores():
            self.addText(score[0], x, y, size=30)
            self.addText(str(score[1]), x + 200, y, size=30)

            y += 30

        self.addText("Press F1 to start a new game", x, y + 60, size=30)
        super(HighScoreScene, self).render()

    def handleEvents(self, events):
        # pass events to parent
        super(HighScoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)

