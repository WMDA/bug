import cv2
import os 
from colorama import Fore
from decouple import config

def main():

    directory = config('screenshots')
    print(Fore.RED + 'Press any key to continue to the next picture.' + Fore.RESET)
    
    for file in os.listdir(directory) :
        if '.png' in file:
    
            img = cv2.imread(os.path.join(directory, file), cv2.IMREAD_ANYCOLOR)
    
            cv2.imshow(file, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()