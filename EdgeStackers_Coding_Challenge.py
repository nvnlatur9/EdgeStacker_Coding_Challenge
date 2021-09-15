# importing required libraries
# json to work load json file and os to check if the file path is valid
import json
import os
import datetime

# reading filepath from command prompt
filePath = input("Enter complete json file path")

# checking if file path exists
if os.path.exists(filePath):
    open_file = open(filePath)
    data = json.load(open_file)
    # loop to run through dictionary to extract only required fields
    dict1= list()
    for i in data["dates"]:
        for j in i["sections"]:
            for k in j["meetings"]:
                output_dict = dict()
                output_dict["meeting_id"] = k["id"]
                output_dict["meeting_name"] = k["name"]
                output_dict["race"] = []
                for l in k["events"]:
                    output_dict1 = dict()
                    output_dict1["race_number"] = l["raceNumber"]
                    output_dict1["race_link"] = l["httpLink"]
                    output_dict1["event_id"] = l["id"]
                    if "distance" in l.keys():
                        output_dict1["distance"] = l["distance"]
                    else:
                        output_dict1["distance"] = ""
                    time = datetime.datetime.isoformat(datetime.datetime.fromtimestamp(l["startTime"]))
                    output_dict1["start_time"] = time
                    output_dict["race"].append(output_dict1)
            dict1.append(output_dict)
    print(dict1)

else:
    print("Enter valid file path")

