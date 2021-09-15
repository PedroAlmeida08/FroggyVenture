import Globals as gl
import pickle
import World
from os import path

def reset_level(level, player):
    player.reset(64, gl.HEIGHT - (gl.SIZE * 7))
    gl.mushroom_group.empty()
    gl.check_group.empty()
    if path.exists('./Assets/Level/level{}_data'.format(level)):
        pickle_in = open('./Assets/Level/level{}_data'.format(level), 'rb')
        world_data = pickle.load(pickle_in)
    world = World.World(world_data)

    return world
