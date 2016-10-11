import arcpy

if arcpy.Exists(feature_class_name):
    result = arcpy.GetCount_management(feature_class_name)
    count = result.getOutput(0)