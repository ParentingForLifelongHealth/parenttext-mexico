import os
from rpft.converters import create_flows
from config import *

for source in sources:

        # Load core file information

        source_file_name = source["filename"]
        spreadsheet_ids = source["spreadsheet_ids"]
        tags = source["tags"]

        #####################################################################
        # Step 1: Load google sheets and convert to RapidPro JSON
        #####################################################################

        output_file_name = "gsheet_output"
        output_path = os.path.join("./testing_csv_loading/result", output_file_name + ".json")

        create_flows(spreadsheet_ids, output_path, "google_sheets", model, tags)