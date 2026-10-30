import os

os.system(
    'am start -a android.intent.action.INSERT -d'
    ' content://com.android.calendar/events --esa title "Dawam"'
)
