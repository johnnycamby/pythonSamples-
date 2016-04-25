__author__ = 'johnny'

from XplicitGame.Shared import GameObject
from XplicitGame.Shared import GameConstants

'''
 - Inherits from GameObject
'''
class Brick(GameObject):

    def __init__(self, position, sprite, game):
        # private field
        self.__game = game
        self.__hitPoints = 100
        self.__lives = 1

        # set position and sprite on the game object thus parent class :: so make a call to the base-class
        super(Brick, self).__init__(position, GameConstants.BRICK_SIZE, sprite)

    def getGame(self):
        return self.__game

    def isDestroyed(self):
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitPoints

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        return GameConstants.SOUND_HIT_BRICK