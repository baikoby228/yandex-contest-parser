import openpyxl
import sys
import os

def write_to_excel(persons: list, id: int) -> None:
    wb = openpyxl.Workbook()
    sheet = wb.active

    for person in persons:
        sheet.append([person.name] + person.points + [person.total_points])

    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, f'results_{id}.xlsx')
    wb.save(save_path)
