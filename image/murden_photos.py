import mysql.connector
import os.path
from os import path
outtxt = open("murden_photos.csv","w")

mydb = mysql.connector.connect(
  host="192.168.1.20",
  user="dmurdenadm",
  passwd="Rga05dba!",
  database="piwigo"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT file, path FROM piwigo_images")
myresult = mycursor.fetchall()

i = 1
for x in myresult:
    photo = str(path.exists('O:/Photos'+x[1][8:]))
    print(i,',"'+x[0].decode()+'","O:/Photos'+x[1][8:]+'",'+photo)
    outtxt.write("%i,""%s"",""%s"",""%s""\r" % (i,x[0].decode(),"O:/Photos"+x[1][8:],photo))
    i += 1

mydb.close()
outtxt.close()