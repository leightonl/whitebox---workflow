import os
import pkg_resources
import whitebox

wbt = whitebox.WhiteboxTools()

print("************************Performing Fill Burn Tool**************************************")
wbt.fill_burn(dem="C:/Work/Whitebox/DEM_Bankan_AW3D30.tif", #Input DEM
              streams="C:/Work/Whitebox/rivers_Bankan.shp", #Input rivers shapefile
              output="C:/Work/Whitebox/output/Fill_burn.tif")

print("*************************Performing flow_accumulation_full_workflow********************")
wbt.flow_accumulation_full_workflow(
    dem = "C:/Work/Whitebox/output/Fill_burn.tif", #line 10 output DEM used as input DEM
    out_type = "Catchment Area",
    out_dem = "C:/Work/Whitebox/output/FlowAccu_dem.tif", #output flow accumulation DEM
    out_accum = "C:/Work/Whitebox/output/FlowAccu_file.tif", #output flow accumulation file
    out_pntr = "C:/Work/Whitebox/output/FlowAccu_pntr.tif", #output flow pointer file
)

print("**************************Now Extracting Streams***************************************")
wbt.extract_streams(
    flow_accum = "C:\Work\Whitebox\output\FlowAccu_file.tif", #line 16 output flow accumulation DEM as input
    output = "C:\Work\Whitebox\output\output_streams.tif",
    threshold = 1000
)

print("*************************Converting raster streams to vector****************************")
wbt.raster_streams_to_vector(
    streams = "C:\Work\Whitebox\output\output_streams.tif",
    d8_pntr = "C:\Work\Whitebox\output\FlowAccu_pntr.tif", #line 17 output flow pointer file as input
    output = "C:\Work\Whitebox\output\s.shp" #output streams shapefile
)

print("****************************Creating subbasins*****************************************")
wbt.subbasins(
    d8_pntr = "C:\Work\Whitebox\output\FlowAccu_pntr.tif", #line 17 output flow pointer file as input
    streams = "C:\Work\Whitebox\output\output_streams.tif", #line 24 streams output raster as input
    output = "C:\Work\Whitebox\output\subbasins.tif"
)
