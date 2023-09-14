import os
from rpft.converters import create_flows
from config import *

csv_inputs_dir = "./testing_csv_loading/csv_inputs"
main_files = []

# Walk through the directory and list all folders
for root, dirs, files in os.walk(csv_inputs_dir):
    for folder in dirs:
        # Get the relative path of the main file
        relative_path = os.path.join(csv_inputs_dir, folder, "content_index.csv")
        main_files.append(relative_path)

tags = [1, "delivery",1, "menu", 2,"south_africa"]

#####################################################################
# Step 1: Load google sheets and convert to RapidPro JSON
#####################################################################

output_file_name = "csv_output"
output_path = os.path.join("./testing_csv_loading/result", output_file_name + ".json")

create_flows(main_files, output_path, "csv", model, tags)