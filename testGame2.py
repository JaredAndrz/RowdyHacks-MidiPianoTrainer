import pygame
import pygame.midi
from pygame.locals import *
import time
import random
from time import sleep
from threading import Thread


pygame.init()
pygame.fastevent.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post
start_time = time.time()
totalTime = []


pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (128,128,128)

#ADDED DISPLAY
yellow = (255,255,0)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Correct Keys: " + str(len(totalTime)), True, yellow, gray)
textRect = text.get_rect()
textRect.center = (0, 20)


#display data
display_width = 740
display_height = 800

#FINAL
bigFont = pygame.font.Font('freesansbold.ttf', 128)
textNote = bigFont.render("KEY", True, green, gray)
textNoteRect = textNote.get_rect()
textNoteRect.center = (display_width/2, display_height/2)

#keyboard position
keyboardXPosition = 25
keyboardYPosition = 625
keyLengthLong = 150
keyLengthShort = 90
keyWidthLong = 40
keyWidthShort = 30
positions_blackKey = [55, 105, 205, 255, 305, 405, 455, 555, 605, 655]
note_xValue_dict = {48:keyboardXPosition,
                 49:55,
                 50:keyboardXPosition + 50,
                 51:105,
                 52:keyboardXPosition + 100,
                 53:keyboardXPosition + 150,
                 54:205,
                 55:keyboardXPosition + 200,
                 56:255,
                 57:keyboardXPosition + 250,
                 58:305,
                 59:keyboardXPosition + 300,
                 60:keyboardXPosition + 350,
                 61:405,
                 62:keyboardXPosition + 400,
                 63:455,
                 64:keyboardXPosition + 450,
                 65:keyboardXPosition + 500,
                 66:555,
                 67:keyboardXPosition + 550,
                 68:605,
                 69:keyboardXPosition + 600,
                 70:655,
                 71:keyboardXPosition + 650}
xValue_note_dict = dict((y,x) for x,y in note_xValue_dict.items())
#print(xValue_note_dict.keys(), xValue_note_dict.values())

whichKey = 0
keyPressed = 0



#key colors
longKeyReleaseColor = white
shortKeyReleaseColor = black
longKeyPressColor = green
shortKeyPressColor = blue

pygame.display.set_caption("midi test")
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

counts_keys = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
counts_pads = [0,0,0,0,0,0,0,0]

note_names = {48:'C',
              49:'C#',
              50:'D',
              51:'D#',
              52:'E',
              53:'F',
              54:'F#',
              55:'G',
              56:'G#',
              57:'A',
              58:'A#',
              59:'B',
              60:'C',
              61:'C#',
              62:'D',
              63:'D#',
              64:'E',
              65:'F',
              66:'F#',
              67:'G',
              68:'G#',
              69:'A',
              70:'A#',
              71:'B'}

def endGame():
    print("Training Complete")
    #ADDED DISPLAY
    reactionTime = 0
    for x in totalTime:
        reactionTime = reactionTime + x
    #print("Reaction Time = ", reactionTime/len(totalTime), "sec")
    #print("Correct keys = ", len(totalTime) - 1)

    if len(totalTime) == 1:
        text = font.render(("Reaction Time = N/A "), True, yellow, gray)
        text2 = font.render("Correct keys = " + str(len(totalTime) - 1), True, yellow, gray)
    else:
        text = font.render("Reaction Time = " + str(reactionTime/len(totalTime) - 1) + "sec", True, yellow, gray)
        text2 = font.render("Correct keys = " + str(len(totalTime) - 1), True, yellow, gray)
    screen.blit(text, (0,0))
    screen.blit(text2, (0,30))
    pygame.display.update()
    time.sleep(5)
    return True

def blocks(blockX, blockY, blockW, blockH, color):
    pygame.draw.rect(screen, color, [blockX, blockY, blockW, blockH])

