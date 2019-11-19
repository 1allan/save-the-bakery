from random import randint

#General
RESOLUTION = (400, 600)
CLOCK = 120

#Entity generation
ASTEROID_GEN_INTERVAL = 800
POWERUP_GEN_INTERVAL = 5000

#Images
ASTEROID_IMAGE = 'assets/asteroid.png'
POWERUP_IMAGE = 'assets/cake.png'
BULLET_IMAGE = 'assets/bullet.png'
PLAYER_IMAGE = 'assets/spaceship.png'

#Asteroids
ASTEROID_SIZE_RANGE = (1, 3)

#Powerups
POWERUP_SIZE = (30, 30)
POWERUP_LIST = [
    {'effect': 'one_more_bullet', 'modifier': 1}, 
    {'effect': 'fire_cadence', 'modifier': 10},
    {'effect': 'spaceship_speed', 'modifier': 3}
]

#Player
PLAYER_SIZE = (60, 80)
PLAYER_LOCATION = [RESOLUTION[0] / 2, RESOLUTION[1] * .85]
PLAYER_LIFES = 3
PLAYER_SPEED = 2
PLAYER_MAX_SPEED = 8
PLAYER_BULLETS = [[]]
PLAYER_BULLET_SPEED = 10
PLAYER_MAX_BULLETS = 3
PLAYER_BULLET_SIZE = [10, 50] 
PLAYER_FIRE_CADENCE = 600
PLAYER_MAX_FIRE_CADENCE = 1000
PLAYER_BULLET_X_POS = [
    [PLAYER_LOCATION[0] + PLAYER_SIZE[0] / 2], 
    [PLAYER_LOCATION[0] + 20, PLAYER_LOCATION[0] + PLAYER_SIZE[0] - 20], 
    [PLAYER_LOCATION[0] + 10, PLAYER_LOCATION[0] + PLAYER_SIZE[0] / 2, PLAYER_LOCATION[0] + PLAYER_SIZE[0] - 10]
]
PLAYER_BULLET_Y_POS = PLAYER_LOCATION[1] + PLAYER_SIZE[1] / 2

