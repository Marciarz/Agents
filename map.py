red = (255, 87, 20)
black = (10, 10, 10)
blue = (70, 125, 227)
brown = (122, 105, 35)

def Generate_map(colors_list):
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
    return html_table
