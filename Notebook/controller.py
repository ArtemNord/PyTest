from view import greeting, goodbye, show_menu, get_note_id, get_note_text, get_date, show_in_console
from database import create, get_notes_list, get_note, update_note, delete_note


def create_new_note():
    try:
        title, text = get_note_text()
        create(title, text)
        print('Заметка успешно сохранена')
    except:
        print('При создании заметки произошла ошибка')


def read_all_notes():
    try:
        all_notes = get_notes_list()
        show_in_console(all_notes)
    except:
        print('При выгрузке данных произошла ошибка')


def read_all_notes_by_date():
    try:
        date = get_date()
        filtered_notes = [note for note in get_notes_list() if note['date'].startswith(date)]
        if filtered_notes:
            show_in_console(filtered_notes)
        else:
            print(f'Заметок на дату {date} не найдено')
    except:
        print('При выгрузке данных произошла ошибка')


def find_note_by_id():
    try:
        id = get_note_id()
        note = get_note(id)
        if note:
            show_in_console(note)
    except:
        print('При поиске заметки произошла ошибка')


def edit_note():
    try:
        id = get_note_id()
        title, text = get_note_text()
        update_note(id, title, text)
        print('Заметка успешно обновлена')
    except:
        print('При редактировании заметки произошла ошибка')


def delete_note_by_id():
    try:
        id = get_note_id()
        delete_note(id)
    except:
        print('При удалении заметки произошла ошибка')



COMMANDS_LIST = {
    '1': create_new_note,
    '2': read_all_notes,
    '3': read_all_notes_by_date,
    '4': find_note_by_id,
    '5': edit_note,
    '6': delete_note_by_id,
}


def start():
    greeting()
    is_running = True
    while is_running:
        command = show_menu()
        if command == '0':
            is_running = False
            goodbye()
        else:
            try:
                COMMANDS_LIST[command]()
            except:
                print("Ошибка работы программы")
