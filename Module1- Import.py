from openpyxl import Workbook
from openpyxl import load_workbook
# import sqlite3
# conn = sqlite3.connect('import_data.db')


#Part 1 - open the excel file
def load_excel_file(file_path):
    workbook = load_workbook(file_path)
    print (workbook.get_sheet_names())
    sheet_names = []
    for i in workbook.get_sheet_names():
        sheet_names.append(i)
    print (sheet_names)
    number = 1 #Starting the list from one as it's easier for people to relate
    for item in sheet_names:
        print (str(number) + " - " + item)
        number +=1
    sheet_select = int(input("Enter the number of the sheet to be imported: "))
    sheet_select -=1 #take 1 from the value as list addresses start from zero
    worksheet = workbook[sheet_names[sheet_select]] # open the selected sheet
    row_number = 1
    while row_number <20:
        print (worksheet.cell(row=row_number, column=1).value)
        row_number +=1
    input("Press Enter to exit")





if __name__ == '__main__':
    print("Welcome to Craig's simple file renaming tool!\n\n")
    file_path = input("Enter the Path of the document to be processed: ")
    print("Printing directory contents: \n")
    load_excel_file(file_path)
