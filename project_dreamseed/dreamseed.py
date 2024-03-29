""" This is the result of my training """

"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import math
import os
import random

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Project Dreamseed"

CHARACTER_SCALING = 1
TILE_SCALING = 4
MOB_SCALING = 0.5

# spell casting globals

SPELL_CAST_X = 200
SPELL_CAST_Y = 400

FIRESPEED = 5
WATERSPEED = 15
LIGHTNINGSPEED = 50


class Menu:
    def __init__(self):
        # Main menu Sprite lists
        self.menu_list1 = None
        self.menu_list2 = None
        self.menu_background = None


def setup_menu_1():
    menu = Menu()

    # Appending main menu sprites to lists
    menu.menu_list1 = arcade.SpriteList()
    menu.menu_list2 = arcade.SpriteList()
    menu.menu_background = arcade.SpriteList()

    back_drop = arcade.Sprite("images/menu icons/MenuBackdrop.png", 1)
    back_drop.center_x = 800
    back_drop.center_y = 400
    menu.menu_background.append(back_drop)

    backg_Wizard = arcade.Sprite("images/menu icons/Wizard.png", 3)
    backg_Wizard.center_x = 1300
    backg_Wizard.center_y = 200
    menu.menu_background.append(backg_Wizard)

    start_icon = arcade.Sprite("images/menu icons/Start.png", 1)
    start_icon.center_x = 800
    start_icon.center_y = 400
    menu.menu_list1.append(start_icon)

    easy_icon = arcade.Sprite("images/menu icons/Easy.png", 1)
    easy_icon.center_x = 800
    easy_icon.center_y = 525
    menu.menu_list2.append(easy_icon)

    normal_icon = arcade.Sprite("images/menu icons/Normal.png", 1)
    normal_icon.center_x = 800
    normal_icon.center_y = 400
    menu.menu_list2.append(normal_icon)

    hard_icon = arcade.Sprite("images/menu icons/Hard.png", 1)
    hard_icon.center_x = 800
    hard_icon.center_y = 275
    menu.menu_list2.append(hard_icon)

    return menu


# class to store variables for drawing the magic pool
class Magic:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.color = 0
        self.s_angle = 0
        self.f_angle = 0
        self.tilt = 0
        self.sections = 0


# setting up a health pool

class Health:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.max = 0
        self.value = 0
        self.color = 0


# Section for building functions

# class to store variables for drawing the magic pool
class Magic:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.color = 0
        self.s_angle = 0
        self.f_angle = 0
        self.tilt = 0
        self.sections = 0


# setting up a health pool

class Health:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.max = 0
        self.value = 0
        self.color = 0


# Section for building functions

# function to display the magic pool
def make_magic():
    magic = Magic()
    magic.x = 100
    magic.y = 700
    magic.width = 40
    magic.height = 40
    magic.color = arcade.color.BLUE_VIOLET
    magic.s_angle = 0
    magic.f_angle = 160
    magic.tilt = 0
    magic.sections = 300
    return magic


# function to display the health pool
def make_health():
    health = Health()
    health.x = 800
    health.y = 700
    health.width = 40
    health.max = 100
    health.color = arcade.color.DARK_SPRING_GREEN

    return health


# function to display the health pool
def make_health():
    health = Health()
    health.x = 800
    health.y = 700
    health.width = 40
    health.max = 100
    health.color = arcade.color.DARK_SPRING_GREEN

    return health


