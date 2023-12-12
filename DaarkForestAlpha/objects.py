
import gametext as gtxt
import encounters as enc



#weaopon class. Every creature that attacks has an instance of this. It is used to decide damage
class weapon:

    def __init__(self,name="body", dmg_dice_sides=4,num_dice=1,bonus=0):
        self.name = name
        self.dmg_dice_sides= dmg_dice_sides
        self.num_dice=num_dice
        self.bonus=bonus
    
    def damage(self):
        return enc.roll_d(self.dmg_dice_sides,self.num_dice) + self.bonus

#default values
player_ac = 13
default_weapon = weapon()

#Base creature class. Contains everything all creatures have in common.
class creature:
    
    def __init__(self, name='creature', health=10, max_health=100, living=True, ac=5, atk_mod=0):
        self.name = name
        self.health = health
        self.living = living
        self.max_health = max_health
        self.ac = ac
        self.atk_mod = atk_mod
    
    def damage(self,hp_num):
        self.health -= hp_num
        if self.health <= 0:
            self.health = 0
            self.living = False

    def heal(self,hp_num):
        print(f"{self.name} is healed for {hp_num} HP.")
        self.health += hp_num
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} now has {self.health} HP.")

# Player class. A child class of creature that can attack enemies.
class player_char(creature):
    
    #current location of the player
    zone = "Entrance"

    def __init__(self,name, weapon=default_weapon, health=50, max_health=50, living=True, ac=player_ac, atk_mod=0, gender="child"):
        creature.__init__(self,name,health,max_health,living,ac,atk_mod)
        self.weapon = weapon
        self.gender = gender

    def attack(self,creature):
        print(f'You attack the {creature.name} with your {self.weapon.name}.')
        if (enc.roll_d(20)+self.atk_mod) >= creature.ac:
            dmg = self.weapon.damage()
            print(f"You hit for {dmg} damage!")
            creature.damage(dmg)
        else:
            print("You miss!")

    def restore_health(self):
        self.health = self.max_health
        print("Your health is restored to full.")

#Enemy class. A child class of class creature that can attack the player
class enemy(creature):
    def __init__(self, name='creature', weapon=default_weapon, health=10, max_health=10, ac=12, atk_mod=0 ):
        creature.__init__(self)
        self.name = name
        self.weapon = weapon
        self.health = health
        self.max_health = max_health
        self.ac = ac
        self.atk_mod = atk_mod

    def attack(self,target):
        print(f'The {self.name} attacks with its {self.weapon.name}!')
        if (enc.roll_d(20)+self.atk_mod) >= target.ac:
            dmg = self.weapon.damage()
            print(f"You are hit for {dmg} damage.")
            target.damage(dmg)
            print(f"You now have {target.health} health.")
        else:
            print(f"The {self.name} misses.")

#runs at start of game. sets up player character object
def character_setup():
    #ask character name
    char_name = input('What is your name?\n')
    print('Are you a boy or a girl?')
    char_gender = eval(enc.p_select(gtxt.choose_gender))
    
    #ask to select weapon
    print(gtxt.starter_weapon_select)
    char_weapon = eval(enc.p_select(gtxt.starter_weapons)) #call p_select and pass it a library of options for player to choose from

    # create the character object
    player = player_char(name=char_name,gender=char_gender,weapon=char_weapon)
    print(f"You are a young {player.gender} named {player.name}, and you wield your {player.weapon.name}.")

    return player

#------- Dictionary of common creatures. -------#
# default args for weapon are: (name="body", dmg_dice_sides=4, num_dice=1, bonus=0)
# default args for an enemy creature are: ( name='creature', weapon=default_weapon, health=10, max_health=10, living=True, ac=12, atk_mod=0)
creature_dict ={
	"viper":"obj.enemy(name='viper',weapon = obj.weapon(name='fangs', num_dice=2, bonus=2),health=5, max_health=5, atk_mod=4)",
	"fairy":"obj.enemy(name='fairy', weapon=obj.weapon(name='wand', dmg_dice_sides=6, num_dice=2), health=20, max_health=20, ac=13, atk_mod=4)",
	"bat":"obj.enemy( name='bat', weapon=obj.weapon(name='fangs'), health=5, max_health=5, ac=15, atk_mod=0)"
}