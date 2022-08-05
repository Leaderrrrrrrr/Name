import ftplib

# Open ftp connection
ftp = ftplib.FTP('192.168.0.132', 'student', 'password')


# List the files in the current directory

date = input("Enter data, format YYYYMMDD:\n")

for filename in ftp.nlst("MED_DATA_" + date + "*.csv"):
    path = r"C:\Users\Student\Documents\Temp\\" + filename

    with open(path, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)
        file.close()
