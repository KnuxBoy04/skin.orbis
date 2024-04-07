import os
import xbmc
import time
import xbmcgui

# Assuming total progress steps are 10 (modify as needed)
total_steps = 10

progress = xbmcgui.DialogProgress()
progress.create('Installing update','Installing system update')

# Update progress in smaller increments for smoother visuals
for i in range(1, total_steps + 1):
    progress_percent = int((i / total_steps) * 100)
    progress.update(progress_percent, "", str(progress_percent) + '%', "")
    time.sleep(0.2)  # Adjust sleep time as desired

progress.update(100, "", '100%', "")
xbmc.executebuiltin('Dialog.Close(all,true)')
xbmc.executebuiltin('ActivateWindow(1251)')
