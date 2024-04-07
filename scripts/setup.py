import os
import xbmc
import time
import xbmcgui

# Create progress dialog object
progress = xbmcgui.Dialog()
progress.text = 'Installing update'
progress.heading = 'Installing system update'

# Simulate progress (adjusted for xbmcgui 5.17)
for i in range(0, 101, 10):  # Update in 10% increments
    progress.update(i, 'Completed ' + str(i) + '%')
    time.sleep(0.5)

# Close progress dialog
progress.close()

# Activate window (assuming window 1251 still applies)
xbmc.executebuiltin('ActivateWindow(1251)')
