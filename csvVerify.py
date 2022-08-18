import sys
import os
import logging
import pandas as pd

if len(sys.argv) < 2: # The file takes at least one file as an argument
    logging.error(" Must have at least one argument")
    logging.log("Exiting...")
    exit()

for file in sys.argv[1:]: # For each file given as an argument
    logging.log(f"Validating file %s" % file)

    filename = file.split("/")[-1]

    # If file cannot get read, delete
    try:
        data = pd.read_csv(file)
        logging.log(0, "file read")
        logging.log("removing temp file")   # !WITH THE TEMP FILE REMOVED, CONTINUE WILL DELETE THE FILE
        os.remove(file)
    except:
        logging.error("File not readable")
        logging.log("Deleting file...")
        os.remove(file)
        continue

    # Check file name
    if filename[:9] != "MED_DATA_" or filename[23:] != ".csv":
        logging.error("Invalid file name")
        continue
    #if filename[:9] !=                 TODO: check date of file

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
    for timestamp in range(1, len(data["timestamp"])):
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
    #for cols in data.columns[2:]:
    #    for i in data[cols]:

    # n = float("{0:.3f}".format(n))


    # Save file to checked folder
    logging.log("File Approved: sending to checked folder")
    pd.to_csv("./checked/" + filename)      # If the file already exists, it will be overwritten

    logging.log("removing temp file")