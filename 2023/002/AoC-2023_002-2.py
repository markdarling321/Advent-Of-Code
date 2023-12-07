#	--- Day 2: Cube Conundrum ---
#	You're launched high into the atmosphere! The apex of your trajectory just
#	barely reaches the surface of a large island floating in the sky. You gently
# 	land in a fluffy pile of leaves. It's quite cold, but you don't see much snow.
# 	An Elf runs over to greet you.
#	
#	The Elf explains that you've arrived at Snow Island and apologizes for the
# 	lack of snow. He'll be happy to explain the situation, but it's a bit of a 
# 	walk, so you have some time. They don't get many visitors up here; would you 
# 	like to play a game in the meantime?
#	
#	As you walk, the Elf shows you a small bag and some cubes which are either 
# 	red, green, or blue. Each time you play this game, he will hide a secret 
# 	number of cubes of each color in the bag, and your goal is to figure out 
# 	information about the number of cubes.
#	
#	To get information, once a bag has been loaded with cubes, the Elf will reach 
# 	into the bag, grab a handful of random cubes, show them to you, and then put 
# 	them back in the bag. He'll do this a few times per game.
#	
#	You play several games and record the information from each game (your puzzle 
# 	input). Each game is listed with its ID number (like the 11 in Game 11: ...) 
# 	followed by a semicolon-separated list of subsets of cubes that were revealed 
# 	from the bag (like 3 red, 5 green, 4 blue).
#	
#	For example, the record of a few games might look like this:
#	
#	Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#	Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#	Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#	Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#	Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#	In game 1, three sets of cubes are revealed from the bag (and then put back 
# 	again). The first set is 3 blue cubes and 4 red cubes; the second set is 
# 	1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.
#	
#	The Elf would first like to know which games would have been possible if the 
# 	bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#	
#	In the example above, games 1, 2, and 5 would have been possible if the bag 
# 	had been loaded with that configuration. However, game 3 would have been 
# 	impossible because at one point the Elf showed you 20 red cubes at once; 
# 	similarly, game 4 would also have been impossible because the Elf showed you 
# 	15 blue cubes at once. If you add up the IDs of the games that would have 
# 	been possible, you get 8.
#	
#	Determine which games would have been possible if the bag had been loaded 
# 	with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of 
# 	the IDs of those games?
#	
#	Your puzzle answer was 2528.
#	
#	--- Part Two ---
#	The Elf says they've stopped producing snow because they aren't getting any 
# 	water! He isn't sure why the water stopped; however, he can show you how to 
# 	get to the water source to check it out for yourself. It's just up ahead!
#	
#	As you continue your walk, the Elf poses a second question: in each game you 
# 	played, what is the fewest number of cubes of each color that could have been 
# 	in the bag to make the game possible?
#	
#	Again consider the example games from earlier:
#	
#	Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#	Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#	Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#	Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#	Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#	In game 1, the game could have been played with as few as 4 red, 2 green, and 
# 	6 blue cubes. If any color had even one fewer cube, the game would have been 
# 	impossible.
#	Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
#	Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
#	Game 4 required at least 14 red, 3 green, and 15 blue cubes.
#	Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
#	The power of a set of cubes is equal to the numbers of red, green, and blue 
# 	cubes multiplied together. The power of the minimum set of cubes in game 1 is 
# 	48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these 
# 	five powers produces the sum 2286.
#	
#	For each game, find the minimum set of cubes that must have been present. What 
# 	is the sum of the power of these sets?
#	
#	Your puzzle answer was 67363.
#
################################################################################

# OPEN FILE FOR READING
inFile = open("input.txt","r")

# VARIABLES
redCubes = ''
greenCubes = ''
blueCubes = ''
powerOfGame = 0
sumOfPower = 0
lowestRed = '-1'
lowestGreen = '-1'
lowestBlue = '-1'
localMaxRed = '-1'
localMaxGreen = '-1'
localMaxBlue = '-1'

