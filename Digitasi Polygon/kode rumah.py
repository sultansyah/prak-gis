import arcpy

TheShapefile="C:\Users\ASUS\Documents\DATA KULIAH SEMESTER 7\Praktikum GIS\Digitasi Polygon\Rumah.shp"

# Create an update cursor based on the shapefile

TheRows=arcpy.UpdateCursor(TheShapefile)

# Update the  row

from random import randrange
import random
nama_orang = ["Muhammad", "Ahmad", "Siti", "Lina", "Budi", "Andi", "Rina", "Dewi", "Fitri", "Nina", "Rahmat", "Indra", "Siti", "Wulan", "Nurul", "Rizki", "Ika", "Rudi", "Ivan", "Fahmi", "Anita", "Eka", "Irfan", "Lia", "Aulia", "Adi", "Nadia", "Surya", "Dina", "Rizka", "Dian", "Arif", "Eva", "Rina", "Ilham", "Citra", "Yanti", "Hadi", "Lita", "Yusuf", "Dewa", "Yani", "Wahyu", "Sari", "Andika", "Rika", "Ade", "Maya", "Bima", "Nindy", "Ryan", "Wulan", "Ismail"]
nama_lain = ["Adnan", "Ariyanto", "Asih", "Darmawan", "Fajri", "Hartati", "Joko", "Kusnadi", "Lestari", "Maulana", "Nadia", "Purwanto", "Rahayu", "Sugito", "Triyono", "Utami", "Wahyuni", "Yulianto", "Zainal", "Abdul", "Bambang", "Cahaya", "Dwi", "Eko", "Fitriani", "Gita", "Hendro", "Ika", "Juli", "Kartika", "Lukman", "Murni", "Nur", "Ono", "Puspita", "Ratna", "Siti", "Taufik", "Umar", "Vina", "Widi", "Yanti", "Zahra", "Bagus", "Cahyo", "Dini", "Evi", "Feri", "Guntur", "Hanif", "Ismi"]

for TheRow in TheRows:
    TheRow.setValue("NoRumah", randrange(1, 400))
    
    TheRow.setValue("NamaPemili", random.choice(nama_orang))
    
    TheRow.setValue("NoKTPPemil", randrange(1, 100000))
    
    TheRow.setValue("NoTlpnPemi", randrange(1, 100000))
    
    TheRow.setValue("NamaPenghu", random.choice(nama_lain))
    
    TheRow.setValue("NoKTPPengh", randrange(1, 100000))
    
    jumlah_lk = randrange(20)
    jumlah_pr = randrange(20)
    total_huni = jumlah_lk + jumlah_pr
    
    TheRow.setValue("jumlah_lk", jumlah_lk)
    TheRow.setValue("jumlah_pr", jumlah_pr)
    TheRow.setValue("total_huni", total_huni)
    
    TheRows.updateRow(TheRow)