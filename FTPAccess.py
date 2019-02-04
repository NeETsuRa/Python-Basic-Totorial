from ftplib import FTP

#domain name or server ip (connect):
ftp = FTP('123.server.ip')
ftp.login(user='username', passwd = 'password')
#navigate
ftp.cwd('/whyfix/')
# download a file
def grabFile():

    filename = 'example.txt'

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()
#upload a file
def placeFile():

    filename = 'exampleFile.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

placeFile()