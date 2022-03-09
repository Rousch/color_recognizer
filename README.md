# color_recognizer

I mitt program har jag använt mig av både pandas och NumPy då jag skriver i både text och nman på färger mm. men även färgernas RGB-värden dvs. siffror. Pandas för att enklare skriva i bokstäver och NumPy för enklare med siffrorna i bildernas RGB-värden.
```
import numpy as np
import pandas as pd
import cv2
```
Cv2 använder jag för att läsa av bilderna som jag skickar in i mitt program.

Sedan döper jag om min bild som jag laddat ned till min mapp och använder cv2 för att processera den. Jag döper om den för att enkelt kunna byta mellan olika bilder som jag har i min mapp. 

Sedan använder vi oss av våran csv-fil som innehåller alla färger och delar upp värdena i filen med dess respektive namn och RGB-värden.

Vi gör en klick-funktion som inte ska ge någon färg förän vi klickar.

Sedan definierar vi 2 funktioner för programmet. Det första är för att läsa av en färg vilket vi gör med RGB-värdena som vi har läst in från vår csv-fil. Denna funktion fungerar så att den tar de närmaste värdena den kan hitta för att läsa av en färg.
```
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
```

Den andra funktionen som vi definierar är våran klick-funktion. Denna funktion har vi att den läser av RGB-värdena från våran muspekare när vi dubbelklickar. 
```
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
```
Efter funktionerna är skapade så ska vi köra vårt program vilket vi gör genom att vi öppnar ett fönster med cv2 där bilden kan dyka upp i. 

Till sist så skapar vi en while-loop med våra funktioner intigrerade och skapar en text string som ska då kunna säga vilken färg och vilka RGB-värden som dyker upp när vi klickar. Den läser av RGB-värdena och ger namnet på färgen med vit text på en bakgrund med färgen som vi klickat på så att man får en bättre syn på den. Vi har även en liten if-sats som ändrar textens färg om färgen vi klickar på är ljus så att man ska kunna läsa den. 
```
while(1):
    cv2.imshow("Färganalys",färgglad_bild)
    if (clicked):
   
        cv2.rectangle(färgglad_bild,(20,20), (750,60), (b,g,r), -1)
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        cv2.putText(färgglad_bild, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(färgglad_bild, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
    if cv2.waitKey(20) & 0xFF ==27:
            break

cv2.destroyAllWindows()
```
Till sist så skapar vi ett sätt att stänga ned vårt programm då det är en while-loop och annars kommer pågå för evigt. I detta fall har vi satt "esc" som vår anstängningsknapp. 

För att köra programmet så behöver man en bild. Denna bild ska laddas ned och läggas in i samma mapp som din programeringskod. I detta fall har jag bara använt mig av och testat jpg-bilder. Du refererar till bilden med dess namn och bildtyp där du döper om den. Sedan öppnar du en terminal och skriver följande: python *ditt programs namn*.py
Nu kan du köra programmet. 

Syftet med detta program var att lösa ett problem jag kan stöta på i vardan vilket i detta fall är min färgblindhet. Därför är detta ett bra program för mig, men jag kan snabbt se en förbättring som man kan göra. En förbättring som jag skulle vilja ha är att man ska kunna köra 2 bilder samtidigt så att man skulle kunna jämföra dom direkt. Just nu så skulle man behöva byta ut bild och starta om programmet för att se en annan bild vilket går ganska snabbt men är en förbättring som jag kan se kan göras. 
