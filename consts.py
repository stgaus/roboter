class Consts():

    IMG_WIDTH = 640
    IMG_HEIGHT = 480
    CENTER_TOLERANCE = 13
    DISTANCE_FOR_CLOSE_CONTOURS = 60
    SEEN_ANIMAL_COUNTER = 3
    
    TIME_TO_GRAB = 3
    TIME_TO_LAST_IR_TICK = 500000
    TIME_TO_DRIVE_INTO_TARGET = 1

    #normal Speed:
    MOTOR_WHEELS_FREQUENCY = 21000
    MOTOR_WHEELS_DUTYCYLCE = 210000
    #Speed when animal is on screen:
    MOTOR_WHEELS_FREQUENCY_SLOW = 12000
    MOTOR_WHEELS_DUTYCYLCE_SLOW = 190000
    #Speed to drive into target:
    MOTOR_WHEELS_FREQUENCY_TARGET = 100000
    MOTOR_WHEELS_DUTYCYLCE_TARGET = 250000
    #Speed for one wheel (left or right) while steering:
    MOTOR_WHEELS_FREQUENCY_STEER = 34000
    MOTOR_WHEELS_DUTYCYLCE_STEER = 350000
    
    MOTOR_WHEELS_FREQUENCY_END = 100000
    MOTOR_WHEELS_DUTYCYLCE_END = 250000

    #correcting Speed:
    MOTOR_WHEELS_FREQUENCY_CORRECT = 100000
    MOTOR_WHEELS_DUTYCYLCE_CORRECT = 250000

    GPIO_IR_SENSOR_LEFT = 22
    GPIO_IR_SENSOR_RIGHT = 24
