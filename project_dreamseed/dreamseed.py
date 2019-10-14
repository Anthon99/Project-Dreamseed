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

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Project Dreamseed"

CHARACTER_SCALING = 1
TILE_SCALING = 4
MOB_SCALING = 0.5

#spell casting globals

SPELL_CAST_X = 200
SPELL_CAST_Y = 400

FIRESPEED = 5
WATERSPEED = 15

#class to store variables for drawing the magic pool
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
	
#Section for building functions

#function to display the magic pool
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




class MyGame(arcade.Window):
	"""
	Main application class.

	NOTE: Go ahead and delete the methods you don't need.
	If you do need a method, delete the 'pass' and replace it
	with your own code. Don't leave 'pass' in this program.
	"""

	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

		# If you have sprite lists, you should create them here,
		# and set them to None
		
		self.spell_list = None
		self.enem_list = None
		self.base_list = None
		self.gui_list = None
		self.cursor_sprite = None
		self.magic_list = []
		
		magic = make_magic()
		self.magic_list.append(magic)
		
		
		self.tree = None
		
		#load spell casting variables
		self.selected_spell = 1
		self.magic_resource_percentage = 0.5
		self.magic_resource_replenish = 1
		self.magic_resource_spend_modifer = 1
		
		#load spell cost variables
		self.firefury_cost = 0.07
		self.waterblast_cost = 0.7
		"""
		This part is to set the variable settings for what is open 
		"""
		
		self.set_mouse_visible(False)
		

	def setup(self):
		# Create your sprites and sprite lists here
		self.spell_list = arcade.SpriteList()
		self.enem_list = arcade.SpriteList()
		self.base_list = arcade.SpriteList()
		self.gui_list = arcade.SpriteList()
		
		
		
		self.cursor_sprite = arcade.Sprite("images/cursor/cursor1.png", CHARACTER_SCALING)
		self.cursor_sprite.center_x = 100
		self.cursor_sprite.center_y = 200
		self.gui_list.append(self.cursor_sprite)
		
		tree = arcade.Sprite("images/tree/tree1.png", TILE_SCALING)
		tree.center_x = 300
		tree.center_y = 300
		self.gui_list.append(tree)

	def on_draw(self):
		"""
		Render the screen.
		"""

		# This command should happen before we start drawing. It will clear
		# the screen to the background color, and erase what we drew last frame.
		arcade.start_render()
		# Draw the sky in the top two-thirds
		arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_HEIGHT * (1 / 3), arcade.color.SKY_BLUE)
		# Draw the ground in the bottom third
		arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_SPRING_GREEN)
		
		#Draw magic bar
		for magic in self.magic_list:
			arcade.draw_circle_filled(magic.x, magic.y, magic.height , arcade.color.LAVENDER_BLUE, 128)
			arcade.draw_arc_filled(magic.x, magic.y, magic.width,  magic.height, magic.color, magic.s_angle, (360* self.magic_resource_percentage), magic.tilt, magic.sections)
			arcade.draw_circle_outline(magic.x, magic.y, magic.height , arcade.color.REGALIA, 5, 128)
		# Call draw() on all your sprite lists below
		self.gui_list.draw()
		self.spell_list.draw()
		self.base_list.draw()
		self.enem_list.draw()

	

	def update(self, delta_time):
		"""
		All the logic to move, and the game logic goes here.
		Normally, you'll call update() on the sprite lists that
		need it.
		"""
		
		#update sprite lists
		self.spell_list.update()
		self.gui_list.update()
		
		#logic for spells
		for firefury in self.spell_list:
			if firefury.bottom > self.width or firefury.top < 0 or firefury.right < 0 or firefury.left > self.width:
				firefury.kill()
				
		for waterblast in self.spell_list:
			if waterblast.bottom > self.width or waterblast.top < 0 or waterblast.right < 0 or waterblast.left > self.width:
				waterblast.kill()
		#update magic resource bar
		
		
		if self.magic_resource_percentage < 1:
			self.magic_resource_percentage = (self.magic_resource_percentage + (self.magic_resource_replenish/60))
			
			


	def on_key_press(self, key, key_modifiers):
		
		if key == (arcade.key.KEY_1 or arcade.key.NUM_1):
			self.selected_spell = 1
			print ("Spell 1 selected")
		
		if key == (arcade.key.KEY_2 or arcade.key.NUM_2):
			self.selected_spell = 2
			print ("Spell 2 selected")
		
		

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
		#check selected spell and draw spell at caster location
		if (self.selected_spell == 1) and (self.magic_resource_percentage > (self.magic_resource_spend_modifer * self.firefury_cost)):
			firefury = arcade.Sprite("images/spells/spell_firefury1.png", CHARACTER_SCALING)
			firefury.center_x = SPELL_CAST_X
			firefury.center_y = SPELL_CAST_Y
			self.magic_resource_percentage = self.magic_resource_percentage - self.firefury_cost
			
			
			#grab mouse position to calculate aim
			destination_x = x
			destination_y = y
			
			difference_in_x = destination_x - SPELL_CAST_X
			difference_in_y = destination_y - SPELL_CAST_Y
			angle = math.atan2(difference_in_y, difference_in_x)
			
			#use calculated angle to rotate spell sprite
			firefury.angle = math.degrees(angle)
			
			#calc rates of change to move spell in right direction
			
			firefury.change_x = math.cos(angle) * FIRESPEED
			firefury.change_y = math.sin(angle) * FIRESPEED
			
			#append to sprite list
			self.spell_list.append(firefury)

		elif (self.selected_spell == 2) and (self.magic_resource_percentage > (self.magic_resource_spend_modifer * self.waterblast_cost)):
			waterblast = arcade.Sprite("images/spells/spell_waterblast1.png", CHARACTER_SCALING)
			waterblast.center_x = SPELL_CAST_X
			waterblast.center_y = SPELL_CAST_Y
			self.magic_resource_percentage = self.magic_resource_percentage - self.waterblast_cost
			
			#grab mouse position to calculate aim
			destination_x = x
			destination_y = y
			
			difference_in_x = destination_x - SPELL_CAST_X
			difference_in_y = destination_y - SPELL_CAST_Y
			angle = math.atan2(difference_in_y, difference_in_x)
			
			#use calculated angle to rotate spell sprite
			waterblast.angle = math.degrees(angle)
			
			#calc rates of change to move spell in right direction
			
			waterblast.change_x = math.cos(angle) * WATERSPEED
			waterblast.change_y = math.sin(angle) * WATERSPEED
			
			#append to sprite list
			self.spell_list.append(waterblast)
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
