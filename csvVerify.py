import sys
import os
import logging
import pandas as pd

CHECKED_PATH = "./checked/"

if len(sys.argv) < 2: # The file takes at least one file as an argument
    logging.error(" Must have at least one argument")
    logging.log(0, "Exiting...")
    exit()

#for file in sys.argv[1:]: # For each file given as an argument
for file in os.scandir(CHECKED_PATH):
    if not filename.is_file():
        continue

    logging.log(0, f"Validating file %s" % file)

    filename = file.split('/')[-1]   # separate between brackets

    # If file cannot get read, delete
    try:
        print(file)
        data = pd.read_csv(file)
        logging.log(0, "file read")
        logging.log(0, "removing temp file")   # !WITH THE TEMP FILE REMOVED, CONTINUE WILL DELETE THE FILE

        os.remove(file)
    except:
        logging.error("File not readable")
        logging.log(0, "Deleting file...")
        os.remove(file)
        continue

    # Check file name
    if filename[:9] != "MED_DATA_" or filename[23:] != ".csv":
        logging.error("Invalid file name")
        continue
    if int(filename[9:13]) > 3000 or int(filename[9:13]) < 1970 or int(filename[13:15]) > 12 or int(filename[13:15]) < 1 or int(filename[15:17]) > 31 or int(filename[15:17]) < 1:
        logging.error("Invalid date in file name")
        continue

    if int(filename[17:19]) > 24 or int(filename[17:19]) < 0 or int(filename[19:21]) > 59 or int(filename[19:21]) < 0 or int(filename[21:23]) > 59 or int(filename[21:23]) < 0:
        logging.error("Invalid time in file name")
        continue

    # Check number of columns
    if len(data.columns) == 12:
        logging.log(0, "correct number of columns")
    else:
        logging.error("Incorrect number of columns!")
        continue

    # Check for unique batch IDs
    ids = []
    for i in range(len(data["batch_id"])):
        if data["batch_id"][i] not in ids: # If new ID
            ids.append(data["batch_id"][i])
        else: # If timestamp is not same as old ID
            logging.error("IDs not unique")
            continue

    # timestamp checking
    for timestamp in data["timestamp"]:
        parts = timestamp.split(":")
        if int(parts[0]) > 24 or int(parts[0]) < 0 or len(parts[0]) != 2:
            logging.error("Invalid hour")
            continue
        if int(parts[1]) > 59 or int(parts[1]) < 0 or len(parts[1]) != 2:
            logging.error("Invalid minutes ")
            continue
        if int(parts[2]) > 59 or int(parts[2]) < 0 or len(parts[2]) != 2:
            logging.error("Invalid seconds ")
            continue

    # Reading checking
    for cols in data.columns[2:]:
        for i in range(len(data[cols])):
            if data[cols][i] < 0 or data[cols][i] > 9.9:
                logging.error("value out of bounds")
                continue

            # Format
            data[cols][i] = float("{0:.3f}".format(data.loc[i].at[cols]))


    # Save file to checked folder
    logging.log(0, "File Approved: sending to checked folder")
    data.to_csv(CHECKED_PATH + filename)      # If the file already exists, it will be overwritten
