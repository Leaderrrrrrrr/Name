import ftplib
from datetime import datetime


def download_file(ftp, filename):
    path = "/home/ftpclient/Documents/FTP/" + filename
    
    with open(path, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)
        file.close()
    

# function download files from specific date
def download_date(ftp, date_entered):
    for filename in ftp.nlst("MED_DATA_" + date_entered + "*.csv"):
        download_file(ftp, filename)


# function to download all files not previously downloaded
def download_all(ftp, previously_downloaded):
    file = open(previously_downloaded, "r+")
    files_downloaded = file.readlines()
    
    for filename in ftp.nlst("MED_DATA_*.csv"):
        if filename + "\n" not in files_downloaded:
            print('Downloading: ' + filename + "\n")
            download_file(ftp, filename)
            file.write(filename)
    file.close()


# Open ftp connection
print("Connecting to FTP")
ftp = ftplib.FTP('192.168.200.128', 'ftp_user', 'password')
print("Connected to FTP")

date_entered = input("Enter data, format YYYYMMDD (if blank, default is today). Enter \"All\" to download all files:\n")

if date_entered == "":
    print("Downloading files from today only.")
    date_entered = datetime.today().strftime("%Y%m%d")

if date_entered.upper() == "ALL":
    print("Downloading all")
    download_all(ftp, "/home/ftpclient/Documents/FTP/files_downloaded.txt")
else:
    print("Downloading for date: " + datetime.strptime(date_entered, "%Y%m%d").strftime("%d/%m/%Y"))
    download_date(ftp, date_entered)

print('All files downloaded')
