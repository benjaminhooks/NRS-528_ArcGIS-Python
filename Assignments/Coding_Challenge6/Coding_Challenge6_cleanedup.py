import arcpy, os

listMonths = ["02", "04", "05", "07", "10", "11"]
outputDirectory = r"C:\NRS_528\Classes\06_Cheating\Step_3_Data"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

from arcpy.sa import *

for month in listMonths:
    arcpy.env.workspace = os.path.join(outputDirectory, "2015" + str(month))
    listRasters = arcpy.ListRasters("*", "TIF")

    listRasterVis = [x for x in listRasters if "B4" in x]
    listRasterNIR = [x for x in listRasters if "B5" in x]

    print("Creating NVDI raster from " + str(listRasterVis) + str(listRasterNIR))

    output_raster = (Raster(listRasterNIR) - Raster(listRasterVis)) / (Raster(listRasterNIR) + Raster(listRasterVis))
    output_raster.save(os.path.join(outputDirectory, "2015" + str(month) + "_NDVI.tif"))
