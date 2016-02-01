#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block

#mc = minecraft.Minecraft.create("cvcis01.progrape.jp")
mc = minecraft.Minecraft.create("bes-master.cis.nagasaki-u.ac.jp")
pos = mc.player.getPos()
#mc.postToChat(pos)
#mc.postToChat("Hello Python by Hayashida")

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
		mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.AIR.id)
'''
for i in range(1, 5):
    for j in range(0, 5):
        for k in range(1, 5):
		if i == 0 or i == 9:
			mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.BRICK_BLOCK.id)
		if j == 9:
			mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.BRICK_BLOCK.id)
		if k == 0 or k == 9:
			mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.BRICK_BLOCK.id)
			#mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.BRICK_BLOCK.id)
'''