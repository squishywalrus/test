#!/usr/bin/python2

import pyglet
from pyglet.window import key

class player():
	def __init__(self, win_dimensions):
		self.image = pyglet.image.SolidColorImagePattern((0, 255, 0, 255)).create_image(32, 32)
		
		self.wwidth = win_dimensions[0]
		self.wheight = win_dimensions[1]
		
		#position
		self.x = 0
		self.y = (self.wheight/2) - 16
		
		#velocity
		self.dx = 0
		self.dy = 0
		self.max_x = 8
		self.max_y = 8
		
		#acceleration (should be constant)
		self.acc_x = 1
		self.acc_y = 1
		
		self.input = {}
		for foo in ['back', 'fwd', 'up', 'down']:
			self.input[foo] = False
		
	def draw(self):
		self.image.blit(self.x, self.y)
		
	def update(self):
		if self.input['up']:
			if self.dy < self.max_y:
				self.dy += self.acc_y
		elif self.input['down']:
			if self.dy > (-1 * self.max_y):
				self.dy -= self.acc_y
				
		if self.input['fwd']:
			if self.dx < self.max_x:
				self.dx += self.acc_x
		elif self.input['back']:
			if self.dx > (-1 * self.max_x):
				self.dx -= self.acc_x
				
		self.x += self.dx
		self.y += self.dy
		
		if self.x < 0:
			self.x = 0
		elif (self.x + self.image.width) > self.wwidth:
			self.x = (self.wwidth - self.image.width)
		
		if self.y < 0:
			self.y = 0
		elif (self.y + self.image.height) > self.wheight:
			self.y = (self.wheight - self.image.height)

def main():
	window = pyglet.window.Window(1280, 720)
	
	mans = player((1280, 720))
	
	@window.event
	def on_draw():
		window.clear()
		mans.update()
		mans.draw()

	#input events		
	@window.event
	def on_key_press(symbol, modifiers):
		if symbol == key.A:
			mans.input['back'] = True
		elif symbol == key.W:
			mans.input['up'] = True
		elif symbol == key.S:
			mans.input['down'] = True
		elif symbol == key.D:
			mans.input['fwd'] = True
			
	@window.event
	def on_key_release(symbol, modifiers):
		if symbol == key.A:
			mans.input['back'] = False
		elif symbol == key.W:
			mans.input['up'] = False
		elif symbol == key.S:
			mans.input['down'] = False
		elif symbol == key.D:
			mans.input['fwd'] = False
	
	pyglet.app.run()

if __name__ == "__main__":
	main()
