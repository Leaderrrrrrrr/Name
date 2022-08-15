import ftplib
from datetime import datetime


#function to download file to client machine from server
def download_file(ftp, filename, previously_downloaded):
    path = "/home/ftpclient/Documents/FTP/" + filename

    with open(previously_downloaded, "a") as downloaded:

        with open(path, "wb") as file:
            print('Downloading: ' + filename + "\n")

            #download file
            ftp.retrbinary(f"RETR {filename}", file.write)

            file.close()

        downloaded.write(filename + "\n")
        downloaded.close()

# function find files from specific date
def download_date(ftp, date_entered, previously_downloaded):

    #find files
    for filename in ftp.nlst("MED_DATA_" + date_entered + "*.csv"):

        #call download file
        download_file(ftp, filename, previously_downloaded)


# function to find all files not previously downloaded
def download_all(ftp, previously_downloaded):
    with open(previously_downloaded, "r+") as file:
        files_downloaded = file.readlines()

        #find files
        for filename in ftp.nlst("MED_DATA_*.csv"):
            if filename + "\n" not in files_downloaded:

                #call download file
                download_file(ftp, filename, previously_downloaded)
        file.close()


#%% Open ftp connection
print("Connecting to FTP")
ftp = ftplib.FTP('192.168.200.128', 'ftp_user', 'password')
print("Connected to FTP")

#%% get information from user


date_entered = input("""Enter data, format YYYYMMDD (if blank, default is today).
Enter \"All\" to download all files:\n""")
FILES_DOWNLOADED_LOCATION = "/home/ftpclient/Documents/FTP/files_downloaded.txt"


#%% run download

#get current date if required
if date_entered == "":
    print("Downloading files from today only.\n")
    date_entered = datetime.today().strftime("%Y%m%d")

if date_entered.upper() == "ALL":
    print("Downloading all\n")
    download_all(ftp, FILES_DOWNLOADED_LOCATION)
else:
    print("Downloading for date: " + datetime.strptime(date_entered, "%Y%m%d")
          .strftime("%d/%m/%Y") + "\n")
    download_date(ftp, date_entered, FILES_DOWNLOADED_LOCATION)

print('All files downloaded')
