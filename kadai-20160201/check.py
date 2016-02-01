#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import datetime

print "Start...."
#mc = minecraft.Minecraft.create("cvcis01.progrape.jp")
mc = minecraft.Minecraft.create("bes-master.cis.nagasaki-u.ac.jp")
mc.postToChat("Hello Python by Hayashida")

# 自分のポジション(最初のレスポンス座標からの相対座標を返す)
#pos = mc.player.getPos()
#print pos
#print "End"