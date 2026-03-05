#from time import sleep

#def traffic_light():
#    for i in range(10):
#        print("stop")
#        print("Red")
#        sleep(5)
        
#        print("Get Ready")
#        print("Yellow")
#        sleep(5)

#        print("Go")
#        print("Green")
#
#traffic_light()

import re
text="cat hat bat"
matches=re.findall("c.t",text)
print(matches)