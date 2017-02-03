from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

MATRIX_WIDTH = 8
MATRIX_CENTRE = 3
edge = [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 57, 56, 48, 40, 32, 24, 16, 8]
length = len(edge)
ratio = length / 360.0
last_y = 3

while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]

    pitch = round(pitch, 1)
    roll = round(roll, 1)

    angle = roll
    if roll > 180:
        angle = -(360 - roll)
        
    roll_max = 24 #32
    roll_min = -24 #328
    roll_range = roll_max - roll_min

    roll_ratio = roll_range / MATRIX_WIDTH
    
    y = angle // roll_ratio
    
    y = MATRIX_CENTRE + y
    
    if y > 6:
        y = 6
    elif y < 0:
        y = 0
    print("\rRoll: {0} Pitch: {1} Angle: {2} Roll Range: {3} y: {4}".format(roll, pitch, angle, roll_range, y)),
    
    if last_y != y:
	    sense.set_pixel(0, last_y, 0, 0, 0)
	    sense.set_pixel(0, last_y + 1, 0, 0, 0)
	    
    sense.set_pixel(0, y, 255, 255, 255)
    sense.set_pixel(0, y + 1, 255, 255, 255)
    last_y = y
