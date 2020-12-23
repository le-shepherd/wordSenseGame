import pygame, random, sys
from pygame.locals import *
# rom random import shuffle

########################################################
#
#    Version targeting the first part of the compound
#
########################################################

import pickle # to turn the csv table into a byte stream
import os.path # to check whether pickled data exists in file already

# We need to read from File: the High Scores, in the form Name,Score
# read "wordSenseScores.txt"

if os.path.isfile("./data.pickle"):
    with open('data.pickle', 'rb') as f:
        content = pickle.load(f)
else:
    with open('wordSenseScores.txt', 'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content] 
        content = [x.split(",") for x in content] 

    
    with open('data.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(content, f, pickle.HIGHEST_PROTOCOL)

sortedList = sorted(content, key=lambda score: int(score[1]),reverse=True)
winner,highscore = sortedList[0]
runnerUp1,highscore1 = sortedList[1]
runnerUp2,highscore2 = sortedList[2]
runnerUp3,highscore3 = sortedList[3]
runnerUp4,highscore4 = sortedList[4]
runnerUp5,highscore5 = sortedList[5]
runnerUp6,highscore6 = sortedList[6]
runnerUp7,highscore7 = sortedList[7]
runnerUp8,highscore8 = sortedList[8]
runnerUp9,highscore9 = sortedList[9]
        
# winner,highscore = content[0]
# runnerUp1,highscore1 = content[1]
# runnerUp2,highscore2 = content[2]
# runnerUp3,highscore3 = content[3]
# runnerUp4,highscore4 = content[4]
# runnerUp9,highscore9 = content[9]

# Window settings
WINDOWWIDTH = 1600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60

# set up the colors
BLACK = (0,0,0)
GRAY = (200,200,200)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)



# Set up pygame, the window, and the mouse cursor.
# pygame.init()
pygame.font.init()
pygame.display.init()
# pygame.mixer.init()
# pygame.joystick.init()
# pygame.freetype.init()
# pygame.midi.init()
# pygame.cdrom.init()
# pygame.scrap.init()

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Word sense matching")
pygame.mouse.set_visible(True) # use a visible cursor
# pygame.mouse.set_visible(False)


# Set up the fonts.
font = pygame.font.SysFont(None, 48)
def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

def drawText(text, font, surface, x, y):
    # textobj = font.render(text, 1, TEXTCOLOR)
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
# Set up images.
instructionsImage = pygame.image.load('wordSenseInstructions.bmp')
instructionsRect = instructionsImage.get_rect()
instructionsRect.centerx = 800
instructionsRect.centery = 300

# Draw the instructions
windowSurface.blit(instructionsImage, instructionsRect)
pygame.display.update()
waitForPlayerToPressKey()

# set up the fonts
basicFont = pygame.font.SysFont(None,48)


# set up positions
compoundAPositionX = compoundBPositionX = targetAPositionX = targetBPositionX = windowSurface.get_rect().centerx - 600

compoundAPositionY = windowSurface.get_rect().centery - 200
compoundBPositionY = windowSurface.get_rect().centery + 100
definitionAPositionX = windowSurface.get_rect().centerx - 300
definitionAPositionY = windowSurface.get_rect().centery - 50
definitionBPositionX = windowSurface.get_rect().centerx - 300
definitionBPositionY = windowSurface.get_rect().centery + 50
targetAPositionY = windowSurface.get_rect().centery - 100
targetBPositionY = windowSurface.get_rect().centery + 200

# use mixed pairs?
# for the prototype: only one version
# form,course,account,floor,jacket,limit,service,mine,model,race,tank,screen,plant,line,bill,case,run,drop,stand,bar 20
# I can go till the end if I play as fast as possibly ignoring correctness!
# Better add some more!
# 25, and that should be enough!

sourceListSameB = [["transfer form","verse form","a printed document with spaces in which to write","an arrangement of the elements in a composition or discourse"],
              ["vegetable course","zoology course","part of a meal served at one time","education imparted in a series of lessons or meetings"],
              ["insider account","cash account","a record or narrative description of past events","a contractual relationship to provide for regular banking services"],
              ["jungle floor","wagon floor","the ground on which people and animals move about","the inside lower horizontal surface"],
              ["cashmere jacket","book jacket","a short coat","an outer wrapping or casing"],
              ["confidence limit","city limit","the greatest possible degree of something","the boundary of a specific area"],
              ["funeral service","tea service","the act of public worship following prescribed rules","tableware consisting of a complete set of articles for use at table"],
              ["diamond mine","land mine","excavation in the earth from which ores and minerals are extracted","explosive device that explodes on contact"],
              ["agency model","climate model","a person who wears clothes to display fashions","a hypothetical description of a complex entity or process"],
              ["armament race","elf race","any competition","people who are believed to belong to the same genetic stock"],
              ["water tank","battle tank","a large (usually metallic) vessel for holding gases or liquids","an enclosed armored military vehicle"],
              ["cinema screen","wind screen","a white or silvered surface for projecting films","a protective covering that keeps things out or hinders sight"],
              # so far all from the Reddy List
              ["hop plant","engine plant","a living organism lacking the power of locomotion","buildings for carrying on industrial labor"],
              ["coffee line","fuel line","a formation of people or things one behind another","a pipe used to transport liquids or gases"],
              ["gas bill","government bill","an itemized statement of money owed","a statute in draft before it becomes law"],
              ["rape case","presentation case","a lawsuit","a glass container used to display items"],
              ["chicken run","print run","an enclosure for small domestic animals","the production achieved during a continuous period of operation"],
              ["price drop","ransom drop","a sudden sharp decrease in some quantity","the act of dropping something"],
              ["microphone stand","vegetable stand","a support or foundation","a booth where articles are displayed for sale"],
              ["iron bar","hotel bar","a rigid piece of metal or wood","a room where alcoholic drinks are served over a counter"],
              ["paradigm shift","night shift","a qualitative change","the time period during which you are at work"],
              ["bow tie","family tie","neckwear consisting of a long narrow piece of material","a social or business relationship"],
              ["baseball cap","distributor cap","a tight-fitting headdress","a top (as for a bottle)"],
              ["sound check","trading check","the act of inspecting or verifying","a written order directing a bank to pay money"],
              ["party cell","prison cell","a part or the nucleus of a larger political movement","any small compartment"]
              
]
# ["","","",""]

# not so much BrE (Melanie)              ["coffee line","fuel line","a formation of people or things one behind another","a pipe used to transport liquids or gases"],


# snake, game, credit, brass, head, rock, bank,call,case,chain,engine,firing,interest,crash,ball,draft,web,plant,china,lift
# 21
sourceListSameA = [["snake cable","snake charmer","something long, thin, and flexible resembling a snake","limbless scaly elongate reptile"],
                   ["game theory","game bird","a contest with rules to determine a winner","animal hunted for food or sport"],
                   ["credit agreement","credit sequence","money available for a client to borrow","an entry on a list of persons who contributed to a film"],
                   ["brass foundry","brass ensemble","an alloy of copper and zinc","a wind instrument"],
                   ["head servant","head gear","a person who is in charge","the upper part of the human body"],
                   ["rock field","rock tour","a lump or mass of hard consolidated mineral matter","a genre of popular music"],
                   ["bank job","bank barn","a financial institution","sloping land"],
                   ["call position","call log","the option to buy a given stock","a telephone connection"],
                   ["case lid","case ending","a portable container for carrying several objects","any of the inflected forms of noun, adjective, or pronoun"],
                   ["chain store","chain letter","a number of similar establishments","a series of things depending on each other"],
                   ["engine driver","engine mounting","a wheeled vehicle","a type of motor"],
                   ["firing pattern","firing process","the act of firing weapons","the act of setting something on fire"],
                   ["interest rate","interest span","a fixed charge for borrowing money","a sense of concern with and curiosity"],
                   ["crash barrier","crash period","a serious accident","a sudden large decline of business or the prices of stocks"],
                   ["ball game","ball dress","round object","a lavish dance"],
                   ["draft constitution","draft evasion","any of the various versions in the development of a written work","compulsory military service"],
                   ["web site","web width","a computer network","a fabric"],
                   ["china plate","china lobby","high quality porcelain","a communist nation in eastern Asia"],
                   ["plant pot","plant loss","a living organism","buildings for carrying on industrial labor"],
                   ["lift attendant","lift effect","lifting device consisting of a cage","aerodynamic force component opposing gravity"],
                   ["crack addict","crack length","purified and potent form of cocaine","a long narrow opening"],
                   ["bug spray","bug fix","general term for any insect","a fault or defect in a computer program"],
                   ["slug gun","slug pellet","a gastropod having an elongated slimy body","a projectile that is fired from a gun"],
                   ["capital injection","capital goods","wealth in the form of money","assets available for use in production"],
                   ["star dancer","star map","someone who is dazzlingly skilled in any field","a celestial body"]
                   
]

# ["","","",""]


sourceListMixed = [["bank account","river bank","an institution where people can keep their money","raised area of ground"],
              ["baseball cap","distributor cap","a tight-fitting headdress","a top (as for a bottle)"],
                   ["ball game","ball dress","round object","a lavish dance"],
                   ["race horse","mill race","a contest of speed","a canal for a current of water"],
              ["paradigm shift","night shift","a qualitative change","the time period during which you are at work"],
                   ["draft constitution","draft evasion","any of the various versions in the development of a written work","compulsory military service"],
              ["sound check","trading check","the act of inspecting or verifying","a written order directing a bank to pay money"],
                   ["spy ring","ring practice","an association of criminals","a platform usually marked off by ropes"],
                   ["plate tectonics","collection plate","a rigid layer of the Earth's crust","a shallow receptacle for collection in church"],                   
              ["chicken run","print run","an enclosure for small domestic animals","the production achieved during a continuous period of operation"],
              ["price drop","ransom drop","a sudden sharp decrease in some quantity","the act of dropping something"],
                   ["web site","web width","a computer network","a fabric"],
                   ["china plate","china lobby","high quality porcelain","a communist nation in eastern Asia"],
              ["iron bar","hotel bar","a rigid piece of metal or wood","a room where alcoholic drinks are served over a counter"],
                   ["plant pot","plant loss","a living organism","buildings for carrying on industrial labor"],
                   ["lift attendant","lift effect","lifting device consisting of a cage","aerodynamic force component opposing gravity"],
                   ["rock star","star pattern","someone who is dazzlingly skilled in any field","a celestial body"],
                   ["crack addict","crack length","purified and potent form of cocaine","a long narrow opening"],
                   ["bug spray","bug fix","general term for any insect","a fault or defect in a computer program"],
                   ["slug gun","slug pellet","a gastropod having an elongated slimy body","a projectile that is fired from a gun"],
                   ["capital injection","capital goods","wealth in the form of money","assets available for use in production"],
                                 ["rape case","presentation case","a lawsuit","a glass container used to display items"],
              ["microphone stand","vegetable stand","a support or foundation","a booth where articles are displayed for sale"],
              ["bow tie","family tie","neckwear consisting of a long narrow piece of material","a social or business relationship"],
              ["party cell","prison cell","a part or the nucleus of a larger political movement","any small compartment"]
                   
                   

]
#  ["","","",""]


# sourceList = sourceListSameB
sourceList = sourceListSameA
# sourceList = sourceListMixed

# use Org to latter check whether the answers were wrong or right.
compoundOrgA,compoundOrgB,definitionA,definitionB = sourceList[0]

# shuffle the two pairs
toShuffle = [compoundOrgA,compoundOrgB]

newList = random.sample(toShuffle,2)
compoundA = newList[0]
compoundB = newList[1]

compoundAPart1, compoundAPart2 = compoundA.split(" ")
compoundBPart1, compoundBPart2 = compoundB.split(" ")

textA = basicFont.render(definitionA,True,WHITE,BLUE)
textARect = textA.get_rect()
textARect.left = definitionAPositionX
textARect.centery = definitionAPositionY


textB = basicFont.render(definitionB,True,WHITE,BLUE)
textBRect = textB.get_rect()
# print(textBRect)
# textBRect.centerx = windowSurface.get_rect().centerx + 400
textBRect.left = definitionBPositionX
textBRect.centery = definitionBPositionY

compoundAtext = basicFont.render(compoundA,True,WHITE,BLUE)
compoundAtextRect = compoundAtext.get_rect()
compoundAtextRect.centerx = compoundAPositionX
compoundAtextRect.centery = compoundAPositionY

compoundBtext = basicFont.render(compoundB,True,WHITE,BLUE)
compoundBtextRect = compoundBtext.get_rect()
# print(textBRect)
compoundBtextRect.centerx = compoundBPositionX 
compoundBtextRect.centery = compoundBPositionY


# Note: below the red highlighting is switched to the first compound part!

compoundAPart1text = basicFont.render(compoundAPart1,True,RED,WHITE)
compoundAPart2text = basicFont.render(compoundAPart2,True,BLACK,WHITE)
compoundAPart1textRect = compoundAPart1text.get_rect()
compoundAPart1textRect.centerx = compoundAPositionX
compoundAPart1textRect.centery = compoundAPositionY
compoundAPart2textRect = compoundAPart2text.get_rect()
compoundAPart2textRect.left = compoundAPart1textRect.right + 10
compoundAPart2textRect.centery = compoundAPositionY

compoundBPart1text = basicFont.render(compoundBPart1,True,RED,WHITE)
compoundBPart2text = basicFont.render(compoundBPart2,True,BLACK,WHITE)
compoundBPart1textRect = compoundBPart1text.get_rect()
compoundBPart1textRect.centerx = compoundBPositionX
compoundBPart1textRect.centery = compoundBPositionY
compoundBPart2textRect = compoundBPart2text.get_rect()
compoundBPart2textRect.left = compoundBPart1textRect.right + 10
compoundBPart2textRect.centery = compoundBPositionY


# targetFields
targetA = basicFont.render("??????????",True,WHITE,RED)
targetB = basicFont.render("??????????",True,WHITE,RED)

targetARect = targetA.get_rect()
# print(targetARect)

targetARect.centerx = targetAPositionX
targetARect.centery = targetAPositionY 

targetBRect = targetB.get_rect()
# print(targetBRect)

targetBRect.centerx = targetBPositionX
targetBRect.centery = targetBPositionY


# draw the white background onto the surface
windowSurface.fill(WHITE)

selectedTextA = False
selectedTextB = False

definitionAMatched = definitionBMatched = False
score = 0
counter = 0
# variable for the name of the player
name = ""
player = ""

# time the game is running
gameTime = 60000
# gameTime = 10000
# gameTime = 5000


displayCorrect = False
paused  = False
running = True
compoundCounter = 0
counterCorrect = 0
timeCorrect = 500    # time the Correct!/Wrong! things are displayed
# run game loop
start_time = pygame.time.get_ticks() 
correctOrNot = ""


while True:
    
    for event in pygame.event.get():
        elapsedTime = pygame.time.get_ticks()
        pygame.time.wait(0)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        (mouseX,mouseY) = pygame.mouse.get_pos()    
        # event.button 1 is the left button of the mouse    
        # if event.type == MOUSEMOTION:
        #     textRect.centerx = event.pos[0]
        #     textRect.centery = event.pos[1]
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            (mouseX,mouseY) = pygame.mouse.get_pos()
            print(mouseX,mouseY)
            # textRect.centerx = mouseX
            # textRect.centery = mouseY
        # test whether we clicked on a definition
        if event.type == MOUSEBUTTONDOWN and textARect.collidepoint(mouseX,mouseY) and selectedTextA == False:
            print("Mouse clicked on first definition")
            textA = basicFont.render(definitionA,True,WHITE,RED)
            textARect = textA.get_rect()
            textARect.left = windowSurface.get_rect().centerx - 300
            textARect.centery = windowSurface.get_rect().centery - 50
            # textRect.centerx = windowSurface.get_rect().centerx
            # textRect.centery = windowSurface.get_rect().centery
            # (mouseX,mouseY) = pygame.mouse.get_pos()
            # textRect.centerx = mouseX
            # textRect.centery = mouseY
            selectedTextA = True
        # else:
        #     selectedTextA = False
        # print(selectedTextA)
        if event.type == MOUSEBUTTONDOWN and textBRect.collidepoint(mouseX,mouseY) and selectedTextB == False:
            print("Mouse clicked on second definition")
            textB = basicFont.render(definitionB,True,WHITE,RED)
            textBRect = textB.get_rect()
            textBRect.left = windowSurface.get_rect().centerx - 300
            textBRect.centery = windowSurface.get_rect().centery + 50
            # textRect.centerx = windowSurface.get_rect().centerx
            # textRect.centery = windowSurface.get_rect().centery
            # (mouseX,mouseY) = pygame.mouse.get_pos()
            # textRect.centerx = mouseX
            # textRect.centery = mouseY
            selectedTextB = True
        # if selectedTextA == True and event.type == MOUSEMOTION:
        # if selectedTextA and event.type == MOUSEMOTION:
        # if selectedTextA and event.type == MOUSEBUTTONDOWN:
        if selectedTextA and event.type == MOUSEMOTION:
            # If the mouse moves, move the player where to the cursor.
            # textRect.centerx = event.pos[0]
            # textRect.centery = event.pos[1]
            (mouseX,mouseY) = pygame.mouse.get_pos()
            textARect.centerx = mouseX
            textARect.centery = mouseY
            # print(textARect)
            # print(mouseY)
        # if selectedTextB and event.type == MOUSEBUTTONDOWN:
        if selectedTextB and event.type == MOUSEMOTION:
            (mouseX,mouseY) = pygame.mouse.get_pos()
            textBRect.centerx = mouseX
            textBRect.centery = mouseY
            # print(textBRect)
            # print(mouseY)
        # if event.type == MOUSEBUTTONDOWN and textRect.collidepoint(mouseX,mouseY) and selectedTextA:
        #     textRect.centerx = windowSurface.get_rect().centerx
        #     textRect.centery = windowSurface.get_rect().centery
        #     text = basicFont.render(compound,True,WHITE,BLUE)
        #     textRect = text.get_rect()
        #     selectedTextA = False

        # if event.type == MOUSEBUTTONDOWN and textARect.colliderect(targetARect):
        if event.type == MOUSEBUTTONUP and textARect.colliderect(targetARect):
        # if textARect.colliderect(targetARect):
            print("Definition A matched to compound A")
            matchTrackerA = "AA"
            targetA = basicFont.render("",True,WHITE,WHITE)
            selectedTextA = False
            textARect.left = windowSurface.get_rect().centerx - 700 
            textARect.centery = windowSurface.get_rect().centery - 100
            definitionAMatched = True
        if event.type == MOUSEBUTTONUP and textARect.colliderect(targetBRect):
            print("Definition A matched to compound B")
            matchTrackerA = "AB"
            targetB = basicFont.render("",True,WHITE,WHITE)
            selectedTextA = False
            textARect.left = windowSurface.get_rect().centerx - 700 
            textARect.centery = windowSurface.get_rect().centery + 200
            definitionAMatched = True
        if event.type == MOUSEBUTTONUP and textBRect.colliderect(targetARect):
            print("Definition B matched to compound A")
            matchTrackerB = "BA" 
            targetA = basicFont.render("",True,WHITE,WHITE)
            selectedTextB = False
            textBRect.left = windowSurface.get_rect().centerx - 700 
            textBRect.centery = windowSurface.get_rect().centery - 100
            definitionBMatched = True
        if event.type == MOUSEBUTTONUP and textBRect.colliderect(targetBRect):
            print("Definition B matched to compound B")
            matchTrackerB = "BB" 
            targetB = basicFont.render("",True,WHITE,WHITE)
            selectedTextB = False
            textBRect.left = windowSurface.get_rect().centerx - 700 
            textBRect.centery = windowSurface.get_rect().centery + 200
            definitionBMatched = True


        # if definitionAMatched == True and definitionBMatched == True:
        #     print("Hurray")
        #     counter += 1
        #     print(counter)
        #     definitionAMatched = definitionBMatched = False
        #     # player and food squares
        if definitionAMatched == True and definitionBMatched == True:
            # Check if these are the correct answers
            # HIER WEITER! USE matchTracker and compoundA and compoundAOrig!!
            if matchTrackerA == "AA" and (compoundA == compoundOrgA):
                print("Correct, defintion A matches compound A!!")
                # drawText('Correct!', font, windowSurface, (WINDOWWIDTH / 3) + 180, (WINDOWHEIGHT / 3) - 250)
                displayCorrect = True
                print(displayCorrect)
                correctOrNot = "Correct!"
                displayCorrectStartTime = pygame.time.get_ticks() - start_time
                # pygame.time.wait(1000)  
                counterCorrect += 1
            elif matchTrackerA == "AB" and (compoundB == compoundOrgA):
                print("Correct, defintion A matches compound B!")
                # drawText('Correct!', font, windowSurface, (WINDOWWIDTH / 3) + 180, (WINDOWHEIGHT / 3) - 250)
                displayCorrect = True
                correctOrNot = "Correct!"
                print(displayCorrect)
                displayCorrectStartTime = pygame.time.get_ticks() - start_time
                counterCorrect += 1
            else:
                    displayCorrect = True
                    displayCorrectStartTime = pygame.time.get_ticks() - start_time
                    print("Wrong! You made a mistake")
                    correctOrNot = "Wrong!"

        # The flo
        if displayCorrect == True:
            drawText('Correct!', font, windowSurface, 50,800)
            print("test")
            pygame.display.update()
            if (((pygame.time.get_ticks() - start_time) - displayCorrectStartTime)) > 5000: 
              displayCorrect = False
              print("testover")
        for structures in sourceList[:]:
                
            if definitionAMatched == True and definitionBMatched == True:
  
                

                # Prepare new items 
                sourceList.remove(structures)
                definitionAMatched = definitionBMatched = False
                # compoundA,compoundB,definitionA,definitionB = sourceList[0]
                compoundOrgA,compoundOrgB,definitionA,definitionB = sourceList[0]
                toShuffle = [compoundOrgA,compoundOrgB]
                newList = random.sample(toShuffle,2)
                compoundA = newList[0]
                compoundB = newList[1]
 
                textA = basicFont.render(definitionA,True,WHITE,BLUE)
                textARect = textA.get_rect()
                textARect.left = windowSurface.get_rect().centerx - 300
                textARect.centery = windowSurface.get_rect().centery - 50
                
                # textA = basicFont.render(definitionA,True,WHITE,BLUE)
                # textARect = textA.get_rect()
                # textARect.left = windowSurface.get_rect().centerx - 300
                # textARect.centery = windowSurface.get_rect().centery - 50
                # # print(textARect)
                # # 188, 35
                
                textB = basicFont.render(definitionB,True,WHITE,BLUE)
                textBRect = textB.get_rect()
                print(textBRect)
                # textBRect.centerx = windowSurface.get_rect().centerx + 400
                textBRect.left = windowSurface.get_rect().centerx - 300
                textBRect.centery = windowSurface.get_rect().centery + 50
 
                # OK, hier weiter: reset the targets and the compounds!
                # targetFields
                targetA = basicFont.render("??????????",True,WHITE,RED)
                targetB = basicFont.render("??????????",True,WHITE,RED)
                
                targetARect = targetA.get_rect()
                print(targetARect)
                # 188, 35
                targetARect.centerx = targetAPositionX
                targetARect.centery = windowSurface.get_rect().centery - 100 
                
                targetBRect = targetB.get_rect()
                print(targetBRect)
                # 188, 35
                targetBRect.centerx = targetBPositionX
                targetBRect.centery = windowSurface.get_rect().centery + 200
                compoundAPart1, compoundAPart2 = compoundA.split(" ")
                compoundBPart1, compoundBPart2 = compoundB.split(" ")
                compoundAPart1text = basicFont.render(compoundAPart1,True,RED,WHITE)
                compoundAPart2text = basicFont.render(compoundAPart2,True,BLACK,WHITE)
                compoundAPart1textRect = compoundAPart1text.get_rect()
                compoundAPart1textRect.centerx = compoundAPositionX
                compoundAPart1textRect.centery = compoundAPositionY
                compoundAPart2textRect = compoundAPart2text.get_rect()
                compoundAPart2textRect.left = compoundAPart1textRect.right + 10
                compoundAPart2textRect.centery = compoundAPositionY
                
                compoundBPart1text = basicFont.render(compoundBPart1,True,RED,WHITE)
                compoundBPart2text = basicFont.render(compoundBPart2,True,BLACK,WHITE)
                compoundBPart1textRect = compoundBPart1text.get_rect()
                compoundBPart1textRect.centerx = compoundBPositionX
                compoundBPart1textRect.centery = compoundBPositionY
                compoundBPart2textRect = compoundBPart2text.get_rect()
                compoundBPart2textRect.left = compoundBPart1textRect.right + 10
                compoundBPart2textRect.centery = compoundBPositionY
 
 
                # compoundAtext = basicFont.render(compoundA,True,WHITE,BLUE)
                # compoundAtextRect = compoundAtext.get_rect()
                # compoundAtextRect.centerx = compoundAPositionX
                # compoundAtextRect.centery = windowSurface.get_rect().centery - 200
                # 
                # compoundBtext = basicFont.render(compoundB,True,WHITE,BLUE)
                # compoundBtextRect = compoundBtext.get_rect()
                # print(textBRect)
                # # 188, 35
                # compoundBtextRect.centerx = compoundBPositionX
                # compoundBtextRect.centery = windowSurface.get_rect().centery + 100
                compoundCounter += 1
                # pygame.time.get_ticks() - start_time
                # if (pygame.time.get_ticks() - start_time) == 60000:
                # if compoundCounter == 9:
                    # display end sequence!
                    # windowSurface.fill(WHITE)
                    # drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                    # print(counterCorrect)
                    # drawText('Press a key to exit.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                    # 
                    # pygame.display.update()
                    # waitForPlayerToPressKey()
                    # 
                    # pygame.quit()
                    # sys.exit()
            

    if not paused:
        counting_time = pygame.time.get_ticks() - start_time

        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str( (counting_time%60000)//1000 ).zfill(2)
        counting_millisecond = str(counting_time%1000).zfill(3)

        # counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)
        counting_string = "Time: %s:%s" % (counting_minutes, counting_seconds)

        counting_text = basicFont.render(str(counting_string), True, WHITE,BLACK)
        counting_rect = counting_text.get_rect() # center = windowSurface.get_rect().center)

        # screen.fill( (0,0,0) )
    

        # print(counting_string)
        # HIER WEITER!
        # if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where to the cursor.
        #    textRect.centerx = event.pos[0]
        #    textRect.centery = event.pos[1]
        # draw the tet onto the surface
        # if counting_time > 60000:
        if counting_time > gameTime:
            name = " "
            done = True
            
            # if compoundCounter == 9:
            # display end sequence!
            windowSurface.fill(WHITE)
            name = " "
            while done == True:
                # windowSurface.fill(WHITE)
                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                print(counterCorrect)
                drawText('Your score: {}'.format(str(counterCorrect)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                drawText('Highscore: {} ({})'.format(str(highscore),str(winner)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 150)
                drawText('Please add your name to the highscore list:', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 250)
                # name = " "
                # done = True
                
                for evt in pygame.event.get():
                    if evt.type == KEYDOWN:
                        if evt.unicode.isalpha():
                            name += evt.unicode
                        elif evt.key == K_BACKSPACE:
                            name = name[:-1]
                        elif evt.key == K_RETURN:
                            player = name
                            name = ""
                            done = False
                            
                windowSurface.fill(WHITE)
                    # whereToWrite =
                pygame.draw.rect(windowSurface,(210,210,210),((WINDOWWIDTH // 2 - 200),(WINDOWHEIGHT // 2 + 225),400,50)) # x,y,width,height.
                block = font.render(name, True, BLACK)
                rect = block.get_rect()
                # rect.center = windowSurface.get_rect().center
                rect.center = ((WINDOWWIDTH // 2),(WINDOWHEIGHT // 2 + 250))
                windowSurface.blit(block, rect)
                drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                print(counterCorrect)
                drawText('Your score: {}'.format(str(counterCorrect)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
                drawText('Highscore: {} ({})'.format(str(highscore),str(winner)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 150)
                drawText('Please add your name to the highscore list and hit return:', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 250)

                # pygame.display.flip()
                pygame.display.update()
                
                
                
                
                # if name == "":


            # Calculate new high score rankings
            if counterCorrect > int(highscore):
                print("new highscore")
            # if counterCorrect > highscore:
            #     print("you tied with the highscore")
            if counterCorrect > int(highscore9):
                print("you made it into the top ten!")
            content.append([player,counterCorrect])
            # [winner,runnerUp1,runnerUp2,runnerUp3,runnerUp4,counterCorrect]
            sortedList = sorted(content, key=lambda score: int(score[1]),reverse=True)
            # write new list to file
            with open('data.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(content, f, pickle.HIGHEST_PROTOCOL)

            winner,highscore = sortedList[0]
            runnerUp1,highscore1 = sortedList[1]
            runnerUp2,highscore2 = sortedList[2]
            runnerUp3,highscore3 = sortedList[3]
            runnerUp4,highscore4 = sortedList[4]
            runnerUp5,highscore5 = sortedList[5]
            runnerUp6,highscore6 = sortedList[6]
            runnerUp7,highscore7 = sortedList[7]
            runnerUp8,highscore8 = sortedList[8]
            runnerUp9,highscore9 = sortedList[9]

            


                
            # waitForPlayerToPressKey()
            windowSurface.fill(WHITE)        
            drawText('Top ten:', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) - 200)
            drawText('1. {} ({} points)'.format(str(winner),str(highscore)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) - 150)
            drawText('2. {} ({} points)'.format(str(runnerUp1),str(highscore1)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) - 120)
            drawText('3. {} ({} points)'.format(str(runnerUp2),str(highscore2)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) - 90)
            drawText('4. {} ({} points)'.format(str(runnerUp3),str(highscore3)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) - 60)
            drawText('5. {} ({} points)'.format(str(runnerUp4),str(highscore4)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) - 30)
            drawText('6. {} ({} points)'.format(str(runnerUp5),str(highscore5)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) )
            drawText('7. {} ({} points)'.format(str(runnerUp6),str(highscore6)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
            drawText('8. {} ({} points)'.format(str(runnerUp7),str(highscore7)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 60)
            drawText('9. {} ({} points)'.format(str(runnerUp8),str(highscore8)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 90)
            drawText('10. {} ({} points)'.format(str(runnerUp9),str(highscore9)), font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 120)
                
            # drawText('Your score: points', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 150)
            drawText('Press a key to exit.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 200)
            print("wann sind wir hier")

            
            pygame.display.update()
            waitForPlayerToPressKey()
            
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)
    if displayCorrect == True:
        # drawText('Correct!', font, windowSurface, WINDOWWIDTH-150,WINDOWHEIGHT-500)
        drawText(correctOrNot, font, windowSurface, WINDOWWIDTH-150,WINDOWHEIGHT-500)
        print("test")
        pygame.display.update()
        if (((pygame.time.get_ticks() - start_time) - displayCorrectStartTime)) > timeCorrect: 
          displayCorrect = False
          print("testover")
    # drawText('Time: %s' % (elapsedTime), font, windowSurface, 10, 0)
    windowSurface.blit(textA,textARect)
    windowSurface.blit(textB,textBRect)
    # windowSurface.blit(compoundAtext,compoundAtextRect)
    windowSurface.blit(compoundAPart1text,compoundAPart1textRect)
    windowSurface.blit(compoundAPart2text,compoundAPart2textRect)
    # windowSurface.blit(compoundBtext,compoundBtextRect)
    windowSurface.blit(compoundBPart1text,compoundBPart1textRect)
    windowSurface.blit(compoundBPart2text,compoundBPart2textRect)
    windowSurface.blit(targetA,targetARect)
    windowSurface.blit(targetB,targetBRect)
    windowSurface.blit(counting_text, counting_rect)
    pygame.display.update()
    mainClock.tick(FPS)




    
# rock mix
# police account
