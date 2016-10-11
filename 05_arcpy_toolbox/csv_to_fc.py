import arcpy

# Get the spatial reference from the tool dialog.
csv_file = arcpy.GetParameter(0)
output_folder = arcpy.GetParameter(1)
x_field = arcpy.GetParameter(2)
y_field = arcpy.GetParameter(3)
spatial_ref = arcpy.GetParameter(4)

# Display the Spatial Reference properties
arcpy.AddMessage("CSV file is: {0}".format(csv_file))
arcpy.AddMessage("Output location is: {0}".format(output_folder))
arcpy.AddMessage("X field is: {0}".format(x_field))
arcpy.AddMessage("Y field is: {0}".format(y_field))
arcpy.AddMessage("Spatial reference is: {0}".format(spatial_ref.name))

arcpy.SetParameter(5, 1423424)

"""
# get parameters
layer_alias = arcpy.GetParameterAsText(0)
layer_path = ""

if layer_alias == "counties":
    layer_path = "C:/pathto/data/" + layer_alias + ".shp" #"C:/pathto/data/counties.shp"

# do work
mxd = arcpy.mapping.MapDocument("CURRENT")
dataFrame = arcpy.mapping.ListDataFrames(mxd, "*")[0]
addLayer = arcpy.mapping.Layer(layer_path)
arcpy.mapping.AddLayer(dataFrame, addLayer)
"""
