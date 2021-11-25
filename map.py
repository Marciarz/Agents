import remote_file_helper
import passwords

red = (255, 87, 20)
black = (10, 10, 10)
blue = (70, 125, 227)
brown = (122, 105, 35)

def Generate_map(colors_list, game_number):
    html_table = f'<table style="width:100%">'
    for row in colors_list:
        html_table += f'<tr style="height:150px">'
        for cell in row:
            rgb_color = ""
            if cell == "red":
                rgb_color = red
            elif cell == "blue":
                rgb_color = blue
            elif cell == "black":
                rgb_color = black
            else:
                rgb_color = brown
            html_table += f'<td style="background-color:rgb{rgb_color};"></td>'
        html_table += f'</tr>'
    html_table += f'</table>'

    pass_codes = passwords.Passwords()
    remote_helper = remote_file_helper.FtpHelper(pass_codes.ftp_ip, pass_codes.ftp_login,
                                                 pass_codes.ftp_pass, pass_codes.ftp_shared_folder_path,
                                                 pass_codes.file_name, game_number)
    remote_helper.delete_previous_html_local_file()
    remote_helper.save_html_file_from_string(html_table)
    remote_helper.upload_file()
