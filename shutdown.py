import os



sd = input('La revedere?')

if sd == str.lower('Da'):
    os.system('taskkill /im uTorrent.exe')
    os.system('taskkill /im Origin.exe')
    os.system("shutdown /s /t 1")
else:
    exit()
