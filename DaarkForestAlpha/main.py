import gametext as gtxt
import encounters as enc
import objects as obj


#let the user know the application has started
print('Loading Daark Forest Game Demo...\n\n')


#function runs a loop while the game is active
def run_game():
    game_running=True

    #Initialize starting zone
    enc.zone="Entrance"

    #Intro and character creation
    print(gtxt.intro_text)
    player= obj.character_setup()

    #main game loop
    while game_running:
        
        enc.zone_options(player)
    # game_running loop ends


# End of declarations. 
# Game begins here.
run_game()

# We should never get to this point, but if we de we can at least be polite.
print(f"Goodbye!")