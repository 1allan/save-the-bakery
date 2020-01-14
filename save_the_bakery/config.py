from random import randint

#General
RESOLUTION = (400, 600)
CLOCK = 120


#Entity generation
ASTEROID_GEN_INTERVAL = 600
SPECIAL_ASTEROIDS = [
    {'name': 'deathstar', 'chance': 20}
]
POWERUP_GEN_INTERVAL =  0 #set 0 to deactivate
POWERUP_ON_KILL_CHANCE = 30
POWERUPS_CHANCE = {
    'one_more_bullet': 33,
    'fire_cadence': 33,
    'spaceship_speed': 33
}


#Images
BACKGROUND_IMAGE = 'assets/background.jpg'
ASTEROID_IMAGE = 'assets/asteroid.png'
POWERUP_IMAGE = 'assets/cake.png'
BULLET_IMAGE = 'assets/bullet.png'
PLAYER_IMAGE = 'assets/spaceship.png'


#Background
BACKGROUND_POSITION = [0, 0]


#Asteroids
ASTEROID_SIZE_RANGE = (1, 3)
ASTEROID_SPEED_RANGE = (2, 4)
DEATHSTAR_FIRE_CADENCE = 800
DEATHSTAR_START_SHOOTING = 1800
DEATHSTAR_IMAGE = 'assets/deathstar.png'



#Powerups
POWERUP_SIZE = (30, 30)
POWERUP_LIST = [
    {'effect': 'one_more_bullet', 'modifier': 1},
    {'effect': 'fire_cadence', 'modifier': 50},
    {'effect': 'spaceship_speed', 'modifier': 1}
]


#Player
PLAYER_SIZE = (60, 80)
PLAYER_POSITION = [RESOLUTION[0] / 2, RESOLUTION[1] * .85]
PLAYER_HP = 3
PLAYER_SPEED = 3
PLAYER_MAX_SPEED = 8
PLAYER_BULLET_LINES = 1
PLAYER_BULLET_SPEED = 10
PLAYER_MAX_BULLETS = 3
PLAYER_BULLET_SIZE = [10, 50] 
PLAYER_FIRE_CADENCE = 400
PLAYER_MAX_FIRE_CADENCE = 1000
PLAYER_BULLET_X_POS = [
    [PLAYER_POSITION[0] + PLAYER_SIZE[0] / 2], 
    [PLAYER_POSITION[0] + 20, PLAYER_POSITION[0] + PLAYER_SIZE[0] - 20], 
    [PLAYER_POSITION[0] + 10, PLAYER_POSITION[0] + PLAYER_SIZE[0] / 2, PLAYER_POSITION[0] + PLAYER_SIZE[0] - 10]
]
PLAYER_BULLET_Y_POS = PLAYER_POSITION[1] + PLAYER_SIZE[1] / 2


#Animation lists
ANIMATIONS = {
    'explosion': ['assets/explosion0.png','assets/explosion1.png','assets/explosion2.png','assets/explosion3.png','assets/explosion4.png','assets/explosion5.png','assets/explosion6.png','assets/explosion7.png','assets/explosion8.png']
}