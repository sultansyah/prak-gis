import arcpy

TheShapefile="C:\Users\ASUS\Documents\DATA KULIAH SEMESTER 7\Praktikum GIS\Digitasi Polygon\Sawah.shp"

# Create an update cursor based on the shapefile

TheRows=arcpy.UpdateCursor(TheShapefile)

# Update the  row

from random import randrange
import random

nama_lain = ["Adnan", "Ariyanto", "Asih", "Darmawan", "Fajri", "Hartati", "Joko", "Kusnadi", "Lestari", "Maulana", "Nadia", "Purwanto", "Rahayu", "Sugito", "Triyono", "Utami", "Wahyuni", "Yulianto", "Zainal", "Abdul", "Bambang", "Cahaya", "Dwi", "Eko", "Fitriani", "Gita", "Hendro", "Ika", "Juli", "Kartika", "Lukman", "Murni", "Nur", "Ono", "Puspita", "Ratna", "Siti", "Taufik", "Umar", "Vina", "Widi", "Yanti", "Zahra", "Bagus", "Cahyo", "Dini", "Evi", "Feri", "Guntur", "Hanif", "Ismi", "Muhammad", "Ahmad", "Siti", "Lina", "Budi", "Andi", "Rina", "Dewi", "Fitri", "Nina", "Rahmat", "Indra", "Siti", "Wulan", "Nurul", "Rizki", "Ika", "Rudi", "Ivan", "Fahmi", "Anita", "Eka", "Irfan", "Lia", "Aulia", "Adi", "Nadia", "Surya", "Dina", "Rizka", "Dian", "Arif", "Eva", "Rina", "Ilham", "Citra", "Yanti", "Hadi", "Lita", "Yusuf", "Dewa", "Yani", "Wahyu", "Sari", "Andika", "Rika", "Ade", "Maya", "Bima", "Nindy", "Ryan", "Wulan", "Ismail"]

for TheRow in TheRows:
    TheRow.setValue("NamaPemili", random.choice(nama_lain))
    
    TheRows.updateRow(TheRow)