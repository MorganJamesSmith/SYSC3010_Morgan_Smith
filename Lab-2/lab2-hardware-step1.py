from sense_hat import SenseHat
from sense_hat import ACTION_PRESSED

s = SenseHat()
s.low_light = True

blue = (0, 0, 255)
pink = (255,105, 180)
nothing = (0, 0, 0)

def letter_M():
    P = pink
    O = nothing
    logo = [
    P, P, O, O, O, O, P, P,
    P, P, P, O, O, P, P, P,
    P, P, P, O, O, P, P, P,
    P, P, O, P, P, O, P, P,
    P, P, O, P, P, O, P, P,
    P, P, O, O, O, O, P, P,
    P, P, O, O, O, O, P, P,
    P, P, O, O, O, O, P, P,
    ]
    return logo

def letter_S():
    B = blue
    O = nothing
    logo = [
    O, B, B, B, B, B, B, O,
    B, B, B, B, B, B, B, B,
    B, B, O, O, O, O, O, O,
    B, B, B, B, B, B, B, O,
    O, B, B, B, B, B, B, B,
    O, O, O, O, O, O, B, B,
    B, B, B, B, B, B, B, B,
    O, B, B, B, B, B, B, O,
    ]
    return logo


images = [letter_M, letter_S]
count = 1

s.set_pixels(letter_M())
while True:
    events = s.stick.get_events()
    if events:
        for e in events:
            if e.action == ACTION_PRESSED:
                s.set_pixels(images[count % len(images)]())
                count += 1
