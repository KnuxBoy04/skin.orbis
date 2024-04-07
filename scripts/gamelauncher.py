import os
import xbmc
import time
game = xbmc.getInfoLabel("Skin.String(gamelaunch)")
xbmc.executebuiltin('ReplaceWindow(9091)')
xbmc.executebuiltin('ReplaceWindow(9092)')
time.sleep(3) 
os.startfile(game)
