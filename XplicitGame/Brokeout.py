__author__ = 'johnny'


import pygame
from XplicitGame import *
from XplicitGame.Scenes import *
from XplicitGame.Shared import GameConstants


class Breakout:

# ============================= Constructor =========================
    def __init__(self):
        self.__lives = 1
        self.__score = 0

        self.__level = Level(self)
        # load the game
        #self.__level.loadRandom()
        self.__level.load(0)

        # start-position (center of the screen)
        # '1' => height, '0' => width
        self.__pad = Pad((GameConstants.SCREEN_SIZE[0]/2, GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1]), pygame.image.load(GameConstants.SPRITE_PAD))
        # Is a collection the one can append more values to
        self.__balls = [
            Ball((400, 400), pygame.image.load(GameConstants.SPRITE_BALL), self)
            #Ball((300, 400), pygame.image.load(GameConstants.SPRITE_BALL), self),
            #Ball((200, 400), pygame.image.load(GameConstants.SPRITE_BALL), self),
            #Ball((100, 400), pygame.image.load(GameConstants.SPRITE_BALL), self)
        ]

        # initialize pygame
        pygame.init()
        # initialize mixer
        pygame.mixer.init()
        pygame.display.set_caption("Game programming with Python & PyGame")

        self.__clock = pygame.time.Clock()

        # load screen
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)
        # disable mouse
        pygame.mouse.set_visible(0)

        # define scenes :: using a tuple, one cannot add values to a tuple
        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighScoreScene(self),
            MenuScene(self)
        )

        self.__currentScene = 3

        # sounds tuple
        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_LIFE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_SPEED),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_WALL),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_PAD)
        )

    def start(self):
        # game loop
        while 1:
            self.__clock.tick(100)
            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLives(self):
        return self.__lives

    def getBalls(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    def reduceLives(self):
        self.__lives -=1

    def increaseLives(self):
        self.__lives += 1

    def reset(self):
        self.__lives = 5
        self.__score = 0
        self.__level.load(0)


Breakout().start()