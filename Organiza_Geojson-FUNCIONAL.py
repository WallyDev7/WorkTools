import os
import json

def organize_geojson_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".geojson"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            organized_data = organize_geojson(data)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(organized_data, file, indent=2)

def organize_geojson(data):
    if data["type"] == "Feature":
        coordinates = data["geometry"]["coordinates"]
        if len(coordinates) == 1:
            # If there's only one set of coordinates, assume it's a Polygon
            data["geometry"]["coordinates"] = [coordinates[0]]
        elif len(coordinates) == 2:
            # If there are two sets of coordinates, assume it's a LineString
            data["geometry"]["coordinates"] = coordinates
    return data

# Example usage:
folder_path = "C:/Users/BSOC2/Desktop/Gabriel/Scripts/KML_SP/"
organize_geojson_files(folder_path)
