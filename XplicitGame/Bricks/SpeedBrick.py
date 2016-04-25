__author__ = 'johnny'

__author__ = 'johnny'

from XplicitGame.Bricks import Brick
from XplicitGame.Shared.GameConstants import GameConstants

class SpeedBrick(Brick):

    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.getGame()

        for ball in game.Balls():
            ball.setSpeed(ball.getSpeed() + 1)

        super(SpeedBrick, self).hit()

    def getHitSound(self):
        return GameConstants.SOUND_HIT_BRICK_SPEED
