import json
from datetime import datetime
from model import Note

DATABASE_NAME = 'my_notes.json'

def write_to_database(data):
    with open(DATABASE_NAME, 'w', encoding='UTF-8') as base:
        json.dump(data, base, indent=2)

def get_notes_list():
    with open(DATABASE_NAME, 'r', encoding='UTF-8') as base:
        data = []
        try:
            data = json.load(base)
        except:
            print('Вы создали первую заметку!')
        return data

def get_note(id):
    data = get_notes_list()
    for i in range(len(data)):
        if data[i]['id'] == id:
            return data[i]
    print(f'Запись с id = {id} не найдена')

def create_id_number(all_notes):
    id = 0
    for note in all_notes:
        if note['id'] >= id:
            id = note['id'] + 1
    return id

def create(title, text):
    all_notes = get_notes_list()
    id = create_id_number(all_notes)
    new_note = Note(id, title, text)
    all_notes.append(new_note.__dict__)
    write_to_database(all_notes)

def update_note(id, title, text):
    data = get_notes_list()
    is_updated, i = False, 0
    while not is_updated and i < len(data):
        if data[i]['id'] == id:
            data[i]['title'] == title
            data[i]['text'] == text
            data[i]['date'] == datetime.now().strftime("%d.%m.%Y %H:%M")
            is_updated = True
        i += 1
    if is_updated:
        write_to_database(data)
    else:
        print(f'Запись с id = {id} не найдена')

def delete_note(id):
    data = get_notes_list()
    is_delete, i = False, 0
    while not is_delete and i < len(data):
        if data[i]['id'] == id:
            data.pop(i)
            is_delete = True
        i += 1
    if is_delete:
        print(f'Заметка с id = {id} успешно удалена')
        write_to_database(data)
    else:
        print(f'Запись с id = {id} не найдена')
