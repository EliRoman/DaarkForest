import gametext as gtxt
import objects as obj
import random

# Global variables.
QUIT_COMMAND = "end game"


# This is used to end the game gracefully
def quit_game():
	print(gtxt.quit_game_message)
	quit()

# Prompts user for a coin toss and returns true if they win
def coin_flip():
	print('\n\nHeads or tails?\n')
	selected = int(p_select_from_list(["Heads","Tails"]))
	correct_side = random.randint(1,2)
	match correct_side:
		case 1:
			print("Heads.\n")
		case 2:
			print("Tails.\n")
	
	if selected == correct_side:
		return True
	else:
		return False


#dice rolling function for convenience
def roll_d(sides, num=1):
    results=[]
    for _ in range(num):
        roll = random.randint(1, sides)
        results.append(roll)
    return sum(results)

# Checks for certain inputs that are always options (including non-numeric commands). i.e. quit game, inventory, etc.
def check_inputs(player_input):
	
	#option to quit out of the game.
	if player_input == QUIT_COMMAND:
		game_running=False
		quit_game()
	
	#inventory not yet implemented

# Given a library of options and matching results, this function will display options and return the action to preform.
def p_select(options):
	
	# If a list object is passed, then p_select_from_list is used instead.
	if type(options) is list:
		return p_select_from_list(options)

	# While loop that keeps going until we get valid input and break out.
	while True:
		try:
			print("\nChoose one:")
			index=1
			keys={}
		    
		    #loop displays all keys in the library and assigns an index to them
			for key in options:
				print(f'{index}: {key}')
				keys[index]=key
				index +=1
		    
		    #take in player input
			player_input = input().lower().strip()

		    #check inputs for options that are always available
			check_inputs(player_input)
			
		    #match the input to the corresponding key and return the value
			chosen_key = keys[int(player_input)]
			return options[chosen_key]

		#If we get an invalid input then we catch it, display a warning message, and loop
		except (ValueError, KeyError):
			print(gtxt.invalid_input)

# Given a list of options this function will display options and return the number of the option chosen.
def p_select_from_list(options):
	
	# loops untill it valid input and returns valid value
	while True:
		try:
			print("\nChoose one:")
			number=1
			for choice in options:
				print(f'{number}: {choice}')
				number +=1
			
			player_input = input().lower().strip()

			#check inputs for options always available from player input screen
			check_inputs(player_input)

			#if input given is a valid option we return it
			if int(player_input) in range(1,number):
				return int(player_input)
			
			#if invalid print a message and the loop starts over
			print(gtxt.invalid_input)
		except (ValueError, KeyError):
			print(gtxt.invalid_input)

# Used to handle combat. Excepts enemy and player as args.
def combat(enemy, p, surprised=False):
	in_combat=True

	#In some scenarios player may get to attack first.
	#If so then surprised will be passed in as True and the enemy's first turn is skipped.
	if not surprised:
		print(f"\n    The {enemy.name} is attacking!")
		enemy.attack(p)
	else:
		print(f"\n    You charge at the {enemy.name}!")

	#combat loops until player or enemy is dead or flees
	while in_combat and p.living:
		
		#choose to attack(enemy) or flee
		match p_select([gtxt.atk,gtxt.flee]):
			case 1:
				p.attack(enemy)
			case 2:
				if flee():
					in_combat=False
					
		#if we're still fighting then enemy attacks, otherwise decide how to end
		if enemy.living and in_combat:
			enemy.attack(p)
		elif not enemy.living:
			print(f"The {enemy.name} dies.")
			in_combat=False
	#-- end of combat loop --#
	
	#if combat ends because of player death we end the game
	if not p.living:
		print(gtxt.defeat)
		quit_game()

# user Interface for escaping. returns true if sucessful.
def flee():
	print("You attempt to flee...")
	if coin_flip():
		print("You escape!")
		return True
	else:
		print("You failed to escape!")
		return False


#------------------------------#
#------- Event Handling -------#
#------------------------------#

#describes local setting and decides which encounter to display next. Used in zone transitions.
def next_scene(p):

	# describe_setting
	print(gtxt.setting[p.zone])
	
	#run a random encounter
	rand_encounter(p)