def drawKeyboard(midiNote, midiEvent):
        #
        # draw keyboard background
        #

    pygame.draw.rect(screen, red, [0,615,740,185])

        #
        # draw keyboard background
        #

    if midiNote == 48 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 50 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 50,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 50,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 52 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 100,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 100,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 53 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 150,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 150,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 55 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 200,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 200,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 57 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 250,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 250,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 59 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 300,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 300,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 60 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 350,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 350,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 62 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 400,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 400,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 64 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 450,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 450,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 65 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 500,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 500,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 67 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 550,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 550,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 69 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 600,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 600,keyboardYPosition,keyWidthLong,keyLengthLong))

    if midiNote == 71 and midiEvent != 0:
        pygame.draw.rect(screen,longKeyPressColor,(keyboardXPosition + 650,keyboardYPosition,keyWidthLong,keyLengthLong))
    else:
        pygame.draw.rect(screen,longKeyReleaseColor,(keyboardXPosition + 650,keyboardYPosition,keyWidthLong,keyLengthLong))

        #
        #Begin short keys
        #

    if midiNote == 49 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 30,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 30,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 51 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 80,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 80,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 54 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 180,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 180,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 56 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 230,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 230,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 58 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 280,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 280,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 61 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 380,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 380,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 63 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 430,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 430,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 66 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 530,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 530,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 68 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 580,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 580,keyboardYPosition,keyWidthShort,keyLengthShort))

    if midiNote == 70 and midiEvent != 0:
        pygame.draw.rect(screen,shortKeyPressColor,(keyboardXPosition + 630,keyboardYPosition,keyWidthShort,keyLengthShort))
    else:
        pygame.draw.rect(screen,shortKeyReleaseColor,(keyboardXPosition + 630,keyboardYPosition,keyWidthShort,keyLengthShort))


def midiCounter(counts_keys, counnts_pads, midi_event):
    detectPress(midi_event)

def detectPress(midi_event):
    if(midi_event[0][0][0] == 144 and not(midi_event[0][0][1] == 40 or midi_event[0][0][1] == 38 or midi_event[0][0][1] == 46 or midi_event[0][0][1] == 44 or midi_event[0][0][1] == 37 or midi_event[0][0][1] == 36 or midi_event[0][0][1] == 42 or midi_event[0][0][1] == 54)):
        print("my midi note is " + str(midi_events[0][0][1]))
        counts_keys[midi_events[0][0][1] - 48] += 1
        print(counts_keys)
    elif(midi_event[0][0][1] == 40 or midi_event[0][0][1] == 38 or midi_event[0][0][1] == 46 or midi_event[0][0][1] == 44 or midi_event[0][0][1] == 37 or midi_event[0][0][1] == 36 or midi_event[0][0][1] == 42 or midi_event[0][0][1] == 54):
        print("pad pressed")

