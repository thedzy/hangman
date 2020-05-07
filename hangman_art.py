
"""
Create your own hangman art here.
Add the characters in the shaders you wish to use

Create as many objects as you want each will increase the score by 1.
Include the objects in the objects array

Each object is a matrix of shaders.  Trailing 0's are not necessary.  Size is not set or limited
"""


# Define characters that correspond to the arrays, in conflicts with objects the highest value is taken
shaders = [' ', '▄', '▀', '█', ' ']

# Define parts of the body
gallows = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [3, 3, 0, 0, 0, 1, 3, 3, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
           [3, 3, 0, 1, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
           [3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
           [3, 3, 2],
           [3, 3],
           [3, 3],
           [3, 3],
           [3, 3],
           [3, 3],
           [3, 3],
           [3, 3],
           [3, 3],
           [3, 3],
           [3, 3]
           ]

head = [[], [],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 4, 4, 2, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 4, 1, 3, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0],
        ]

arm_right = [[], [], [], [], [],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 2, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0],
             ]

arm_left = [[], [], [], [], [],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
            ]

body = [[], [], [], [], [],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1],
        ]

leg_right =[[], [], [], [], [], [], [], [], [], [],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2]
            ]

leg_left =[[], [], [], [], [], [], [], [], [], [],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
           ]

# Define the order of the parts
objects = [gallows, head, body, arm_right, arm_left, leg_right, leg_left]