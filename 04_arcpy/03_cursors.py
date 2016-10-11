import arcpy

# print(arcpy.CheckExtension('spatial'))

# Search Cursors: https://pro.arcgis.com/en/pro-app/arcpy/functions/searchcursor.htm
# Insert Cursors: https://pro.arcgis.com/en/pro-app/arcpy/functions/insertcursor.htm
# Update Cursors: https://pro.arcgis.com/en/pro-app/arcpy/functions/updatecursor.htm

# We want COUNTY_NUM > 25
rows = arcpy.SearchCursor('counties', 'COUNTY_NUM = \'21\'')
for row in rows:
    print(row.COUNTY_NAM + ': ' + row.COUNTY_NUM)