# BEGIN FILE PROCESSING
with open("input.txt") as file:

	# PROCESS EACH LINE
	for line in file:
		line = line.rstrip()
		print("\n\nPRINT:\t", line)    # PRINT FOR REFERENCE

		# SPLIT LINE ON : TO GET GAME ID AND SEPARATE ROUNDS FROM ID
		gameID = line.split(":")
		gameID = gameID[0].split(" ")
		gameID = gameID[1]
		print("GAME ID: ", gameID)

		# SPLIT LINE ON ; FOR INDIVIDUAL ROUNDS
		rounds = line.split(":")
		rounds = rounds[1].replace(" ","").split(";")
		print("ROUNDS: ", rounds)
		print()
		
		# RESET VARIABLES
		lowestRed = '-1'
		lowestGreen = '-1'
		lowestBlue = '-1'

		# ENUMERATE INDIVIDUAL DRAWS AND DETERMINE CUBE COUNTS PER DRAW
		for draws in rounds:
			# RESET VARIABLES
			redCubes = ''
			blueCubes = ''
			greenCubes = ''
			localMaxRed = '-1'
			localMaxGreen = '-1'
			localMaxBlue = '-1'
			
			draw = draws.split(",")		# CREATE LIST OF STRINGS CONTAINING INDIVIDUAL PICKS CONTAINING CUBE COUNT AND COLOR
			print("DRAW: ", draw)		# PRINT FOR REFERENCE

			# EXTRACT CUBE COUNTS FROM DATA
			for cube in draw:	# NOT EVERY DRAW PICKS ALL 3 COLORS EVERY TIME
				if cube.find("red") != -1:
					for char in cube:
						if char.isnumeric():
							redCubes += char	# BUILD CUBE COUNT AS STRING
					
				elif cube.find("green") != -1:
					for char in cube:
						if char.isnumeric():
							greenCubes += char	# BUILD CUBE COUNT AS STRING
					
				elif cube.find("blue") != -1:
					for char in cube:
						if char.isnumeric():
							blueCubes += char	# BUILD CUBE COUNT AS STRING

			# QUICK FIX FOR DRAWS WITHOUT A COLOR SELECTED			
			if redCubes == '':
				redCubes = 0
			if greenCubes == '':
				greenCubes = 0
			if blueCubes == '':
				blueCubes = 0

			# PRINT FOR REFERENCE
			print("RED CUBES: ", redCubes)
			print("GREEN CUBES: ", greenCubes)
			print("BLUE CUBES: ", blueCubes)
			print()

			# DETERMINE MINIMUM NUMBER OF CUBES FOR CURRENT DRAW
			if int(redCubes) > int(localMaxRed):
				localMaxRed = redCubes
				if int(localMaxRed) > int(lowestRed):
					lowestRed = redCubes
			if int(greenCubes) > int(localMaxGreen):
				localMaxGreen = greenCubes
				if int(localMaxGreen) > int(lowestGreen):
					lowestGreen = greenCubes
			if int(blueCubes) > int(localMaxBlue):
				localMaxBlue = blueCubes
				if int(localMaxBlue) > int(lowestBlue):
					lowestBlue = blueCubes

			# PRINT FOR REFERENCE
			print("RED LOCAL MAX: ", localMaxRed)
			print("LOWEST RED: ", lowestRed)
			print()
			print("GREEN LOCAL MAX: ", localMaxGreen)
			print("LOWEST GREEN: ", lowestGreen)
			print()
			print("BLUE LOCAL MAX: ", localMaxBlue)
			print("LOWEST BLUE: ", lowestBlue)
			print()
		
		# DETERMINE POWER OF GAME
		powerOfGame = int(lowestRed) * int(lowestGreen) * int(lowestBlue)
		sumOfPower += powerOfGame
	
	# DISPLAY FINAL RESULT
	print("SUM OF POWER: ", sumOfPower)

# CLOSE FILE
inFile.close()