#finds and runs appropriate random encounter
def rand_encounter(p):

	# fetch list of scenes based on current zone. return one at random.
	scene = random.choice(zone_event[p.zone])
	
	#run the corresponding function
	eval(scene+"(p)")

#display and execute player options based on the area they are in
def zone_options(p):

	# This input does nothing. It's meant as a mental pause from whatever came before
	check_inputs(input())
	# We still check for universally excepted inputs.

	# describe setting
	print(gtxt.setting[p.zone])
	
	# Nested switch statements decide next action based on player inputs
	selecting=True
	match p.zone:
		# What the player can do depends on where in the game they are located.

		case "Entrance":
			print("From here you can go deeeper into the forest or leave on your boat.")
			while selecting:
				match p_select(["Enter the forest.", "Leave the forest."]):
					case 1:
						selecting = False
						print("You travel deeper into Daark Forest.")
						p.zone="Forest"
						next_scene(p)
					case 2:
						print("Not without your brother!")
			#-- end while loop --#

		case "Forest":
			print("You can search the area or rest for a while.")
			match p_select(["Search","Rest","Go back to the entrance."]):
				case 1:
					rand_encounter(p)
				case 2:
					print("You make a small shelter hidden in foliage and rest for a while.")
					p.restore_health()
				case 3:
					print("You walk back to the entrance of the forest.")
					p.zone = "Entrance"
					


#---------------------------------------------------------------#
#------- lists and dictionaries of events and encounters -------#
#---------------------------------------------------------------#

#dictionary of enimies with corresponding combat objects
combat_dict={
	"bat":'combat( eval(obj.creature_dict["bat"]), p=player)',
	"viper": "combat( eval(obj.creature_dict['viper']), p=player)",
	"fairy": "combat( eval(obj.creature_dict['fairy']), p=player)",
	"fairy_s":"combat(eval(obj.creature_dict['fairy']), p=player, surprised=True)"
}

#dictionary of zones with corresponding list of possible events
zone_event={
	"Entrance":["no_event"],
	"Forest":["fairy_event","viper_event","bat_event"],
	"Swamp":["no_event"],
	"Castle":["no_event"]
}
#currently only forest zone is available


#-------------------------------#
#------- event functions -------#
#-------------------------------#
# Each of these functions handle an event in the game

def no_event(p):
	print("You find nothing here.")
	return

# What happens when the player encounters a fairy
def fairy_event(player):

	#Print event description
	print(gtxt.evnt_fairy)

	#player chooses how to proceed
	match p_select(gtxt.basic_encounter_options):
		
		#attack
		case 1:
			eval(combat_dict["fairy_s"])
		
		#sneak
		case 2:
			if coin_flip():
				print("You hide and wait out the possible danger.")
				return
			else:
				print("The fairy notices you peaking at it from your hidding spot and becomes enraged.")
				eval(combat_dict["fairy"])
		
		#talk
		case 3:
			print(f"You approach and say a greating.")
			print(f'"Oh!", the fairy says. "A polite little {player.gender}! How unusual. What are you doing here?"')
			match p_select([
				'"I am looking for my brother."',
				'"I am here to defeat Lord Daark."',
				'"I just wandered in here, I guess."']):
				case 1: # Player is healed
					print('"How sweet! But this forest is very deadly. Allow me to help you..."')
					print("A low green aura rises from the fairy and rests upon you.")
					player.heal(roll_d(6,2)+3)
					input()
					print(f'"... And now I must be on my way, but be careful!" \nThe fairy zips off into the trees.')
				case 2: # Player is attacked
					print('"Oh dear... Then I guess I\'ll have to kill you."')
					eval(combat_dict["fairy"])
				case 3: # Player is moved to the starting area, "Entrance"
					print('"This is no place for one such as yourself. Let me show you the way out."')
					print('The fairy snapps it\'s fingers and a bright light fills your vison.')
					print('You feal your feet moving on their own, and before you know it you are somewhere else...\n')
					player.zone="Entrance"


def bat_event(player):

	#Print event description
	print("You see a crazed bat flying around in circles and shrieking loudly. It notices you and breaks into a dive.")
	#combat
	eval(combat_dict["bat"])

def viper_event(player):

	#Print event description
	print("While walking through the foliage you step on something strange. You look down, and see that it is a snake!")
	#combat
	eval(combat_dict["viper"])

