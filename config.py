# Data sources, ids of google sheets where the core date is stored, "filename" is how it will be generally named in the pipeline. 
#  "crowdin_name" will be the name of the file that is produced to send to the translators
sources = [
    {"filename": "parenttext_onboarding", "spreadsheet_id": "12ddvTz_ZfC-9-b0yxjVrSzczciUUE3GosLUFeOLIv9I", "crowdin_name": "onboarding", "split_no": 2},
]

#Data copied from Chiara's pipeline for testing on multiple files, leave here for now

# sources = [
#     {"filename": "parenttext_onboarding", "spreadsheet_id": "12ddvTz_ZfC-9-b0yxjVrSzczciUUE3GosLUFeOLIv9I", "crowdin_name": "onboarding"},
#     {"filename": "parenttext_modules", "spreadsheet_id": "1ONmD9PF9rcno3ha3QpfrIR5EIvHuuEqJXF3T90rlZ78", "crowdin_name": "modules_teen"},
#     {"filename": "parenttext_goalcheckin", "spreadsheet_id": "1gympuD5KdlAdDJSuaVQiXjWSwJxoDcA9K-oBRyKmS7o", "crowdin_name": "goal_checkins"},
#     {"filename": "parenttext_dev_assess_tools", "spreadsheet_id": "1OhhQF5yarUDmaSl2tlt7eIT7wJ8bGwNFzI3BOplJYsc", "crowdin_name": "dev_assess_tools"},
#     {"filename": "parenttext_ltp_act_teen", "spreadsheet_id": "1Jx7vOmdefzK62ao2nlJJVLMAIS8d-6r1G8qn0jG8gww", "crowdin_name": "ltp_activities_teen"}
# ]


# Model that is used as part of the process when the data is extracted from excel
model = "models.parenttext_models"

# Languages that will be looked for to localize back into the flows, "language" is the 3 letter code used in RapidPro, "code" is the 2 letter code used in crowdin
languages = [
    {"language": "swa", "code": "ss"}
]

# Location where translations are stored, at the moment pointing to a locally cloned repo, should maybe be adapted so we can provide a link to an online repo
translation_repo = "../PLH-Digital-Content/translations/parent_text_v2"

# Desination file for all files (including intermediary files and log files)
outputpath = "./output"

# In one of the latter stages we have the option to modify the quick replies,
# 1 - We may want to remove the quick replies and add them to message text and give numerical prompts to allow basic phone users to use the app - for this use reference code "move"
# 2 - We may want to reformat the quick replies so that long ones are added to the message text as above - for this use reference code "reformat"
# 3 - We may not want to do anything, for this use reference code "none"
qr_treatment = "reformat"

# This is the default phrase we want to add in if the quick replies are being moved to message text
select_phrases = "./edits/select_phrases.json"

# If we are in scenario 1 above, we may wish to add some basic numerical quick replies back in, if so we need to specify add_selectors as "yes"
add_selectors = "yes"

# Some words we always want to keep as full quick replies, they are specified in this file
special_words = "./edits/special_words.json"

# In scenario 2 we set limits on the number of quick replies and the length of the quick replies. 
#   count_threshold (relates to number of quick replies)
#   length_threshold (relates to length of the longest quick reply)
# If the number of QRs is below or equal the count_threshold and the longest QR is shorter than or equal to the length_threshold then the QR are to be left in place the node will not be changed. 
# In places where the QR are too long. We will make the changes to make the QRs numbers and add the number references to the message text as example 1.
# Thresholds should be entered as strings
count_threshold = "10"
length_threshold = "100"

#Google sheet ID containing ab testing data
ab_testing_sheet_ID = "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s"

#Google sheet ID containing dict edits data
dict_edits_sheet_ID = None

#Google sheet ID containing safeguarding data
SG_sheet_ID = None
SG_flow_name = None

#PAth to file containing translated safeguarding words
SG_path = None