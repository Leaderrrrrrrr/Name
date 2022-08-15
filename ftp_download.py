import ftplib
import datetime


# function download files from specific date
def download_date(ftp, date_entered):
    for filename in ftp.nlst("MED_DATA_" + date_entered + "*.csv"):
        path = "/home/ftpclient/Documents/FTP/" + filename
        
        with open(path, "wb") as file:
            ftp.retrbinary(f"RETR {filename}", file.write)
            file.close()


# function to download all files not previously downloaded
def download_all(ftp, previously_downloaded, files_downloaded):
    file = open(previously_downloaded, "w")
    lines = file.readlines()

    print(lines)
    print(type(lines))


# Open ftp connection
print("Connecting to FTP")
ftp = ftplib.FTP('192.168.200.128', 'ftp_user', 'password')
print("Connected to FTP")

date_entered = input("Enter data, format YYYYMMDD (if blank, default is today). Enter \"All\" to download all files:\n")

files_downloaded = []

if date_entered == "":
    date_entered = datetime.date.today().strftime("%Y%m%d")

if date_entered.upper() == "ALL":
    print("Downloading all")
    download_all(ftp, r"C:\Users\Student\Documents\Temp\downloaded_files.txt")
else:
    print("Downloading for date {date_entered}")
    download_date(ftp, date_entered)

# print("Files downloaded are: " + files_downloaded)
