__author__ = 'johnny'

import pygame
from XplicitGame.Scenes.Scene import Scene
from XplicitGame.Shared import *

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()


        game = self.getGame()
        level = game.getLevel()
        pad = game.getPad()
        balls = game.getBalls()

        if level.getAmountOfBricksLeft() <= 0:
            for ball in balls:
                ball.setMotion(0)

            level.loadNextLevel()


        if game.getLives() <= 0:
            game.playSound(GameConstants.SOUND_GAMEOVER)
            game.changeScene(GameConstants.GAMEOVER_SCENE)



        for ball in balls:
            for ball2 in balls:
                if ball != ball2 and ball.intersects(ball2):
                    ball.changeDirection(ball2)

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick):
                    game.playSound(brick.getHitSound())
                    brick.hit()
                    level.brickHit()
                    game.increaseScore(brick.getHitPoints())
                    ball.changeDirection(brick)
                    #print("intersected")
                    break

            if ball.intersects(pad):
                game.playSound(GameConstants.SOUND_HIT_PAD)
                ball.changeDirection(pad)

            ball.updatePosition()

            if ball.isBallDead():
                ball.setMotion(0)
                game.reduceLives()

            game.screen.blit(ball.getSprite(), ball.getPosition())

        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())


        # stick the pad at the bottom of the screen based on changing the x-position
        pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1]))
        game.screen.blit(pad.getSprite(), pad.getPosition())

        self.clearText()

        self.addText("Your score: " + str(game.getScore()), x = 0, y = GameConstants.SCREEN_SIZE[1] - 60, size = 30)
        self.addText("Lives: " + str(game.getLives()), x = 0, y = GameConstants.SCREEN_SIZE[1] - 30, size = 30)


    def handleEvents(self, events):
        # pass events to parent
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBalls():
                    ball.setMotion(1)



