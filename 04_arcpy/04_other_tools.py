import arcpy

arcpy.MakeFeatureLayer_management('streams', selected_streams_layer, 'OBJECTID < 9000')
