#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Nishadini Widanagamage
    Description:  The notebook calculate the total stream miles located within a 10 km buffer region aorund Flint Hills ecoregion.
    Date created: 09/16/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
import arcpy.management
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = r"C:\Users\nishadini\OneDrive - Kansas State University\Documents\GitHub\firstpythonscript-nishadiniwidanagamage\GISproject\ExerciseData.gdb" 

# Perform geoprocessing
# Selecting Flint Hills ecoregion
select_ecoregion = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

# Creating a 10 km buffer zone around the selected ecoregion
ecoregion_buffered = arcpy.analysis.Buffer(select_ecoregion, "Flinthills_buffered", "10 Kilometers")

# Clipping the major rivers in Kansas with buffered ecoregion
clipped_major_rivers = arcpy.analysis.Clip('ks_major_rivers', ecoregion_buffered, "clipped_ks_major_rivers")

# Saving clipped rivers into a feature class
clipped_rivers = arcpy.management.CopyFeatures(clipped_major_rivers, "Clipped_rivers")

# Calculating the clipped stream lengths in miles
stream_length_miles = arcpy.management.AddGeometryAttributes(clipped_rivers, 'LENGTH', 'MILES_US')

# Calculating the total stream length of clipped rivers feature class
total_stream_length = arcpy.analysis.Statistics(stream_length_miles, "total_stream_length", [["LENGTH", "SUM"]])



