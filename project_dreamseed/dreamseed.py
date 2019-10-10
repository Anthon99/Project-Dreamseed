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
SELECTED_SPELL = 1
SPELL_CAST_X = 200
SPELL_CAST_Y = 400

FIRESPEED = 5

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
		self.tree = None
		
		
		self.set_mouse_visible(False)
		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

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
		self.spell_list.update()
		
		for firefury in self.spell_list:
			if firefury.bottom > self.width or firefury.top < 0 or firefury.right < 0 or firefury.left > self.width:
				firefury.kill()
				

	def on_key_press(self, key, key_modifiers):
		"""
		Called whenever a key on the keyboard is pressed.

		For a full list of keys, see:
		http://arcade.academy/arcade.key.html
		"""
		pass

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
		if SELECTED_SPELL == 1:
			firefury = arcade.Sprite("images/spells/spell_firefury1.png", CHARACTER_SCALING)
			firefury.center_x = SPELL_CAST_X
			firefury.center_y = SPELL_CAST_Y
			
			
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
