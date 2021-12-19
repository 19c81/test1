import pygame
import sys
import random

from pygame.locals import *


# 1.定义颜色：
# ①：经验
greenColor = pygame.Color(0, 255, 0)
# ②：贪吃蛇
blueColor = pygame.Color(0, 255, 255)
# ③：背景
blackColor = pygame.Color(0, 0, 0)

# 2.定义游戏结束


def gameover():
    pygame.quit()
    sys.exit()


# 3.实现工作方式
def main():

    # ①初始化Pygame
    pygame.init()

    # ②游戏速度
    fpsCock = pygame.time.Clock()

    # ③创建pygame显示层
    playsurface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('贪吃蛇')
    pygame.display.flip()

    # ④初始变量
    #
    snakeposition = [100, 100]
    #
    snakeBody = [[100, 100], [80, 100], [60, 100]]
    #
    targetPosition = [300, 300]
    #
    targetflag = 1
    #
    direction = 'right'
    #
    changeDirection = direction

    # ⑤pygame所有事件要实时循环
    while True:

        for event in pygame.event():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                # 判断键盘事件
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
        # 确定方向
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up':
            direction = changeDirection
        if changeDirection == 'right':
            direction = changeDirection
        if changeDirection == 'down':
            direction = changeDirection

        # 根据方向确定蛇头
        if direction == 'right':
            snakeposition[0] += 20
        if direction == 'left':
            snakeposition[0] -= 20
        if direction == 'up':
            snakeposition[1] -= 20
        if direction == 'down':
            snakeposition[1] += 20

        # 增加蛇长
        snakeBody.insert(0, list(snakeposition))
        if snakeposition[0] == targetPosition[0] and snakeposition[1] == targetPosition[1]:
            targetflag = 0
        else:
            snakeBody.pop()

        if targetflag == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)

            targetPosition = [int(x*20), int(y*20)]
            targetflag = 1

        playsurface.fill(blackColor)

        for position in snakeBody:
            pygame.draw.rect(playsurface, blueColor, Rect(
                position[0], position[1], 20, 20))
            pygame.draw.rect(playsurface, greenColor, Rect(
                targetPosition[0], targetPosition[1], 20, 20))

        # 更新显示
        pygame.display.flip()

        # 判断是否结束
        if snakeposition[0] > 620 or snakeposition[0] < 0:
            gameover()
        elif snakeposition[1] > 460 or snakeposition[1] < 0:
            gameover()

        fpsCock.tick(6)


if __name__ == '__mian__':
    main()
