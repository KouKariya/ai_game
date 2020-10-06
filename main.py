import pygame, sys, random, time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import gameMap


#Screen variables
windowWidth = 1024
windowHeight = 614
pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((windowWidth,windowHeight))
textFont = pygame.font.SysFont("monospace", 50)

clock = pygame.time.Clock()

pygame.display.set_caption("A.I.")
startScreen = pygame.image.load("assets/images/start_background.png")
introBackground = pygame.image.load("assets/images/intro_background.png")

#Sound variables
pygame.mixer.init()
startTheme = pygame.mixer.Sound("assets/sounds/rain.wav")
startTheme2 = pygame.mixer.Sound("assets/sounds/test_intro.wav")

#Game state variables
gameStarted = False
#List that preserves information about the game
#Act, room number, karma value
gameAct = 1
playerLocation = 5
playerSanity = 0
gameState = []
roomExitCoordinates = []


#Create Map class
roomMap = gameMap.Map(pygame, surface)

#Start Screen
startSelect = False
loadSelect = False

#Mouse Variables
mousePosition = (0, 0)
mouseClick = (0, 0)
mouseDown = False

#TODO fix clicking issue
# Function to handle all in-game clicks.
def handleClick():
	global mousePosition, mouseDown
	
	if pygame.mouse.get_pressed()[0] is True:
		mouseDown = True
		mouseClick = pygame.mouse.get_pos()
	elif pygame.mouse.get_pressed()[0] is False:
		mouseDown = False

# Function to move the game along, pull and check for "story-events".
#def updateGame():
#

# Function to draw the game map & overall visuals
#TODO fix code to allow cycle through of rooms(Bulk of work needs to happen under gameMap class.
def drawGame():
	roomDrawing = pygame.image.load("assets/images/room_"+ str(gameState[1]) + ".png")
	renderedText = textFont.render(str(gameState[0]), 1, (175, 59, 59))
	surface.blit(renderedText, (0,0))
	surface.blit(roomDrawing, (0,0))

#Function for dealing with the start screen and load up save files
#TODO add start-screen code from main loop unto function & have it execute properly
def startGame():
	global gameStarted, mousePosition, startSelect, loadSelect
	
	surface.blit(startScreen, (0,0))
	startTheme.play()
	startTheme2.play()
	
	
	if mousePosition[0] >= 420 and mousePosition[0] <= 600:
		if mousePosition[1] >= 370 and mousePosition[1] <= 440:
			startSelect = True
			loadSelect = False
			if startSelect is True:
				pygame.draw.rect(surface, (255,255,255), (420, 370, 180, 70), 3)
		elif mousePosition[1] >= 475 and mousePosition[1] <= 510:
			startSelect = False
			loadSelect = True
			if loadSelect is True:
				pygame.draw.rect(surface, (255,255,255), (420, 475, 180, 60), 3)
	else:
		startSelect = False
		loadSelect = False
		pygame.draw.rect(surface, (0,0,0), (420, 370, 180, 70), 3)
		pygame.draw.rect(surface, (0,0,0), (420, 475, 180, 60), 3)
			
	if mouseDown is True and startSelect is True:
		gameStarted = True

def quitGame():
	pygame.quit()
	sys.exit()

while True:

	mousePosition = pygame.mouse.get_pos()
	
	handleClick()
	
	# Load up start screen
	if gameStarted is False:
		startGame()
		
	# Transition into new game
	elif gameStarted is True and startSelect is True:
		gameState = [gameAct,playerLocation,playerSanity] #Game state starts out as Act 1, Room 5, 0 items. The game starts officially from this point.
		startSelect = False
		mouseDown = False
		startTheme2.stop()
		if mouseDown is False:
			surface.blit(introBackground, (0,0)) #Loads up opening scene
		startTheme.stop()
		

	else:
		pygame.time.wait(5000) #Pauses the game during 'introBackground' being drawn before proceeding w/ main game
		drawGame()#List index out of range when reached
		
		
	# Keyboard/Mouse/Close-window events
	for event in GAME_EVENTS.get():
	
		#Quit game. TODO Create some sort of ingame menu
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitGame()
				
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseDown = True
	
		if event.type == GAME_GLOBALS.QUIT:
			quitGame()

	#Refreshes the screen, updates w/ any changes
	clock.tick(60)
	pygame.display.update()
