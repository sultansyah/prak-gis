import arcpy
from random import randrange
import random

TheShapefile="C:\Users\ASUS\Documents\DATA KULIAH SEMESTER 7\Praktikum GIS\Digitasi Polygon\kios.shp"
TheRows=arcpy.UpdateCursor(TheShapefile)

nama_kios = ["Kios Maju", "Kios Jaya", "Kios Sejahtera", "Kios Bahagia", "Kios Barokah", "Kios Cemerlang", "Kios Berkah", "Kios Lancar", "Kios Bersaudara", "Kios Sukses", "Kios Sentosa", "Kios Bermanfaat", "Kios Binaan", "Kios Sejati", "Kios Berkat", "Kios Mandiri", "Kios Pintar", "Kios Rizki", "Kios Berjaya", "Kios Penuh"]
jenis_kios = ["Makanan", "Pakaian", "Elektronik", "Buku", "Kosmetik", "Mainan", "Perabotan", "Alat Rumah Tangga", "Peralatan Olahraga", "Kendaraan", "Perhiasan", "Kesehatan", "Musik", "Peralatan Komputer", "Perkebunan", "Seni dan Kerajinan", "Kesehatan Hewan", "Peralatan Dapur", "Perlengkapan Kecantikan", "Aksesoris"]

for TheRow in TheRows:
    TheRow.setValue("Nama", random.choice(nama_kios))
    
    TheRow.setValue("Jenis", random.choice(jenis_kios))
    
    TheRow.setValue("Luas", randrange(5, 20))
    
    
    
    TheRows.updateRow(TheRow)