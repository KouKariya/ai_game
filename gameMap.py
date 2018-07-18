import pygame

class Map():
	#gameMap class is used to store various important XY coordinates to move around within the game
	
	#Location or "room" that player is on. If game has just started, then starting room is 5(Living Room 1)
	gameLocation = 5
	
	#List containing images of all rooms
	#TODO create a series of lists within the "values" of the room dictionaries
	#Add coordinate info to list within "values" of roomList list/dictionary
	
	roomList = [{"room_0" : pygame.image.load("assets/images/room_0.png")},{"room_1" : pygame.image.load("assets/images/room_1.png")},{"room_2" : pygame.image.load("assets/images/room_2.png")},{"room_3" : pygame.image.load("assets/images/room_3.png")},{"room_4" : pygame.image.load("assets/images/room_4.png")},{"room_5" : pygame.image.load("assets/images/room_5.png")},{"room_6" : pygame.image.load("assets/images/room_6.png")},{"room_7" : pygame.image.load("assets/images/room_7.png")},{"room_8" : pygame.image.load("assets/images/room_8.png")}]
		
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
