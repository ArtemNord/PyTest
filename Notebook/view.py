from datetime import datetime

COMMANDS_LIST ={
    '1': 'Создать новую заметку',
    '2': 'Посмотреть все заметки',
    '3': 'Посмотреть все заметки за выбранную дату',
    '4': 'Найти конкретную заметку',
    '5': 'Редактировать заметку',
    '6': 'Удалить заметку',
    '0': 'Выход',
}

def greeting():
    print('Добро пожаловать!\n')

def goodbye():
    print('До встречи!')

def show_menu():
    print('Выберите цифру соответствующую необходимой команде:')
    for key, value in COMMANDS_LIST.items():
        print(f'{key} - {value}')
    print()
    while True:
        choice = input('Введите номер команды: ')
        if choice in COMMANDS_LIST:
            print(f'Вы выбрали команду "{COMMANDS_LIST[choice]}"')
            return choice
        else:
            print('Команда не распознана. Попробуйте еще раз')

def get_note_id():
    while True:
        id = input('Введите id-номер заметки: ')
        try:
            return int(id)
        except:
            print(f'Введенное значение {id} не является числом. Попробуйте еще раз')

def get_note_text():
    title_required, text_required = True, True
    while title_required:
        title = input('Введите заголовок заметки: ')
        if title:
            title_required = False
        while text_required:
            text = input('Введите текст заметки: ')
            if text:
                text_required = False
        return title, text

def get_date():
    while True:
        date = input('Введите интересующую вас дату в формате ДД.ММ.ГГГГ : ')
        try:
            datetime.strftime(date, '%d.%m.%Y')
            return date
        except:
            print(f'Указанная дата {date} некорректна. Попробуйте еще раз')

def print_note(note):
    print(f'ID: {note["id"]}\n{note["title"].upper()}\n{note["text"]}\nДата последнего изменения:{note["date"]}')

def show_in_console(data):
    if isinstance(data,list):
        for note in data:
            print_note(note)
            print()
    if isinstance(data, dict):
        print_note(data)
    print()
