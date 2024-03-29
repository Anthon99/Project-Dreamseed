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


FIRESPEED = 5
WATERSPEED = 15
LIGHTNINGSPEED = 50

CHARACTER_POS1 = 100
CHARACTER_POS2 = 250
CHARACTER_POS3 = 400


class UpgradeMenu:

    def __init__(self):
        # Upgrade menu sprite list
        self.upgrade_menu = None
        self.background_list = None
        self.menu_list = None

        self.active_wall1 = None
        self.active_fire1 = None
        self.active_lightning1 = None
        self.active_plasma1 = None
        self.active_water1 = None
        self.active_wall2 = None
        self.active_fire2 = None
        self.active_lightning2 = None
        self.active_plasma2 = None
        self.active_water2 = None

        self.wall1_details = None
        self.wall2_details = None
        self.fire1_details = None
        self.fire2_details = None
        self.lightning1_details = None
        self.lightning2_details = None
        self.plasma1_details = None
        self.plasma2_details = None
        self.water1_details = None
        self.water2_details = None


def setup_upgrade_menu():
    upgrade_menu = UpgradeMenu()

    # Appending upgrade menu sprites to lists
    upgrade_menu.background_list = arcade.SpriteList()
    upgrade_menu.menu_list = arcade.SpriteList()

    upgrade_menu.active_wall1 = arcade.SpriteList()
    upgrade_menu.active_fire1 = arcade.SpriteList()
    upgrade_menu.active_lightning1 = arcade.SpriteList()
    upgrade_menu.active_plasma1 = arcade.SpriteList()
    upgrade_menu.active_water1 = arcade.SpriteList()

    upgrade_menu.active_wall2 = arcade.SpriteList()
    upgrade_menu.active_fire2 = arcade.SpriteList()
    upgrade_menu.active_lightning2 = arcade.SpriteList()
    upgrade_menu.active_plasma2 = arcade.SpriteList()
    upgrade_menu.active_water2 = arcade.SpriteList()

    upgrade_menu.wall1_details = arcade.SpriteList()
    upgrade_menu.wall2_details = arcade.SpriteList()
    upgrade_menu.fire1_details = arcade.SpriteList()
    upgrade_menu.fire2_details = arcade.SpriteList()
    upgrade_menu.lightning1_details = arcade.SpriteList()
    upgrade_menu.lightning2_details = arcade.SpriteList()
    upgrade_menu.plasma1_details = arcade.SpriteList()
    upgrade_menu.plasma2_details = arcade.SpriteList()
    upgrade_menu.water1_details = arcade.SpriteList()
    upgrade_menu.water2_details = arcade.SpriteList()

    back_drop = arcade.Sprite("images/menu icons/MenuBackdrop.png", 1)
    back_drop.center_x = 800
    back_drop.center_y = 400
    upgrade_menu.background_list.append(back_drop)

    upgrade_text = arcade.Sprite("images/menu icons/Upgrade Text.png", 1)
    upgrade_text.center_x = 800
    upgrade_text.center_y = 400
    upgrade_menu.background_list.append(upgrade_text)

    next_icon = arcade.Sprite("images/menu icons/Next Round.png", 1)
    next_icon.center_x = 1300
    next_icon.center_y = 100
    upgrade_menu.menu_list.append(next_icon)

    # Upgrade menu icons
    wall_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active wall 1.png", 1)
    wall_icon_1.center_x = 665
    wall_icon_1.center_y = 650
    upgrade_menu.menu_list.append(wall_icon_1)

    active_wall_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Active wall 1.png", 1)
    active_wall_icon_1.center_x = 665
    active_wall_icon_1.center_y = 650
    upgrade_menu.active_wall1.append(active_wall_icon_1)

    wall_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active wall 1.png", 1)
    wall_icon_2.center_x = 765
    wall_icon_2.center_y = 650
    upgrade_menu.menu_list.append(wall_icon_2)

    active_wall_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Active wall 1.png", 1)
    active_wall_icon_2.center_x = 765
    active_wall_icon_2.center_y = 650
    upgrade_menu.active_wall2.append(active_wall_icon_2)

    fire_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active fire 1.png", 1)
    fire_icon_1.center_x = 100
    fire_icon_1.center_y = 650
    upgrade_menu.menu_list.append(fire_icon_1)

    active_fire_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Active fire 1.png", 1)
    active_fire_icon_1.center_x = 100
    active_fire_icon_1.center_y = 650
    upgrade_menu.active_fire1.append(active_fire_icon_1)

    fire_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active fire 1.png", 1)
    fire_icon_2.center_x = 200
    fire_icon_2.center_y = 650
    upgrade_menu.menu_list.append(fire_icon_2)

    active_fire_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Active fire 1.png", 1)
    active_fire_icon_2.center_x = 200
    active_fire_icon_2.center_y = 650
    upgrade_menu.active_fire2.append(active_fire_icon_2)

    lightning_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active lightning 1.png", 1)
    lightning_icon_1.center_x = 100
    lightning_icon_1.center_y = 550
    upgrade_menu.menu_list.append(lightning_icon_1)

    active_lightning_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Active lightning 1.png", 1)
    active_lightning_icon_1.center_x = 100
    active_lightning_icon_1.center_y = 550
    upgrade_menu.active_lightning1.append(active_lightning_icon_1)

    lightning_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active lightning 1.png", 1)
    lightning_icon_2.center_x = 200
    lightning_icon_2.center_y = 550
    upgrade_menu.menu_list.append(lightning_icon_2)

    active_lightning_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Active lightning 1.png", 1)
    active_lightning_icon_2.center_x = 200
    active_lightning_icon_2.center_y = 550
    upgrade_menu.active_lightning2.append(active_lightning_icon_2)

    plasma_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active plasma 1.png", 1)
    plasma_icon_1.center_x = 100
    plasma_icon_1.center_y = 450
    upgrade_menu.menu_list.append(plasma_icon_1)

    active_plasma_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Active plasma 1.png", 1)
    active_plasma_icon_1.center_x = 100
    active_plasma_icon_1.center_y = 450
    upgrade_menu.active_plasma1.append(active_plasma_icon_1)

    plasma_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active plasma 1.png", 1)
    plasma_icon_2.center_x = 200
    plasma_icon_2.center_y = 450
    upgrade_menu.menu_list.append(plasma_icon_2)

    active_plasma_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Active plasma 1.png", 1)
    active_plasma_icon_2.center_x = 200
    active_plasma_icon_2.center_y = 450
    upgrade_menu.active_plasma2.append(active_plasma_icon_2)

    water_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active water 1.png", 1)
    water_icon_1.center_x = 100
    water_icon_1.center_y = 350
    upgrade_menu.menu_list.append(water_icon_1)

    active_water_icon_1 = arcade.Sprite("images/menu icons/Upgrade Icons/Active water 1.png", 1)
    active_water_icon_1.center_x = 100
    active_water_icon_1.center_y = 350
    upgrade_menu.active_water1.append(active_water_icon_1)

    water_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Non-active water 1.png", 1)
    water_icon_2.center_x = 200
    water_icon_2.center_y = 350
    upgrade_menu.menu_list.append(water_icon_2)

    active_water_icon_2 = arcade.Sprite("images/menu icons/Upgrade Icons/Active water 1.png", 1)
    active_water_icon_2.center_x = 200
    active_water_icon_2.center_y = 350
    upgrade_menu.active_water2.append(active_water_icon_2)

    # Upgrade descriptions
    wall1_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/wall1_details.png")
    wall1_details_icon.center_x = 890
    wall1_details_icon.center_y = 575
    upgrade_menu.wall1_details.append(wall1_details_icon)

    wall2_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/wall2_details.png")
    wall2_details_icon.center_x = 990
    wall2_details_icon.center_y = 575
    upgrade_menu.wall2_details.append(wall2_details_icon)

    fire1_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/fire1_details.png")
    fire1_details_icon.center_x = 325
    fire1_details_icon.center_y = 575
    upgrade_menu.fire1_details.append(fire1_details_icon)

    fire2_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/fire2_details.png")
    fire2_details_icon.center_x = 425
    fire2_details_icon.center_y = 575
    upgrade_menu.fire2_details.append(fire2_details_icon)

    lightning1_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/lightning1_details.png")
    lightning1_details_icon.center_x = 325
    lightning1_details_icon.center_y = 475
    upgrade_menu.lightning1_details.append(lightning1_details_icon)

    lightning2_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/lightning2_details.png")
    lightning2_details_icon.center_x = 425
    lightning2_details_icon.center_y = 475
    upgrade_menu.lightning2_details.append(lightning2_details_icon)

    plasma1_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/plasma1_details.png")
    plasma1_details_icon.center_x = 325
    plasma1_details_icon.center_y = 375
    upgrade_menu.plasma1_details.append(plasma1_details_icon)

    plasma2_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/plasma2_details.png")
    plasma2_details_icon.center_x = 425
    plasma2_details_icon.center_y = 375
    upgrade_menu.plasma2_details.append(plasma2_details_icon)

    water1_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/water1_details.png")
    water1_details_icon.center_x = 325
    water1_details_icon.center_y = 275
    upgrade_menu.water1_details.append(water1_details_icon)

    water2_details_icon = arcade.Sprite("images/menu icons/Upgrade Details/water2_details.png")
    water2_details_icon.center_x = 425
    water2_details_icon.center_y = 275
    upgrade_menu.water2_details.append(water2_details_icon)

    return upgrade_menu


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
        self.max = 0
        self.current = 0


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
    magic.max = 100

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


