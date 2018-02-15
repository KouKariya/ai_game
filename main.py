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

pygame.display.set_caption("A.I.")
startScreen = pygame.image.load("assets/images/start_background.png")
introBackground = pygame.image.load("assets/images/intro_background.png")

#Sound variables
pygame.mixer.init()
startTheme = pygame.mixer.Sound("assets/sounds/rain.wav")
startTheme2 = pygame.mixer.Sound("assets/sounds/test_intro.wav")

#Game state variables
gameStarted = False
gameState = []
roomExitCoordinates = []
playerLocation = 5

#Create Map class
roomMap = gameMap.Map(playerLocation, pygame, surface)

#Start Screen
startSelect = False
loadSelect = False

#Mouse Variables
mousePosition = (0, 0)
mouseClick = False

# Function to handle all in-game clicks.
#def handleClick():

# Function to move the game along, pull and check for "story-events".
#def updateGame():

# Function to draw the game map & overall visuals
#def drawGame():

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
			
	if mouseClick is True and startSelect is True:
		gameStarted = True

def quitGame():
	pygame.quit()
	sys.exit()

while True:

	mousePosition = pygame.mouse.get_pos()
	
	#updateGame()
	
	# Load up start screen
	if gameStarted is False:
		startGame()
		
	# Transition into new game
	elif gameStarted is True and startSelect is True:
		startTheme2.stop()
		surface.blit(introBackground, (0,0))
		
		
	# Keyboard/Mouse/Close-window events
	for event in GAME_EVENTS.get():
	
		#Quit game. TODO Create some sort of ingame menu
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitGame()
				
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseClick = True
	
		if event.type == GAME_GLOBALS.QUIT:
			quitGame()

	#Refreshes the screen, updates w/ any changes
	pygame.display.update()
