import os
import xbmc
import time
import xbmcgui
i = 0
progress = xbmcgui.DialogProgress()
progress.create('Installing update','Installing system update')
progress.update( 10, "", '10%', "" )
time.sleep(0.5)
progress.update( 20, "", '20%', "" )
time.sleep(0.5)
progress.update( 30, "", '30%', "" )
time.sleep(0.5)
progress.update( 40, "", '40%', "" )
time.sleep(0.5)
progress.update( 50, "", '50%', "" )
time.sleep(0.5)
progress.update( 60, "", '60%', "" )
time.sleep(0.5)
progress.update( 70, "", '70%', "" )
time.sleep(0.5)
progress.update( 80, "", '80%', "" )
time.sleep(0.5)
progress.update( 90, "", '90%', "" )
time.sleep(0.5)
progress.update( 100, "", '100%', "" )
time.sleep(0.5)
xbmc.executebuiltin('Dialog.Close(all,true)')
xbmc.executebuiltin('ActivateWindow(1251)')