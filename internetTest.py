import csv
import time
import socket
import pandas as pd

def check_internet():
  try:
    # create a socket and send a request to 8.8.8.8 (Google's Primary DNS server)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("8.8.8.8", 53))
    s.close()
    return True
  except socket.error:
    return False
  
import pandas as pd

empty = False;
try:
  pd.read_csv('internet_status.csv') 
except pd.errors.EmptyDataError:
  with open('internet_status.csv', 'w', newline='') as csvfile:
    #  initialize the CSV file
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'Is offline'])

count = 1;
while True:
  # check if the internet is offline
  is_offline = not check_internet()


  # get the current timestamp in the local system time
  timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  

  with open('internet_status.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    if(is_offline):
      count+=1
    if(count > 0): 
      # update the CSV file with the current status
      writer.writerow([timestamp, is_offline])
      count+=1
    if(count > 3): # stops displaying succesful requests
      count = 0
  
  # wait for 30 seconds before checking again
  time.sleep(30)
