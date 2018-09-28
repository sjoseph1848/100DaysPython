import time
import webbrowser


#Fun app that runs every 2 hours, 4X while I am working to play a song to remind me to take a break
#we need to schedule a timer that starts then stops at 2 hours 
#We neeed to open the browser to run 
#the browser needs to go to the specific page for the song (Youtube)
url = 'https://asuonline.asu.edu/online-degree-programs/graduate/computer-science-mcs'
count = 0
while count <= 4:
  print ("Start : %s" % time.ctime())
  time.sleep(1)
  webbrowser.open_new(url)
  print ("End : %s" % time.ctime())
  count += 1
