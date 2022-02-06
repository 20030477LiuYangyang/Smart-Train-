import time
import cv2

# importing the requests library
import requests 
  
# defining the api-endpoint 
API_ENDPOINT = "https://c200-project.000webhostapp.com/updatedConnections.php"
  
# your API key here
# API_KEY = "rpC200IOTtrack!"
  
# your source code here
source_code = '''
print("testing!")

'''
  
# data to be sent to api
"""
data = {'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':source_code,
        'api_paste_format':'php'}
"""

# sending post request and saving response as response object
# r = requests.post(url = API_ENDPOINT, data = {'id':'1'+1, 'value':person})
  
# extracting response text 
#pastebin_url = r.text
#print("The pastebin URL is:%s"%pastebin_url)



hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0)

while True:
     ret, frame = cap.read()
     font = cv2.FONT_HERSHEY_SIMPLEX

     bounding_box_cordinates, weights =  hog.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
     person = 0
     for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
        cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        
        
     cv2.putText(frame, f'Total Persons : {person}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)   
     cv2.imshow('output', frame)  
     key = cv2.waitKey(1) & 0xFF
     if key == ord("q"):
        break

     r = requests.post(url = API_ENDPOINT, data = {'train_id':'1', 'train_car_id':1, 'person_count':person})
     starttime = time.time()
     time.sleep(3.0 - ((time.time() - starttime) % 3.0))

cap.release()
cv2.destroyAllWindows()

