import numpy as np
import pandas as pd
import cv2

färgglad_bild = cv2.imread("color_meets_the_eye.jpg")

#vi hämtar och läser in våran csv-fil med "alla" våra färger med deras RGB-värden
index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#om klicket inte går så blir det ingen färg
clicked = False
r = g = b = xpos = ypos = 0

#det är här som programmet läser av färgen där vi klickar med musen 
def recognize_color(R,G,B):
    minimum = 10000
#här hitter vi färg genom att ta de närmsta RGB-värdena och avläser dom
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


#här läser programmet av vår klick och des koordinater
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = färgglad_bild[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

#här öppnar vi våran bild
cv2.namedWindow('Färganalys')
cv2.setMouseCallback('Färganalys', mouse_click)

#under så skapar vi en text string med färgad bakgrund som ger oss färgens namn och RGB-värden
while(1):
    cv2.imshow("Färganalys",färgglad_bild)
    if (clicked):
   
#här positionerar vi våran lilla textruta 
        cv2.rectangle(färgglad_bild,(20,20), (750,60), (b,g,r), -1)
#här skrivs färgens namn och RGB-värden
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
#här fixar vi textens design osv.
        cv2.putText(färgglad_bild, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
#här fixar vi så att textens fär blir mörk om färgen vi valt var väldigt ljus
        if(r+g+b>=600):
            cv2.putText(färgglad_bild, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
#här avslutas programmet med "esc"
    if cv2.waitKey(20) & 0xFF ==27:
            break

cv2.destroyAllWindows()
