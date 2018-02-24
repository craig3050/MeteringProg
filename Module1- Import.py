from openpyxl import Workbook
from openpyxl import load_workbook
# import sqlite3
# conn = sqlite3.connect('import_data.db')

#Copy from previous working programme
# def excel_list(file_path):
#     drawing_list = Workbook()
#     worksheet_1 = drawing_list.active
#     drawing_list.save("Drawing_list.xlsx")
#     row_number = 1
#     for file_name in os.listdir(file_path):
#         file_name_no_extension = ""
#         for char in file_name:
#             if char != ".":
#                 file_name_no_extension += char
#             else:
#                 break
#         file_extension = file_name.split(".")[-1]
#         worksheet_1.cell(row = row_number, column = 1).value = file_name_no_extension
#         worksheet_1.cell(row = row_number, column = 2).value = file_extension
#         row_number += 1
#     drawing_list.save("Drawing_list.xlsx")
#     print("The drawing list has been written to the same directory as the script")
#     print("Add your drawings into column C")
#     #break before writing the new numbers
#     continue_on()
# drawing_list = load_workbook("Drawing_list.xlsx")
# worksheet_1 = drawing_list.active
# # rename the files
# for i in range(1, row_number):
#     old_file_name = worksheet_1.cell(row=i, column=1).value
#     print(old_file_name)
#     file_extension = worksheet_1.cell(row=i, column=2).value
#     print(file_extension)
#     new_file_name = worksheet_1.cell(row=i, column=3).value
#     print(new_file_name)
#     print("Old = " + old_file_name + ",  New = " + new_file_name)
#     old_file_name = file_path + "/" + old_file_name + "." + file_extension
#     RenameFile(old_file_name, new_file_name)

#Part 1 - open the excel file
def load_excel_file(file_path):
    workbook = load_workbook(file_path)
    print (workbook.get_sheet_names())
    sheet_names = []
    for i in workbook.get_sheet_names():
        sheet_names.append(i)
    print (sheet_names)
    number = 1
    for item in sheet_names:
        print (number + " - " + item)
    sheet_select = input("Enter the number of the sheet to be imported: ")
    sheet_select -=1
    worksheet = sheet_names[sheet_select].active



if __name__ == '__main__':
    print("Welcome to Craig's simple file renaming tool!\n\n")
    file_path = input("Enter the Path of the document to be processed: ")
    print("Printing directory contents: \n")
    load_excel_file(file_path)
