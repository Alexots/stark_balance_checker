from openpyxl.worksheet.datavalidation import DataValidation
from core.const import alphabet

def write_lists(ws,data,row):
    for i in range(len(data)):
        if data[i] == None:
            continue
        dv = DataValidation(type="list", formula1=f'"{data[i]}"', allow_blank=False)
        ws.add_data_validation(dv)
        dv.add(f"{alphabet[i]}{row}")
    return True

def write_data(ws,data,row):
    for i in range(len(data)):
        if data[i] == None:
            continue
        ws[f"{alphabet[i]}{row}"] = data[i]
    return True