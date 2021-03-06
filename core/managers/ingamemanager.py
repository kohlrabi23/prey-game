from core.entities.player import Player
from core.entities.event import *

# import pygame key constants
from pygame_sdl2 import *

# Manager class for players & turn methods
class IngameManager:
	_tag = "IngameManager: "

	actual_turn = 0
	actual_player = None
	actual_player_num = -1

	players = []
	_last_player_id = -1

	# add nature player (num=0) on the beginning
	def __init__(self, eventmanager):
		#register in EventManager
		self._eventmgr = eventmanager
		self._eventmgr.register_listener(self)

		# create nature player
		nature = Player()
		nature.name = "Nature"
		nature.color = (0, 0, 0)
		self.add_player(nature)

	def start_game(self):
		# set turn=0 and player=1
		self.actual_turn = 0
		actual_player_num = 1
		self.change_actual_player(1)

	# add a player by class
	def add_player(self, player):
		# add player number to player and add all to player list
		new_player = player
		new_player.num = self.next_player_number()
		self.players.append(new_player)
		# debug: log player addition
		print (self._tag + "added player name=" + new_player.name + " on number " + str(new_player.num))

	# add a new player by name and color
	def add_new_player(self, player_name, (r, g, b)):
		new_player = Player()
		new_player.name = player_name
		new_player.color = (r, g, b)
		self.add_player(new_player)

	def change_actual_player(self, player_num):
		# update player
		self.actual_player_num = player_num
		self.actual_player = self.players[player_num]
		# fire NextOneEvent
		ev_nextone = NextOneEvent(self.actual_player)
		self._eventmgr.fire(ev_nextone)

	# internal: end turn and start a next one
	def next_turn(self):
		# next turn
		self.actual_turn += 1
		# trigger NextTurnEvent
		ev_nextturn = NextTurnEvent(self.actual_turn)
		self._eventmgr.fire(ev_nextturn)
		# player one starts
		actual_player_num = 1
		self.change_actual_player(actual_player_num)

	# internal: end turn of the actual player and switch to next one
	def next_one(self):
		# next player
		actual_player_num = self.actual_player_num + 1
		self.change_actual_player(actual_player_num)

	# switch player or update turn, "End Turn" button beheaviour
	def forward(self):
		player_count = len(self.players) -1
		# player isn't the last one
		if player_count - self.actual_player_num > 0:
			self.next_one()
		# player is the last one this turn
		elif player_count - self.actual_player_num  == 0:
			self.next_turn()

	# internal: get next player number
	def next_player_number(self):
		self._last_player_id += 1
		return self._last_player_id

	def on_event(self, event):
		if isinstance(event, GameStartedEvent):
			self.start_game()

		if isinstance(event, MouseClickedEvent):
			pass

		if isinstance(event, KeyPressedEvent):
			key = event.key
			if key == K_SPACE:
				self.forward()


