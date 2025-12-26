from parser import parse
from excel_writer import write_to_excel

if __name__ == '__main__':
    id = int(input())
    persons = parse(id)
    write_to_excel(persons, id, True)
