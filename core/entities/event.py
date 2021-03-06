# superclass for any events that might be generated by an object and sent to the EventManager
class Event:
	def __init__(self):
		self.name = "Generic Event"

# SYSTEM EVENTS
class GameStartedEvent(Event):
	def __init__(self):
		self.name = "Game Started Event"

class TickEvent(Event):
	def __init__(self):
		self.name = "CPU Tick Event"

class QuitEvent(Event):
	def __init__(self):
		self.name = "Program Quit Event"

# MAP EVENTS
class MapLoadedEvent(Event):
	def __init__(self, tilemap):
		self.name = "Map Loaded Event: " + str(tilemap)
		self.tilemap = tilemap

class TileSelectedEvent(Event):
	def __init__(self, selected_tile, pos):
		self.name = "Tile Selected Event: " + str(selected_tile)
		self.selected_tile = selected_tile
		self.pos = pos

class TileUnselectedEvent(Event):
	def __init__(self):
		self.name = "Tile Unselected Event"

# TURN EVENTS
class NextTurnEvent(Event):
	def __init__(self, turnnumber):
		self.name = "Next Turn Event: " + str(turnnumber)
		self.turn = turnnumber

class NextOneEvent(Event):
	def __init__(self, actual_player):
		self.name = "Next Player Event: " + str(actual_player)
		self.actual_player = actual_player

# UNIT EVENTS
class UnitSpawnedEvent(Event):
	def __init__(self, unit, (pos_x, pos_y)):
		self.name = "Unit Spawned Event: " + str(unit)
		self.unit = unit
		self.pos = (pos_x, pos_y)

class UnitMoveRequest(Event):
	def __init__(self, unit, (rel_x, rel_y)):
		self.name = "Unit Move Request unit=" + str(unit) + " rel=" + str((rel_x, rel_y))
		self.unit = unit
		self.pos = (rel_x, rel_y)

class UnitMovedEvent(Event):
	def __init__(self, unit):
		self.name = "Unit Moved Event unit=" + str(unit)
		self.unit = unit

class UnitSelectedEvent(Event):
	def __init__(self, unit, moves=[]):
		self.name = "Unit Selected Event: " + str(unit) + " moves=" + str(len(moves))
		self.unit = unit
		self.moves = moves

class UnitUnselectedEvent(Event):
	def __init__(self):
		self.name = "Unit Unselected Event"

# BUILDING EVENTS
class BuildingBuiltEvent(Event):
	def __init__(self, bld, (pos_x, pos_y)):
		self.name = "Building Built Event: bld=" + bld.name + " x=" + str(bld.pos_x) + " y=" + str(bld.pos_y)
		self.bld = bld
		self.pos = (pos_x, pos_y)

class BuildingSelectedEvent(Event):
	def __init__(self, bld):
		self.name = "Building Selected Event bld=" + bld.name + " x=" + str(bld.pos_x) + " y=" + str(bld.pos_y)
		self.building = bld

# INPUT EVENTS
class MouseClickedEvent(Event):
	def __init__(self, pos):
		self.name = "Mouse Clicked Event: pos=" + str(pos)
		self.pos = pos

class MouseRightClickedEvent(Event):
	def __init__(self, pos):
		self.name = "Mouse RightClicked Event: pos=" + str(pos)
		self.pos = pos

class KeyPressedEvent(Event):
	def __init__(self, key):
		self.name = "Key Pressed Event: key=" + str(key)
		self.key = key

# GUI EVENTS
class GuiPanelAddedEvent(Event):
	def __init__(self, anchor, panel):
		self.name = "Panel Added Event: " + str(panel)
		self.anchor = anchor
		self.panel = panel

class GuiPanelUpdatedEvent(Event):
	def __init__(self, panel, action="updated"):
		self.name = "Panel Updated Event: [" + action + "] " + str(panel)
		self.panel = panel
		self.action = action

class GuiWidgetFocusedEvent(Event):
	def __init__(self, widget):
		self.name = "Widget Focused Event: widget=" + str(widget)
		self.widget = widget

class GuiWidgetUnfocusedEvent(Event):
	def __init__(self, widget):
		self.name = "Widget Unfocused Event: widget=" + str(widget)
		self.widget = widget

