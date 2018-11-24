import os
try:
    print ("osX")
    os.system("python3 -m pip install requests")
    os.system("python3 -m pip install beautifulsoup4")
except:
    print("windows")
    os.system("py -3 -m pip install requests")
    os.system("y -3 -m pip install beautifulsoup4")