def midiExample():
    CHURCH_ORGAN = 19
    instrument = CHURCH_ORGAN

    #pygame.init()
    #pygame.midi.init()

    port = pygame.midi.get_default_output_id()
    #print ("using output_id :%s:" % port)
    midi_out = pygame.midi.Output(port, latency = 0)
    #print(pygame.midi.get_device_info(port))
    try:
        midi_out.set_instrument(instrument)

        midi_out.note_on(76,127) # 74 is middle C, 127 is "how loud" - max is 127
        sleep(1)
        midi_out.note_off(76,127)
        #sleep(.5)

    finally:
        del midi_out
        #pygame.midi.quit()

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    global whichKey
    global keyPressed
    global totalTime

    #ADDED DISPLAY
    global text
    global textRect

    #FINAL
    global textNote
    global textNoteRect

    playSound = 1

    keyName = ""

    x_change = 0

    block_startX_whiteKey = random.randrange(25,display_width-25,50)
    bp = random.randrange(0,10)
    block_startX_blackKey = positions_blackKey[bp]
    block_startY = -40
    block_speed = 5
    #block_speed = 12
    #block_speed = 25
    #block_speed = 100
    block_width_whiteKey = 40
    block_height_whiteKey = 40
    block_width_blackKey = 30
    block_height_blackKey = 30

    gameExit = False
    genBlock = False
    isBlack = False
    isWhite = False
    drawFirstLoop = True

    while not gameExit:
        screen.fill(gray)

        if block_startY == -40:
            start_time = time.time()


        if not genBlock and not isWhite and not isBlack:
            noteChoice = random.randrange(0,2)
            if noteChoice == 0:
                genBlock = True
                isWhite = True
            elif noteChoice == 1:
                genBlock = True
                isBlack = True

        if isWhite:
            blocks(block_startX_whiteKey, block_startY, block_width_whiteKey, block_height_whiteKey, white)
            block_startY += block_speed
            keyName = note_names.get(xValue_note_dict.get(block_startX_whiteKey))
            if playSound == 1:
                if __name__ == "__main__":
                    Thread(target = midiExample).start()
                    playSound = 0

        elif isBlack:
            blocks(block_startX_blackKey, block_startY, block_width_blackKey, block_height_blackKey, black)
            block_startY += block_speed
            keyName = note_names.get(xValue_note_dict.get(block_startX_blackKey))
            if playSound == 1:
                if __name__ == "__main__":
                    Thread(target = midiExample).start()
                    playSound = 0

        #ADDED DISPLAY
        drawKeyboard(whichKey, keyPressed)
        text = font.render("Correct Keys: " + str(len(totalTime)), True, yellow, gray)
        screen.blit(text, textRect)

        #FINAL
        textNote = bigFont.render(keyName, True, green, gray)
        screen.blit(textNote, textNoteRect)
        events = pygame.event.get()




        for e in events:
            if e.type in [QUIT]:
                print(e, 1)
                gameExit = True
            if e.type in [KEYDOWN]:
                print(e, 2)
                gameExit = True

        if i.poll():
            midi_events = i.read(10)
            #midi_events[0] is all midi events. [1] breaks this
            #midi_events[0][1] prints the timestamp
            #midi_events[0][0][0] is the note_status
            #midi_events[0][0][1] is the note_id
            #midi_events[0][0][2] is the velocity
            #midi_events[0][0][3] is ???
            #*****midiCounter(counts_keys, counts_pads, midi_events)
            whichKey = midi_events[0][0][1]
            keyPressed = midi_events[0][0][2]

            drawKeyboard(whichKey,keyPressed)
            if midi_events[0][0][2] == 0:
                continue
            elif noteChoice == 0:
                if(note_xValue_dict.get(midi_events[0][0][1]) == block_startX_whiteKey):
                    block_startY = -40
                    totalTime.append(time.time() - start_time)
                    block_startX_whiteKey = random.randrange(25,display_width-25,50)
                    genBlock = False
                    isWhite = False
                    playSound = 1
                else:
                    #ADDED DISPLAY
                    totalTime.append(time.time() - start_time)
                    #print("You Lose")
                    gameExit = endGame()

            elif noteChoice == 1:
                if(note_xValue_dict.get(midi_events[0][0][1]) == block_startX_blackKey):
                    block_startY = -40
                    totalTime.append(time.time() - start_time)
                    bp = random.randrange(0,10)
                    block_startX_blackKey = positions_blackKey[bp]
                    genBlock = False
                    isBlack = False
                    playSound = 1
                else:
                    #ADDED DISPLAY
                    totalTime.append(time.time() - start_time)
                    #print("You Lose")
                    gameExit = endGame()

            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                event_post( m_e )

        #print(block_startX)
        #print(keyboardXPosition + 50)
        """
        if noteChoice == 0:
            if(xValue_note_dict.get(block_startX_whiteKey)):
                print("key is ", xValue_note_dict.get(block_startX_whiteKey))
        elif noteChoice == 1:
            if(xValue_note_dict.get(block_startX_blackKey)):
                print("key is ", xValue_note_dict.get(block_startX_blackKey))
        """

        if block_startY > display_height - 180:
            #print("block hit bottom")
            if noteChoice == 0:
                block_startY = -40
                totalTime.append(time.time() - start_time)
                print(totalTime)
                block_startX_whiteKey = random.randrange(25,display_width-25,50)
                genBlock = False
                isWhite = False
                #print("You Lose")
                gameExit = endGame
            elif noteChoice == 1:
                block_startY = -40
                totalTime.append(time.time() - start_time)
                print(totalTime)
                bp = random.randrange(0,10)
                block_startX_blackKey = positions_blackKey[bp]
                genBlock = False
                isBlack = False
                #print("You Lose")
                gameExit = endGame()

        pygame.display.update()
        clock.tick(60)

game_loop()
i.close()
pygame.midi.quit()

"""
#ADDED DISPLAY
reactionTime = 0
for x in totalTime:
    reactionTime = reactionTime + x
#print("Reaction Time = ", reactionTime/len(totalTime), "sec")
#print("Correct keys = ", len(totalTime) - 1)

if len(totalTime) == 1:
    print(str(len(totalTime)))
    text = font.render(("Reaction Time = N/A "), True, yellow, gray)
    text2 = font.render("Correct keys = " + str(len(totalTime) - 1), True, yellow, gray)
else:
    text = font.render("Reaction Time = " + str(reactionTime/len(totalTime) - 1) + "sec", True, yellow, gray)
    text2 = font.render("Correct keys = " + str(len(totalTime) - 1), True, yellow, gray)
screen.blit(text, (0,0))
screen.blit(text2, (0,30))
pygame.display.update()
time.sleep(.5)
time.sleep(10)
"""
pygame.quit()

#reactionTime = 0
#for x in totalTime:
#    reactionTime = reactionTime + x
#print("Reaction Time = ", reactionTime/len(totalTime), "sec")
#print("Correct keys = ", len(totalTime) - 1)
