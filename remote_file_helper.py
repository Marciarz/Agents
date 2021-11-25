from ftplib import FTP
import os
import fileinput
import json
import logging

class FtpHelper:

    def __init__(self, ip_address, login, password, shared_folder_path, file_name, game_number):
        self.ip_address = ip_address
        self.login = login
        self.password = password
        self.shared_folder_path = shared_folder_path
        self.file_name = file_name
        self.remote_file_name = '{0}_{1}.{2}'.format(file_name.split('.')[0], game_number, file_name.split('.')[1])

    def upload_file(self):
        ftp = FTP()
        ftp.set_debuglevel(0)
        ftp.connect(self.ip_address, 21)
        ftp.login(self.login,self.password)
        ftp.cwd(self.shared_folder_path)

        fp = open(self.file_name, 'rb')
        ftp.storbinary('STOR %s' % os.path.basename(self.remote_file_name), fp, 1024)
        fp.close()
        ftp.quit()

    def get_file_from_ftp(self):
        ftp = FTP()
        ftp.set_debuglevel(0)
        ftp.connect(self.ip_address, 21)
        ftp.login(self.login,self.password)
        ftp.cwd(self.shared_folder_path)
        localfile = open(self.file_name, 'wb')
        ftp.retrbinary('RETR {}'.format(self.file_name), localfile.write, 1024)
        localfile.close()
        ftp.close()

    def get_data_from_file(self):
        json_file = open(self.file_name)
        product_list = json.load(json_file)
        return product_list

    def save_html_file_from_string(self, html_string):
        with open(self.file_name, 'w') as outfile:
            outfile.write(html_string)

    def delete_previous_html_local_file(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)