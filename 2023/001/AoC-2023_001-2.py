#	--- Day 1: Trebuchet?! ---
#	Something is wrong with global snow production, and you've been selected to 
# 	take a look. The Elves have even given you a map; on it, they've used stars 
# 	to mark the top fifty locations that are likely to be having problems.
#	
#	You've been doing this long enough to know that to restore snow operations, 
# 	you need to check all fifty stars by December 25th.
#	
#	Collect stars by solving puzzles. Two puzzles will be made available on each 
# 	day in the Advent calendar; the second puzzle is unlocked when you complete 
# 	the first. Each puzzle grants one star. Good luck!
#	
#	You try to ask why they can't just use a weather machine ("not powerful enough") 
# 	and where they're even sending you ("the sky") and why your map looks mostly 
# 	blank ("you sure ask a lot of questions") and hang on did you just say the sky 
# 	("of course, where do you think snow comes from") when you realize that the 
# 	Elves are already loading you into a trebuchet ("please hold still, we need 
# 	to strap you in").
#	
#	As they're making the final adjustments, they discover that their calibration 
# 	document (your puzzle input) has been amended by a very young Elf who was 
# 	apparently just excited to show off her art skills. Consequently, the Elves 
# 	are having trouble reading the values on the document.
#	
#	The newly-improved calibration document consists of lines of text; each line 
# 	originally contained a specific calibration value that the Elves now need to 
# 	recover. On each line, the calibration value can be found by combining the 
# 	first digit and the last digit (in that order) to form a single two-digit number.
#	
#	For example:
#	
#	1abc2
#	pqr3stu8vwx
#	a1b2c3d4e5f
#	treb7uchet
#	In this example, the calibration values of these four lines are 12, 38, 15, 
# 	and 77. Adding these together produces 142.
#	
#	Consider your entire calibration document. What is the sum of all of the 
# 	calibration values?
#	
#	Your puzzle answer was 55108.
#	
#	--- Part Two ---
#	Your calculation isn't quite right. It looks like some of the digits are 
# 	actually spelled out with letters: one, two, three, four, five, six, seven, 
# 	eight, and nine also count as valid "digits".
#	
#	Equipped with this new information, you now need to find the real first and 
# 	last digit on each line. For example:
#	
#	two1nine
#	eightwothree
#	abcone2threexyz
#	xtwone3four
#	4nineeightseven2
#	zoneight234
#	7pqrstsixteen
#	In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
# 	Adding these together produces 281.
#	
#	What is the sum of all of the calibration values?
#	
#	Your puzzle answer was 56324.
#	
################################################################################

# OPEN FILE FOR READING
inFile = open("input.txt","r")

# INITIALIZE VARIABLES
cLine = ''
cTotal = 0
index = 0

# BEGIN FILE PROCESSING
with open("input.txt") as file:
    
    # PROCESS EACH LINE
    for line in file:
        print(line.rstrip())    # PRINT FOR REFERENCE
        index = 0               # ZERO INDEX FOR CHARACTER BY CHARACTER ANALYSIS OF EACH LINE
        cLine = ""              # CLEAR TEMP STRING BEFORE PROCESSING NEXT LINE
        
        # PROCESS EACH CHARACTER IN LINE
        for char in line:

            # ADD ALL NUMERIC CHARS TO TEMP STRING AUTOMATICALLY
            if char.isnumeric():
                cLine += char
            
            # IF NOT NUMERIC, MUST DETERMINE IF SUBSEQUENT ALPHA CHARACTERS COMPOSE A SPELLED NUMBER
            else:
                if line.find("zero", index, index + 4) != -1:
                    cLine += "0"
                elif line.find("one", index, index + 3) != -1:
                    cLine += "1"
                elif line.find("two", index, index + 3) != -1:
                    cLine += "2"
                elif line.find("three", index, index + 5) != -1:
                    cLine += "3"
                elif line.find("four", index, index + 4) != -1:
                    cLine += "4"
                elif line.find("five", index, index + 4) != -1:
                    cLine += "5"
                elif line.find("six", index, index + 3) != -1:
                    cLine += "6"
                elif line.find("seven", index, index + 5) != -1:
                    cLine += "7"
                elif line.find("eight", index, index + 5) != -1:
                    cLine += "8"
                elif line.find("nine", index, index + 4) != -1:
                    cLine += "9"
            
            # INCREMENT INDEX FOR PROCESSING NEXT CHARACTER IN LINE
            index += 1
        
        # ONCE TEMP STRING IS BUILT IN FULL, DETERMINE CORRECT CALIBRATION VALUE OF LINE'S CONTENTS
        print("UNFILTERED cLine: ", cLine)
        if len(cLine) == 1:
            cLine = int(cLine) * 11
        else:
            cLine = cLine[0] + cLine[-1]
        print("FINAL cLine: ", cLine)

        # MAINTAIN CALIBRATION VALUE TOTAL WHILE CONTINUING TO PROCESS FILE
        cTotal += int(cLine)

# DISPLAY FINAL CALIBRATION VALUE ONCE
print("cTotal: ", cTotal)

# CLOSE FILE
inFile.close()