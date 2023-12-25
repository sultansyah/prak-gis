import arcpy
from random import randrange
import random

TheShapefile="C:\Users\ASUS\Documents\DATA KULIAH SEMESTER 7\Praktikum GIS\Digitasi Polygon\kede.shp"
TheRows=arcpy.UpdateCursor(TheShapefile)

nama_toko = ["Toko Makmur", "Toko Jaya", "Toko Berkat", "Toko Baru", "Toko Sejahtera", "Toko Abadi", "Toko Harmoni", "Toko Sentosa", "Toko Indah", "Toko Maju"]
jenis_toko = ["Elektronik", "Pakaian", "Makanan", "Perhiasan", "Olahraga", "Alat Rumah Tangga", "Buku", "Kosmetik", "Mainan", "Kendaraan"]

for TheRow in TheRows:
    TheRow.setValue("Nama", random.choice(nama_toko))
    
    TheRow.setValue("Luas", randrange(5, 20))
    
    TheRow.setValue("Jenis", random.choice(jenis_toko))
    
    
    TheRows.updateRow(TheRow)