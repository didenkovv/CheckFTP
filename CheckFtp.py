import smtplib
import os
from ftplib import FTP
import time

### credentional for ftp ####
usernameFtp = "ftp_user"
passwordFtp = "FTP_password"
serverFtp = "IP_ADDRESS_FTP_SERVER"
#port ftp
portFtp = 8120
#file in the FTP server. This file will to copy
filename ="test.zip"

### credentional for mail ###
mailAddressFrom = "test@test.com"
mailAddressFromPassword = "******"

mailAddressTo = {"test@test.com"}
try:
    smtpServer = smtplib.SMTP('outlook.office365.com', 587)
    smtpServer.starttls()
    smtpServer.login(mailAddressFrom, "Qoha43041")
except Exception  as e:
    print("SMTP is brocken")

def sendMailbrocken():
    mailBodyMassage = "\r\n".join((
        "From: %s" % mailAddressFrom,
        "To: %s" % mailAddressTo,
        "Subject: %s" % "WARNING FTP server!",
        "",
        "FTP service is not work"
    ))
    smtpServer.sendmail(mailAddressFrom, mailAddressTo, mailBodyMassage)
    smtpServer.quit()
#remove priviuse file
try:
    os.remove(r"c:\Temp\test.zip")
except Exception as e:
    print("this is file not existes")
time.sleep(3)

# download the file
ftp = FTP()
try:
    ftp.connect(serverFtp, portFtp)
    ftp.login(usernameFtp, passwordFtp)
    ftp.cwd("TEST")
    local_filename = os.path.join(r"c:\Temp", filename)
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR " + filename, lf.write, 8 * 1024)
except Exception  as e:
    sendMailbrocken()
ftp.close()

##check ftp server##
#sendMailbrocken()