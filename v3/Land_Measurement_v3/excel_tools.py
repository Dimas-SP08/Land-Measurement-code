from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def to_excel(table):
    '''Save survey data into an Excel file'''
    table.to_excel('Elevation Data.xlsx',float_format='%.3f',index=False)

def graphic_to_excel():
    '''Insert plot images into the Excel file'''
    wb = load_workbook('Elevation Data.xlsx')
    ws = wb.active
    def add_image_to_excel(no_image,image_path, cell):
        no_image = Image(image_path)
        ws.add_image(no_image,cell)
    add_image_to_excel('elevation_scatter_plot.png', 'elevation_scatter_plot.png', 'I2')
    add_image_to_excel('elevation_profile_plot.png', 'elevation_profile_plot.png', 'I30')
    add_image_to_excel('height_difference_bar_plot.png', 'height_difference_bar_plot.png', 'I58')
    wb.save('Elevation Data with graphic.xlsx')
                