
# This file stores most of the text of the game.
# If text needs to be changed or added it is done here and not in the main body code.
# This is done to keep the main body code clean and to make it easier to find text that needs to be changed.



quit_game_message='''Thank you for trying this demo.
Goodbye!
'''


starter_weapon_select='''
Before leaving you managed to arm yourself with your father's old weapon. 
What kind of weapon was it?\n'''

defeat="""You have parished.

"""

invalid_input="Invalid input. Please enter only the number of your selection."

prompt="What will you do?\n\n"


#Game start options
choose_gender={
	"Boy":'"boy"',
	"Girl":'"girl"',
	"Neither":'"child"'
}

# Dictionary of starter weapons
starter_weapons={
        'Sword':'weapon(name="father\'s sword", dmg_dice_sides=8, bonus=2)',
        'Spear':'weapon(name="father\'s spear", dmg_dice_sides=4, bonus=4)',
        'Wand': 'weapon(name="father\'s wand", dmg_dice_sides=12, bonus=0)'
        }
#All starter weapons do an average of 6.5 damage overall, but each should feal different.
#Spear has less max damage but always does decent damg (5-8), 
# wand does 1-12 dmg and feals more random yet sometimes more powerful, 
# sword does 3-10 dmg and is meant to feal more balanced.

#combat options
atk="Attack!"
flee="Try to run away."



#---------- Settings and Scenes ----------#

#intro scene discriptors
intro_text='''The malevolent Lord Daark has kidnapped your innocent younger brother, ensconcing himself in a foreboding castle at the heart of his forest.'''

#library of setting descriptions
setting={
	"Entrance":'''
You stand at the entrance to the forest of Daark.
You see before you the looming canopy of ancient trees, where shadows dance, and unseen whispers hint at the supernatural.
Behind you is a wide river. On the shore is the small paddle boat you used to get here.''',
	"Forest":'''
You are in the heart of the forest.
The canopy of leaves above you is so thick that it's hard to tell night from day, yet somehow it is never too dark to see.
You are surrounded by trees in all directions, but you could find your way back to the entrance from here if you wanted.''',
	"Swamp":'''
You are in the swamp.
It is damp and dark here. Your feet sink about an inch into the mud with every step.''',
	"Castle":'''
You are in the castle of Lord Dark.
Thick tapestries hang over dark wood paneled walls. Dim candlelight twinkles from sconces placed along the walls.'''
}





#----------------------------------------#
#---------- Event Descriptions ----------#
#----------------------------------------#

#Fairy encounter
evnt_fairy='''
You notice something flitting through the air. It's small and human shaped.
You realise this is a fairy!
'''
basic_encounter_options=[
"Attack!",
"Hide.",
"Talk."
]

