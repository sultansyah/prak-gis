import arcpy
from random import randrange
import random

TheShapefile="C:\Users\ASUS\Documents\DATA KULIAH SEMESTER 7\Praktikum GIS\Digitasi Polygon\warkop.shp"
TheRows=arcpy.UpdateCursor(TheShapefile)

nama_warkop = ["Warkop Kenangan", "Warkop Kopi Tubruk", "Warkop Asik", "Warkop Santai", "Warkop Semangat Pagi", "Warkop Pahit Manis", "Warkop Ganteng", "Warkop Cantik", "Warkop Cinta Kopi", "Warkop Kupi-Kupi", "Warkop Cinta Rasa", "Warkop Sederhana", "Warkop Modern", "Warkop Rindu Kopi", "Warkop Pelipur Lara", "Warkop Gurih", "Warkop Nikmat", "Warkop Ceria", "Warkop Penuh Senyum", "Warkop Suka-Suka"]
jenis_warkop = ["Klasik", "Modern", "Kopi Tubruk", "Kopi Susu", "Kopi Hitam", "Warkop Keluarga", "Warkop Kekinian", "Warkop Tradisional", "Warkop Santai", "Warkop Ramai", "Warkop Hangat", "Warkop Pagi", "Warkop Malam", "Warkop Romantis", "Warkop Sejuk", "Warkop Penuh Cinta", "Warkop Cita Rasa", "Warkop Gaya Lama", "Warkop Pelipur Rindu", "Warkop Kekinian"]


for TheRow in TheRows:
    TheRow.setValue("Nama", random.choice(nama_warkop))
    
    TheRow.setValue("Jenis", random.choice(jenis_warkop))
    
    TheRow.setValue("Luas", randrange(5, 20))
    
    
    
    TheRows.updateRow(TheRow)