class MyGame(arcade.Window):
    """
        Main application class.

        NOTE: Go ahead and delete the methods you don't need.
        If you do need a method, delete the 'pass' and replace it
        with your own code. Don't leave 'pass' in this program.
        """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables to determine which screens open at what time.
        self.main_menu_open = True
        self.difficulty_menu_open = False

        self.menus = None

        # sprite lists live here, using individual lists so that when we do collision checking different spells can
        # do different things to different enemies if we want.
        self.spell_list = None
        self.spell_firefury_list = None
        self.spell_waterblast_list = None
        self.spell_lightning_list = None
        self.enem_list = None
        self.enem_shambler_list = None
        self.base_list = None
        self.gui_list = None
        self.cursor_sprite = None
        self.magic_list = []
        self.health_list = []

        self.firefury_damage = 50
        self.waterblast_damage = 5
        self.lightning_damage = 200

        magic = make_magic()
        self.magic_list.append(magic)

        health = make_health()
        self.health_list.append(health)

        self.tree = None

        # set up score and 'money' variables
        self.score_earned = 0
        self.score_current = 0

        # base variables
        self.health_value = 100
        self.stop_x = 700
        self.kill_timer = 0

        # load spell casting variables
        self.selected_spell = 1
        self.magic_resource_percentage = 0.5
        self.magic_resource_replenish = 1
        self.magic_resource_spend_modifer = 1

        # load spell cost variables
        self.firefury_cost = 0.07
        self.waterblast_cost = 0.7
        self.lightning_cost = 1.00

        # variables to determine what upgrades the player has unlocked
        self.wall_level = 0
        self.spikes_level = 0
        """
                This part is to set the variable settings for what is open 
                """

        # Load Sounds
        self.firefury = arcade.load_sound("sounds/Firefury.wav")
        self.SpellChange = arcade.load_sound("sounds/SpellChange.wav")

        self.set_mouse_visible(False)
        
        #score
        self.score = 0

    def setup(self):
        # Create your sprites and sprite lists here

        self.spell_list = arcade.SpriteList()
        self.spell_firefury_list = arcade.SpriteList()
        self.spell_waterblast_list = arcade.SpriteList()
        self.spell_lightning_list = arcade.SpriteList()

        self.enem_list = arcade.SpriteList()
        self.enem_shambler_list = arcade.SpriteList()
        self.base_list = arcade.SpriteList()
        self.gui_list = arcade.SpriteList()

        # number of shamblers to spawn on this setup
        self.enem_pool_shambler = 20
        # the starting timing gap between spawning them for this setup
        self.enem_gap_shambler = 120

        self.cursor_sprite = arcade.Sprite("images/cursor/cursor1.png", CHARACTER_SCALING)
        self.cursor_sprite.center_x = 100
        self.cursor_sprite.center_y = 200
        self.gui_list.append(self.cursor_sprite)

        tree = arcade.Sprite("images/tree/tree1.png", TILE_SCALING)
        tree.center_x = 300
        tree.center_y = 300
        self.base_list.append(tree)

        # if (self.wall_level == 0):
        wall = arcade.Sprite("images/tree/wooden.png", TILE_SCALING)
        wall.center_x = 600
        wall.center_y = 200
        self.base_list.append(wall)
        
        #score
        self.score = 0

        # Declaring menu array and appending Menu object to it.
        self.menus = []
        menu = setup_menu_1()
        self.menus.append(menu)

    def on_draw(self):
        """
                Render the screen.
                """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # Draw the sky in the top two-thirds
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT * (1 / 3),
                                          arcade.color.SKY_BLUE)
        # Draw the ground in the bottom third
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_SPRING_GREEN)
        
        #Draw score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # Draw magic bar
        for magic in self.magic_list:
            arcade.draw_circle_filled(magic.x, magic.y, magic.height, arcade.color.LAVENDER_BLUE, 128)
            arcade.draw_arc_filled(magic.x, magic.y, magic.width, magic.height, magic.color, magic.s_angle,
                                   (360 * self.magic_resource_percentage), magic.tilt, magic.sections)
            arcade.draw_circle_outline(magic.x, magic.y, magic.height, arcade.color.REGALIA, 5, 128)

        if self.kill_timer > 1:
            arcade.draw_text("YOU HAVE FAILED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.CRIMSON_GLORY, 40)

        # Call draw() on all your sprite lists below

        self.spell_list.draw()
        self.spell_firefury_list.draw()
        self.spell_waterblast_list.draw()
        self.spell_lightning_list.draw()
        self.base_list.draw()
        self.enem_list.draw()
        self.enem_shambler_list.draw()

        # draw health bar

        for health in self.health_list:
            arcade.draw_lrtb_rectangle_filled(1200, 1200 + self.health_value, 700 + health.width, 700,
                                              arcade.color.CAMEO_PINK)
            arcade.draw_lrtb_rectangle_outline(1200, (1200 + health.max), 700 + health.width, 700,
                                               arcade.color.CANARY_YELLOW, 5)

        # Draw main menu
        if self.main_menu_open:
            self.menus[0].menu_background.draw()
            self.menus[0].menu_list1.draw()
            # self.menus[0].gui_list.draw()

        elif self.difficulty_menu_open:
            self.menus[0].menu_background.draw()
            self.menus[0].menu_list2.draw()

        self.gui_list.draw()

    def update(self, delta_time):
        """
                All the logic to move, and the game logic goes here.
                Normally, you'll call update() on the sprite lists that
                need it.
                """
        if not self.main_menu_open and not self.difficulty_menu_open:
            # update sprite lists
            self.spell_list.update()
            self.spell_firefury_list.update()
            self.spell_waterblast_list.update()
            self.spell_lightning_list.update()
            self.gui_list.update()
            self.enem_list.update()
            self.enem_shambler_list.update()

            # logic for spells
            for firefury in self.spell_firefury_list:
                if firefury.bottom > self.height or firefury.top < 0 or firefury.right < 0 or firefury.left > self.width:
                    firefury.kill()

            for waterblast in self.spell_waterblast_list:
                if waterblast.bottom > self.height or waterblast.top < 0 or waterblast.right < 0 or waterblast.left > self.width:
                    waterblast.kill()

            for lightning in self.spell_lightning_list:
                if lightning.top < 0 or lightning.right < 0 or lightning.left > self.width:
                    lightning.kill()

            # logic for enemies

            for shambler in self.enem_shambler_list:
                if shambler.bottom > self.width or shambler.top < 0 or shambler.right < 0:
                    print(shambler.health)
                    shambler.kill()
                    print("Shambler deleted")
                # if the unit runs out of health, kill it
                if shambler.health < 0:
                    shambler.kill()
                    self.score += 1
                    print("Shambler DESTROYED")

                if shambler.center_x < 700:
                    shambler.change_x = 0

                if shambler.attack_timer <= 0 and shambler.change_x == 0:
                    self.health_value -= 1
                    shambler.attack_timer = 90
                # Make hit lists
                shambler_fire_hit_list = arcade.check_for_collision_with_list(shambler, self.spell_firefury_list)
                shambler_water_hit_list = arcade.check_for_collision_with_list(shambler, self.spell_waterblast_list)
                shambler_lightning_hit_list = arcade.check_for_collision_with_list(shambler, self.spell_lightning_list)

                if len(shambler_fire_hit_list) > 0:
                    shambler.health -= self.firefury_damage

                for firefury in shambler_fire_hit_list:
                    firefury.remove_from_sprite_lists()

                if len(shambler_water_hit_list) > 0:
                    shambler.health -= self.waterblast_damage

                for waterblast in shambler_water_hit_list:
                    waterblast.remove_from_sprite_lists()

                if len(shambler_lightning_hit_list) > 0:
                    shambler.health -= self.lightning_damage

                for lightning in shambler_lightning_hit_list:
                    lightning.remove_from_sprite_lists()

                # manage the attack timing counter
                shambler.attack_timer -= 1

            # update magic resource bar

            if self.magic_resource_percentage < 1:
                self.magic_resource_percentage = (self.magic_resource_percentage + (self.magic_resource_replenish / 60))

            # code to generate a pool of enemies

            if self.enem_pool_shambler > 0 and self.enem_gap_shambler < 0:
                shambler = arcade.Sprite("images/enemies/enemy_shambler.png")
                shambler.center_x = 1800
                shambler.center_y = random.randint(50, 300)
                shambler.change_x = random.randint(-4, -1)
                shambler.health = random.randint(10, 50)
                shambler.attack_timer = 90
                self.enem_shambler_list.append(shambler)
                self.enem_pool_shambler -= 1
                self.enem_gap_shambler = random.randint(30, 180)

            # code for handling timing variables.
            self.enem_gap_shambler -= 1

            # lose game condition

            if self.health_value < 0:
                self.kill_timer += 1

            if self.kill_timer > 180:
                arcade.close_window()

    def on_key_press(self, key, key_modifiers):

        if key == (arcade.key.KEY_1 or arcade.key.NUM_1):
            self.selected_spell = 1
            # Plays sounds for changing spells, can make each sound different later
            arcade.play_sound(self.SpellChange)
            print("Spell 1 selected")

        if key == (arcade.key.KEY_2 or arcade.key.NUM_2):
            self.selected_spell = 2
            arcade.play_sound(self.SpellChange)
            print("Spell 2 selected")

        if key == (arcade.key.KEY_3 or arcade.key.NUM_3):
            self.selected_spell = 3
            arcade.play_sound(self.SpellChange)
            print("Spell 3 selected")

    def on_key_release(self, key, key_modifiers):
        """
                Called whenever the user lets off a previously pressed key.
                """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
                Called whenever the mouse moves.
                """
        # Move the center of the player sprite to match the mouse x, y
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
                Called when the user presses a mouse button.
                """

        # Navigating main menu
        if self.main_menu_open:
            if 1000 > x > 600 and 450 > y > 350:
                self.main_menu_open = False
                self.difficulty_menu_open = True

        elif self.difficulty_menu_open:
            if 1000 > x > 600 and 450 > y > 350:
                self.difficulty_menu_open = False

        # check selected spell and draw spell at caster location
        elif (self.selected_spell == 1) and (
                self.magic_resource_percentage > (self.magic_resource_spend_modifer * self.firefury_cost)):
            firefury = arcade.Sprite("images/spells/spell_firefury1.png", CHARACTER_SCALING)
            firefury.center_x = SPELL_CAST_X
            firefury.center_y = SPELL_CAST_Y
            self.magic_resource_percentage = self.magic_resource_percentage - self.firefury_cost
            # plays spell sound effect)
            arcade.play_sound(self.firefury)

            # grab mouse position to calculate aim
            destination_x = x
            destination_y = y

            difference_in_x = destination_x - SPELL_CAST_X
            difference_in_y = destination_y - SPELL_CAST_Y
            angle = math.atan2(difference_in_y, difference_in_x)

            # use calculated angle to rotate spell sprite
            firefury.angle = math.degrees(angle)

            # calc rates of change to move spell in right direction

            firefury.change_x = math.cos(angle) * FIRESPEED
            firefury.change_y = math.sin(angle) * FIRESPEED

            # append to sprite list
            self.spell_firefury_list.append(firefury)

        elif (self.selected_spell == 2) and (
                self.magic_resource_percentage > (self.magic_resource_spend_modifer * self.waterblast_cost)):
            waterblast = arcade.Sprite("images/spells/spell_waterblast1.png", CHARACTER_SCALING)
            waterblast.center_x = SPELL_CAST_X
            waterblast.center_y = SPELL_CAST_Y
            self.magic_resource_percentage = self.magic_resource_percentage - self.waterblast_cost
            # Code for sound effect will be here when sound found

            # grab mouse position to calculate aim
            destination_x = x
            destination_y = y

            difference_in_x = destination_x - SPELL_CAST_X
            difference_in_y = destination_y - SPELL_CAST_Y
            angle = math.atan2(difference_in_y, difference_in_x)

            # use calculated angle to rotate spell sprite
            waterblast.angle = math.degrees(angle)

            # calc rates of change to move spell in right direction
            waterblast.change_x = math.cos(angle) * WATERSPEED
            waterblast.change_y = math.sin(angle) * WATERSPEED

            # append to sprite list
            self.spell_waterblast_list.append(waterblast)


        elif (self.selected_spell == 3) and (
                self.magic_resource_percentage > (self.magic_resource_spend_modifer * self.lightning_cost)):
            lightning = arcade.Sprite("images/spells/spell_lightning2.png")
            lightning.center_x = x
            lightning.center_y = SCREEN_HEIGHT + 200
            self.magic_resource_percentage = self.magic_resource_percentage - self.lightning_cost

            # unlike other spells, lightning comes from the top of the screen
            lightning.angle = 0
            lightning.change_y = -LIGHTNINGSPEED

            self.spell_lightning_list.append(lightning)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
                Called when a user releases a mouse button.
                """
        pass


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
