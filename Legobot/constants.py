#   When possible, make values into constants so they can be easily changed throughout the code at once.
#   Constants are subject to change, so make sure to check the values to be certain that they are right.
#   Note: All constant timings are assumed to be in milliseconds unless otherwise specified.

from wallaby import *

#-------------------------------Clone Bot Definitions------------------------
# This is used to determine which robot is which based on how many color channels each bot has.

def MAIN_BOT_CHANNEL_COUNT():
    return(get_channel_count() == 3)

def CLONE_BOT_CHANNEL_COUNT():
    return(get_channel_count() == 4)  # If the bot has 4 camera channels, then it is the clone bot.

IS_MAIN_BOT = right_button() == 0 and MAIN_BOT_CHANNEL_COUNT() or left_button() == 1  # Left button for main

IS_CLONE_BOT = left_button() == 0 and CLONE_BOT_CHANNEL_COUNT() or right_button() == 1  # Right button for clone

#-------------------------------Motors, Servos, and Sensors------------------------

if IS_MAIN_BOT:
    #------------------------Motors------------------------

    # Motor Ports
    LEFT_MOTOR = 2
    RIGHT_MOTOR = 3

    # Base Motor Powers
    BASE_LM_POWER = 900
    BASE_RM_POWER = -900
    HALF_LM_POWER = BASE_LM_POWER / 2
    HALF_RM_POWER = BASE_RM_POWER / 2
    FULL_LM_POWER = BASE_LM_POWER
    FULL_RM_POWER = BASE_RM_POWER
    LFOLLOW_SMOOTH_LM_POWER = int (.7 * BASE_LM_POWER)
    LFOLLOW_SMOOTH_RM_POWER = int (.7 * BASE_RM_POWER)
    OFF = 999999

    # Motor Power Trackers
    CURRENT_LM_POWER = 0
    CURRENT_RM_POWER = 0

    # Motor Timings
    RIGHT_TURN_TIME = 900  # Need to test turn timings periodically. They change as battery charge changes, or on new boards.
    LEFT_TURN_TIME = 900
    DEFAULT_DRIVE_TIME = 500
    DEFAULT_BACKWARDS_TIME = 500
    PIVOT_RIGHT_TURN_TIME = 3580  # Turns 180 degrees. Not currently used.
    PIVOT_LEFT_TURN_TIME = 3400  # Ditto above.
    MOVEMENT_REFRESH_RATE = 30

    #-------------------------------Servos------------------------

    # Servo Limits
    MAX_SERVO_POS = 2047  # Cannot physically exceed 2047 or servo will break. Metal servos are more affected.
    MIN_SERVO_POS = 0  # Cannot physically exceed 0 or servo will break. Metal servos are more affected.

    ARM_MAX_POS = 1900
    ARM_MIN_POS = 100

    CLAW_MAX_POS = 1900
    CLAW_MIN_POS = 100

    WINDSHIELD_WIPER_MAX_POS = 1900
    WINDSHIELD_WIPER_MIN_POS = 100
    SERVO_DELAY = 500  # Time needed to move a servo (need more testing to find a good value).

    # Arm Servo
    ARM_SERVO = 2
    MAX_ARM_SERVO_POS = MAX_SERVO_POS
    MIN_ARM_SERVO_POS = MIN_SERVO_POS
    ARM_UP_POS = 1762
    ARM_DOWN_POS = 1096

    # Wiper Servo
    WINDSHIELD_WIPER_SERVO = 1
    WINDSHIELD_WIPER_LEFT_POS = 101
    WINDSHIELD_WIPER_RIGHT_POS = 1899
    WINDSHIELD_WIPER_MIDDLE_POS = 822

    # Claw Servo
    CLAW_SERVO = 0
    MAX_CLAW_SERVO_POS = MAX_SERVO_POS
    MIN_CLAW_SERVO_POS = MIN_SERVO_POS
    CLAW_OPEN_POS = 417  # Claw fingers form a 180 degree line
    CLAW_CLOSE_POS = 1298
    CLAW_TRUCK_CLOSE_POS = 1418
    CLAW_LESS_OPEN_POS = 928
    CLAW_CHECKING_POS = CLAW_CLOSE_POS

    # Micro Servo
    MICRO_SERVO = 3

    # Starting Positions
    STARTING_ARM_POS = ARM_DOWN_POS
    STARTING_CLAW_POS = CLAW_LESS_OPEN_POS
    STARTING_WINDSHIELD_WIPER_POS = WINDSHIELD_WIPER_RIGHT_POS

    LIST_OF_ALL_SERVOS = [ARM_SERVO, CLAW_SERVO, WINDSHIELD_WIPER_SERVO, MICRO_SERVO]

    #-------------------------------Sensors------------------------

    # Analog Ports
    LIGHT_SENSOR = 5
    LEFT_TOPHAT = 0
    RIGHT_TOPHAT = 1
    THIRD_TOPHAT = 4
    FOURTH_TOPHAT = 3

    # Analog Values
    LEFT_TOPHAT_BW = 721  # If more, black. If less, white.
    RIGHT_TOPHAT_BW = 785  # If more, black. If less, white.
    THIRD_TOPHAT_BW = 2083  # If more, black. If less, white.
    FOURTH_TOPHAT_BW = 2083
    LFOLLOW_REFRESH_RATE = 30  # Default amount of time before tophats check their black/white status again.

    # Digital Sensors
    RIGHT_BUMP_SENSOR = 0
    BUMP_SENSOR = 1

    # Gryo Values
    ROBOT_ANGLE = 0
    MS_SINCE_LAST_GYRO_UPDATE = 0
    LAST_GYRO_UPDATE = 0
    DEGREE_CONVERSION_RATE = 6281.8888889

    # Camera Colors
    YELLOW = 0
    RED = 1
    GREEN = 2

    # Camera Zones
    NEAR_ZONE = -1
    FAR_ZONE = 1
    BURNING_HOSPITAL = NEAR_ZONE
    SAFE_HOSPITAL = FAR_ZONE

    # PID Lfollow Values
    MAX_TOPHAT_VALUE_RIGHT = 3200
    MIN_TOPHAT_VALUE_RIGHT = 158
    MAX_TOPHAT_VALUE_LEFT = 3200
    MIN_TOPHAT_VALUE_LEFT = 158  # These values dont do anything unless calib command doesnt work right.
    KP = 10
    KI = 0.161
    KD = 1
    KP_SAFE = 7
    KI_SAFE = 0.061
    KD_SAFE = 1

    # Miscellaneous Values
    SAFETY_TIME = 15000  # This is the while loop time limit that ensures we don't have an infinite loop.
    SAFETY_TIME_NO_STOP = SAFETY_TIME + 1
    BASE_TIME = 9999
    BASE_VALUE = 99999
    START_TIME = 0
    SECONDS_DELAY = 0

