import xbmc
import xbmcgui
import time

progress = xbmcgui.DialogProgress()
progress.create('Installing theme','Installing theme')

# Update progress in a loop (you can adjust the delay and number of steps)
for i in range(1, 101):
    progress.update(i, "", f'{i}%', "")
    time.sleep(0.05)  # Adjust the delay as needed

progress.close()  # Combined closing methods for potential future changes
xbmc.executebuiltin('ActivateWindow(Home)')