class MyGame(arcade.Window):
    """
        Main application class.

        NOTE: Go ahead and delete the methods you don't need.
        If you do need a method, delete the 'pass' and replace it
        with your own code. Don't leave 'pass' in this program.
        """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.main_menu_open = True
        self.difficulty_menu_open = False
        self.upgrade_menu_open = False

        self.fire1_purchased = False
        self.fire2_purchased = False
        self.lightning1_purchased = False
        self.lightning2_purchased = False
        self.plasma1_purchased = False
        self.plasma2_purchased = False
        self.water1_purchased = False
        self.water2_purchased = False

        self.wall1_details_open = False
        self.wall2_details_open = False
        self.fire1_details_open = False
        self.fire2_details_open = False
        self.lightning1_details_open = False
        self.lightning2_details_open = False
        self.plasma1_details_open = False
        self.plasma2_details_open = False
        self.water1_details_open = False
        self.water2_details_open = False

        self.menus = None
        self.upgrade_menus = None
        self.upgrade_icons = None

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
        self.player_list = None
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

        # setting variable to track the players position for shooting. This is a bit of a hack and slash way of doing
        # it :(
        self.player_shoot_x = 0
        self.player_shoot_y = 0

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
        self.magic_resource_replenish = 0.2
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
        self.player_list = arcade.SpriteList()

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

        player = arcade.Sprite("images/player/wizard1.png", CHARACTER_SCALING)
        player.center_x = 600
        player.center_y = CHARACTER_POS2
        self.player_list.append(player)

        # if (self.wall_level == 0):
        wall = arcade.Sprite("images/tree/wooden.png", TILE_SCALING)
        wall.center_x = 600
        wall.center_y = 200
        self.base_list.append(wall)

        # Declaring menu array and appending Menu object to it.
        self.menus = []
        menu = setup_menu_1()
        self.menus.append(menu)

        # Declaring upgrade menu array and appending Menu object to it.
        self.upgrade_menus = []
        upgrade_menu = setup_upgrade_menu()
        self.upgrade_menus.append(upgrade_menu)

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

        # Draw magic bar

        if self.kill_timer > 1:
            arcade.draw_text("YOU HAVE FAILED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.CRIMSON_GLORY, 40)

        # Call draw() on all your sprite lists below

        self.base_list.draw()
        self.enem_list.draw()
        self.enem_shambler_list.draw()
        self.player_list.draw()
        self.spell_list.draw()
        self.spell_firefury_list.draw()
        self.spell_waterblast_list.draw()
        self.spell_lightning_list.draw()

        # draw health bar the reason there is a plus value after the width draw position is if you want to change the
        # thickness of the bars, use the added value to modify
        for health in self.health_list:
            arcade.draw_lrtb_rectangle_filled(1100, 1100 + self.health_value, 750 + 20, 750, arcade.color.CAMEO_PINK)
            arcade.draw_lrtb_rectangle_outline(1100, (1100 + health.max), 750 + 20, 750, arcade.color.CANARY_YELLOW, 5)

        for magic in self.magic_list:
            # arcade.draw_circle_filled(magic.x, magic.y, magic.height , arcade.color.LAVENDER_BLUE,
            # 128) arcade.draw_arc_filled(magic.x, magic.y, magic.width,  magic.height, magic.color, magic.s_angle,
            # (360* self.magic_resource_percentage), magic.tilt, magic.sections) arcade.draw_circle_outline(magic.x,
            # magic.y, magic.height , arcade.color.REGALIA, 5, 128)
            arcade.draw_lrtb_rectangle_filled(1100, 1100 + magic.max, 700 + 20, 700, arcade.color.REGALIA)
            arcade.draw_lrtb_rectangle_filled(1100, 1100 + (magic.max * self.magic_resource_percentage), 700 + 20, 700,
                                              arcade.color.LAVENDER_BLUE)
            arcade.draw_lrtb_rectangle_outline(1100, (1100 + magic.max), 700 + 20, 700, arcade.color.REGALIA, 5)

        # Draw main menu
        if self.main_menu_open:
            self.menus[0].menu_background.draw()
            self.menus[0].menu_list1.draw()

        if self.difficulty_menu_open:
            self.menus[0].menu_background.draw()
            self.menus[0].menu_list2.draw()

        if self.upgrade_menu_open:
            self.upgrade_menus[0].background_list.draw()
            self.upgrade_menus[0].menu_list.draw()

            if self.fire1_purchased:
                self.upgrade_menus[0].active_fire1.draw()
            if self.fire2_purchased:
                self.upgrade_menus[0].active_fire2.draw()
            if self.lightning1_purchased:
                self.upgrade_menus[0].active_lightning1.draw()
            if self.lightning2_purchased:
                self.upgrade_menus[0].active_lightning2.draw()
            if self.plasma1_purchased:
                self.upgrade_menus[0].active_plasma1.draw()
            if self.plasma2_purchased:
                self.upgrade_menus[0].active_plasma2.draw()
            if self.water1_purchased:
                self.upgrade_menus[0].active_water1.draw()
            if self.water2_purchased:
                self.upgrade_menus[0].active_water2.draw()

            if self.wall_level > 0:
                self.upgrade_menus[0].active_wall1.draw()
            if self.wall_level == 2:
                self.upgrade_menus[0].active_wall2.draw()

            if self.wall1_details_open:
                self.upgrade_menus[0].wall1_details.draw()
            if self.wall2_details_open:
                self.upgrade_menus[0].wall2_details.draw()
            if self.fire1_details_open:
                self.upgrade_menus[0].fire1_details.draw()
            if self.fire2_details_open:
                self.upgrade_menus[0].fire2_details.draw()
            if self.lightning1_details_open:
                self.upgrade_menus[0].lightning1_details.draw()
            if self.lightning2_details_open:
                self.upgrade_menus[0].lightning2_details.draw()
            if self.plasma1_details_open:
                self.upgrade_menus[0].plasma1_details.draw()
            if self.plasma2_details_open:
                self.upgrade_menus[0].plasma2_details.draw()
            if self.water1_details_open:
                self.upgrade_menus[0].water1_details.draw()
            if self.water2_details_open:
                self.upgrade_menus[0].water2_details.draw()

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
            self.player_list.update()

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
                    print("Shambler DESTROYED")

                # code for slowing effect from water
                if shambler.slow_timer > 0:
                    shambler.change_x = (shambler.base_speed * 0.5)
                else:
                    shambler.change_x = shambler.base_speed

                if shambler.center_x < 700:
                    shambler.change_x = 0

                if shambler.attack_timer <= 0 and shambler.change_x == 0:
                    self.health_value -= 1
                    print(self.health_value)
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
                    # cause a slowing effect when hit
                    shambler.slow_timer = 120

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
                shambler.base_speed = shambler.change_x
                shambler.health = random.randint(10, 50)
                shambler.attack_timer = 90
                shambler.slow_timer = 0
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

            # code to update shooting positions

            for player in self.player_list:
                self.player_shoot_x = player.center_x + 30
                self.player_shoot_y = player.center_y + 10

    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.LEFT:
            self.upgrade_menu_open = True

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

        if key == arcade.key.W:
            for player in self.player_list:
                if player.center_y == CHARACTER_POS1:
                    player.center_y = CHARACTER_POS2
                elif player.center_y == CHARACTER_POS2:
                    player.center_y = CHARACTER_POS3

        if key == arcade.key.UP:
            for player in self.player_list:
                if player.center_y == CHARACTER_POS1:
                    player.center_y = CHARACTER_POS2
                elif player.center_y == CHARACTER_POS2:
                    player.center_y = CHARACTER_POS3

        if key == (arcade.key.DOWN or arcade.key.S):
            for player in self.player_list:
                if player.center_y == CHARACTER_POS3:
                    player.center_y = CHARACTER_POS2
                elif player.center_y == CHARACTER_POS2:
                    player.center_y = CHARACTER_POS1

        if key == arcade.key.S:
            for player in self.player_list:
                if player.center_y == CHARACTER_POS3:
                    player.center_y = CHARACTER_POS2
                elif player.center_y == CHARACTER_POS2:
                    player.center_y = CHARACTER_POS1

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

        if self.upgrade_menu_open:
            if 690 > x > 640 and 675 > y > 625:
                self.wall1_details_open = True
            else:
                self.wall1_details_open = False
            if 790 > x > 740 and 675 > y > 625:
                self.wall2_details_open = True
            else:
                self.wall2_details_open = False
            if 125 > x > 75 and 675 > y > 625:
                self.fire1_details_open = True
            else:
                self.fire1_details_open = False
            if 225 > x > 175 and 675 > y > 625:
                self.fire2_details_open = True
            else:
                self.fire2_details_open = False

            if 125 > x > 75 and 575 > y > 525:
                self.lightning1_details_open = True
            else:
                self.lightning1_details_open = False

            if 225 > x > 175 and 575 > y > 525:
                self.lightning2_details_open = True
            else:
                self.lightning2_details_open = False

            if 125 > x > 75 and 475 > y > 425:
                self.plasma1_details_open = True
            else:
                self.plasma1_details_open = False

            if 225 > x > 175 and 475 > y > 425:
                self.plasma2_details_open = True
            else:
                self.plasma2_details_open = False

            if 125 > x > 75 and 375 > y > 325:
                self.water1_details_open = True
            else:
                self.water1_details_open = False

            if 225 > x > 175 and 375 > y > 325:
                self.water2_details_open = True
            else:
                self.water2_details_open = False

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
                Called when the user presses a mouse button.
                """

        # Navigating main menu
        if self.main_menu_open and 1000 > x > 600 and 450 > y > 350:
            self.main_menu_open = False
            self.difficulty_menu_open = True

        elif self.difficulty_menu_open:
            if 1000 > x > 600 and 450 > y > 350:
                self.difficulty_menu_open = False

        if self.upgrade_menu_open:

            if 1500 > x > 1100 and 150 > y > 50:
                self.upgrade_menu_open = False

            if 125 > x > 75 and 675 > y > 625:
                print("Fire 1 selected")
                self.fire1_purchased = True
            if self.fire1_purchased and 225 > x > 175 and 675 > y > 625:
                print("Fire 2 selected")
                self.fire2_purchased = True

            if 125 > x > 75 and 575 > y > 525:
                print("Lightning 1 selected")
                self.lightning1_purchased = True
            if self.lightning1_purchased and 225 > x > 175 and 575 > y > 525:
                print("Lightning 2 selected")
                self.lightning2_purchased = True

            if 125 > x > 75 and 475 > y > 425:
                print("Plasma 1 selected")
                self.plasma1_purchased = True
            if self.plasma1_purchased and 225 > x > 175 and 475 > y > 425:
                print("Plasma 2 selected")
                self.plasma2_purchased = True

            if 125 > x > 75 and 375 > y > 325:
                print("Water 1 selected")
                self.water1_purchased = True
            if self.water1_purchased and 225 > x > 175 and 375 > y > 325:
                print("Water 2 selected")
                self.water2_purchased = True

            if 690 > x > 640 and 675 > y > 625:
                print("Wall 1 selected")
                self.wall_level = 1
            if self.wall_level == 1 and 790 > x > 740 and 675 > y > 625:
                print("Wall 2 selected")
                self.wall_level = 2

        # check selected spell and draw spell at caster location
        if not self.main_menu_open and not self.difficulty_menu_open and not self.upgrade_menu_open:
            if (self.selected_spell == 1) and (
                    self.magic_resource_percentage > (self.magic_resource_spend_modifer * self.firefury_cost)):
                firefury = arcade.Sprite("images/spells/spell_firefury1.png", CHARACTER_SCALING)
                firefury.center_x = self.player_shoot_x
                firefury.center_y = self.player_shoot_y
                self.magic_resource_percentage = self.magic_resource_percentage - self.firefury_cost
                # plays spell sound effect)
                arcade.play_sound(self.firefury)

                # grab mouse position to calculate aim
                destination_x = x
                destination_y = y

                difference_in_x = destination_x - self.player_shoot_x
                difference_in_y = destination_y - self.player_shoot_y
                angle = math.atan2(difference_in_y, difference_in_x)

                # sets firing arc in front of character
                if angle > (1 / 6) and angle <= 3.1:
                    angle = (1 / 6)
                elif angle < 0 and angle < (-1 / 6):
                    angle = (-1 / 6)

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
                waterblast.center_x = self.player_shoot_x
                waterblast.center_y = self.player_shoot_y
                self.magic_resource_percentage = self.magic_resource_percentage - self.waterblast_cost
                # Code for sound effect will be here when sound found

                # grab mouse position to calculate aim
                destination_x = x
                destination_y = y

                difference_in_x = destination_x - self.player_shoot_x
                difference_in_y = destination_y - self.player_shoot_y
                angle = math.atan2(difference_in_y, difference_in_x)

                # sets firing arc in front of character
                if angle > (1 / 6) and angle <= 3.1:
                    angle = (1 / 6)
                elif angle < 0 and angle < (-1 / 6):
                    angle = (-1 / 6)

                print(angle)
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
