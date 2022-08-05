import sys
import logging
import pandas as pd

if len(sys.argv) < 2:
    logging.error(" Must have at least one argument")
    logging.log("Exiting...")
    exit()

for file in sys.argv[1:]:
    data = pd.read_csv(file)
    logging.log(0, "file read")
    if len(data.columns) == 12:
        logging.log(0, "correct number of columns")
    else:
        logging.error("Incorrect number of columns!")