else:  # Clone Bot ----------------------------------------------------------------------------------------------------------------
    # ------------------------Clone Motors------------------------
    # Clone Motor Ports
    LEFT_MOTOR = 2
    RIGHT_MOTOR = 3

    # Clone Base Motor Powers
    BASE_LM_POWER = 900
    BASE_RM_POWER = -900
    HALF_LM_POWER = BASE_LM_POWER / 2
    HALF_RM_POWER = BASE_RM_POWER / 2
    FULL_LM_POWER = BASE_LM_POWER
    FULL_RM_POWER = BASE_RM_POWER
    LFOLLOW_SMOOTH_LM_POWER = int(.7 * BASE_LM_POWER)
    LFOLLOW_SMOOTH_RM_POWER = int(.7 * BASE_RM_POWER)
    OFF = 999999

    # Clone Motor Power Trackers
    CURRENT_LM_POWER = 0
    CURRENT_RM_POWER = 0

    # Clone Motor Timings
    RIGHT_TURN_TIME = 900  # Need to test turn timings periodically. They change as battery charge changes, or on new boards.
    LEFT_TURN_TIME = 900
    DEFAULT_DRIVE_TIME = 500
    DEFAULT_BACKWARDS_TIME = 500
    PIVOT_RIGHT_TURN_TIME = 3580  # Turns 180 degrees. Not currently used.
    PIVOT_LEFT_TURN_TIME = 3400  # Ditto above.
    MOVEMENT_REFRESH_RATE = 30

    # -------------------------------Clone Servos------------------------
    # Clone Servo Limits
    MAX_SERVO_POS = 1900  # Cannot physically exceed 2047 or servo will break. Metal servos are more affected.
    MIN_SERVO_POS = 100  # Cannot physically exceed 0 or servo will break. Metal servos are more affected.
    SERVO_DELAY = 500  # Time needed to move a servo (need more testing to find a good value).

    # Clone Arm Servo
    ARM_SERVO = 2
    MAX_ARM_SERVO_POS = MAX_SERVO_POS
    MIN_ARM_SERVO_POS = MIN_SERVO_POS
    ARM_UP_POS = 1762
    ARM_DOWN_POS = 1096

    # Clone Wiper Servo
    WINDSHIELD_WIPER_SERVO = 1
    WINDSHIELD_WIPER_LEFT_POS = 101
    WINDSHIELD_WIPER_RIGHT_POS = 1899
    WINDSHIELD_WIPER_MIDDLE_POS = 1100

    # Clone Claw Servo
    CLAW_SERVO = 0
    MAX_CLAW_SERVO_POS = MAX_SERVO_POS
    MIN_CLAW_SERVO_POS = MIN_SERVO_POS
    CLAW_OPEN_POS = 417  # Claw fingers form a 180 degree line
    CLAW_CLOSE_POS = 1298
    CLAW_TRUCK_CLOSE_POS = 1418
    CLAW_LESS_OPEN_POS = 928
    CLAW_CHECKING_POS = CLAW_CLOSE_POS

    # Clone Micro Servo
    MICRO_SERVO = 3

    # Clone Starting Positions
    STARTING_ARM_POS = ARM_DOWN_POS
    STARTING_CLAW_POS = CLAW_LESS_OPEN_POS
    STARTING_WINDSHIELD_WIPER_POS = WINDSHIELD_WIPER_MIDDLE_POS

    # -------------------------------Clone Sensors------------------------
    # Clone Analog Ports
    LIGHT_SENSOR = 5
    LEFT_TOPHAT = 0
    RIGHT_TOPHAT = 1
    THIRD_TOPHAT = 4
    FOURTH_TOPHAT = 3

    # Clone Analog Values
    LEFT_TOPHAT_BW = 721  # If more, black. If less, white.
    RIGHT_TOPHAT_BW = 785  # If more, black. If less, white.
    THIRD_TOPHAT_BW = 2083  # If more, black. If less, white.
    FOURTH_TOPHAT_BW = 2083
    LFOLLOW_REFRESH_RATE = 30  # Default amount of time before tophats check their black/white status again.

    # Clone Digital Sensors
    RIGHT_BUMP_SENSOR = 0
    BUMP_SENSOR = 1

    # Clone Gryo Values
    ROBOT_ANGLE = 0
    MS_SINCE_LAST_GYRO_UPDATE = 0
    LAST_GYRO_UPDATE = 0
    DEGREE_CONVERSION_RATE = 6281.8888889

    # Clone Camera Colors
    YELLOW = 0
    RED = 1
    GREEN = 2

    # Clone Camera Zones
    NEAR_ZONE = -1
    FAR_ZONE = 1
    BURNING_HOSPITAL = NEAR_ZONE
    SAFE_HOSPITAL = FAR_ZONE

    # Clone PID Lfollow Values
    MAX_TOPHAT_VALUE_RIGHT = 3200
    MIN_TOPHAT_VALUE_RIGHT = 158
    MAX_TOPHAT_VALUE_LEFT = 3200
    MIN_TOPHAT_VALUE_LEFT = 158  # These values dont do anything unless calib command doesnt work right.
    KP = 10
    KI = 0.161
    KD = 1
    KP_SAFE = 7
    KI_SAFE = 0.061
    KD_SAFE = 1

    # Clone Miscellaneous Values
    SAFETY_TIME = 15000  # This is the while loop time limit that ensures we don't have an infinite loop.
    SAFETY_TIME_NO_STOP = SAFETY_TIME + 1
    BASE_TIME = 9999
    BASE_VALUE = 99999
    START_TIME = 0
    SECONDS_DELAY = 0