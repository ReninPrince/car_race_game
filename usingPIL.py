from PIL import Image 
  
def main(): 
    try: 
         #Relative Path 
        img = Image.open("cropped_racetrack.png") 
        width, height = img.size 
   
        img = img.resize((800, 600)) 
          
        #Saved in the same relative location 
        img.save("resizedcropped_racetrackpicture.png")  
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main() 

##def main(): 
##    try: 
##        #Relative Path 
##        img = Image.open("Car.png")  
##          
##        #Getting histogram of image 
##        print(img.histogram())
##          
##    except IOError: 
##        pass
##  
##if __name__ == "__main__": 
##    main() 


##def main(): 
##    try: 
##        #Relative Path 
##        img = Image.open("Car.png")  
##          
##        #In-place modification 
##        img.thumbnail((200, 200))  
##          
##        img.save("Car1.png") 
##    except IOError: 
##        pass
##  
##if __name__ == "__main__": 
##    main()

##filename = "Car1.png"
##with Image.open(filename) as image: 
##    width, height = image.size
##
##
##
##print(width,height)

##img = Image.open('rotated_racetrack.png')
######im.save('racetrack.png')
####
#####Angle given 
######img = img.rotate(90)  
######  
###### #Saved in the same relative location 
######img.save("rotated_racetrack.png") 
####
##width, height = img.size 
##print(width,height)  
##area = (60, 0, 310, 230) 
##img = img.crop(area) 
##  
###Saved in the same relative location 
##img.save("cropped_racetrack.png")


    
