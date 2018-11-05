class Map():
	#gameMap class is used to store various important XY coordinates to move around within the game
	
	#Location or "room" that player is on. If game has just started, then starting room is 5(Living Room 1)
	gameLocation = 5
	
	#Room-list variables that store important XY coordinates for their respective room
	#TODO update lists with "test locations" and troubleshoot within main class
	roomOne = [1,(0,0)]
	roomTwo = [2,(0,0)]
	roomThree = [3,(0,0)]
	roomFour = [4,(0,0)]
	roomFive = [5,(0,0)]
	roomSix = [6,(0,0)]
	roomSeven = [7,(0,0)]
	roomEight = [8,(0,0)]
	roomNine = [9,(0,0)]
	
	#List of rooms used to cycle and navigate to
	roomList = [roomOne, roomTwo, roomThree, roomFour, roomFive, roomSix, roomSeven, roomEight, roomNine]
	
	#Function to get location
	def getLocation():
		global gameLocation
		return gameLocation
	
	#Function to return list of "exit-coordinates" of the room the player is on	
	#def getRoomExitCoordinates():
		
	#Function to set location
	def setLocation(newLocation):
		global gameLocation
		gameLocation = newLocation
	
	#Defining function for this class
	def __init__(self, roomLocation, pygame, surface):
		self.gameLocation = roomLocation
		self.pygame = pygame
		self.surface = surface
