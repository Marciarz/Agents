from ftplib import FTP
import os
import fileinput
import json
import logging

class FtpHelper:

    def __init__(self, ip_address, login, password, shared_folder_path, file_path):
        self.ip_address = ip_address
        self.login = login
        self.password = password
        self.shared_folder_path = shared_folder_path
        self.file_path = file_path

    def upload_file(self):
        ftp = FTP()
        ftp.set_debuglevel(0)
        ftp.connect(self.ip_address, 21)
        ftp.login(self.login,self.password)
        ftp.cwd(self.shared_folder_path)

        fp = open(self.file_path, 'rb')
        ftp.storbinary('STOR %s' % os.path.basename(self.file_path), fp, 1024)
        fp.close()
        ftp.quit()

    def get_file_from_ftp(self):
        ftp = FTP()
        ftp.set_debuglevel(0)
        ftp.connect(self.ip_address, 21)
        ftp.login(self.login,self.password)
        ftp.cwd(self.shared_folder_path)
        localfile = open(self.file_path, 'wb')
        ftp.retrbinary('RETR {}'.format(self.file_path), localfile.write, 1024)
        localfile.close()
        ftp.close()

    def get_data_from_file(self):
        json_file = open(self.file_path)
        product_list = json.load(json_file)
        return product_list

    def save_list_to_file(self, product_list):
        with open(self.file_path, 'w') as outfile:
            json.dump(product_list, outfile, sort_keys=True, indent=4)