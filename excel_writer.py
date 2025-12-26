import openpyxl
from openpyxl.styles import Alignment

import sys
import os

def write_to_excel(persons: list, id: int) -> None:
    wb = openpyxl.Workbook()
    sheet = wb.active

    tasks_count = 0
    for person in persons:
        tasks_count = max(tasks_count, person.tasks_count)

    sheet.append(['Место', 'Фамилия, имя, область участника'] + [chr(ord('A') + i) for i in range(tasks_count)] + ['Итог'])

    for person in persons:
        sheet.append([person.place] + [person.name] + person.points + [person.total_points])

    for i in range(tasks_count + 3):
        mx = 0
        C = chr(ord('A') + i)
        for cell in sheet[C]:
            if cell.value:
                mx = max(mx, len(str(cell.value)))
        sheet.column_dimensions[C].width = mx + 2

        if i == 1:
            continue
        for cell in sheet[C]:
            cell.alignment = Alignment(horizontal='center')

    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, f'results_{id}.xlsx')
    wb.save(save_path)
