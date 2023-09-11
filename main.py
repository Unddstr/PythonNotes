from datetime import datetime

file_path = "notes.txt"


def show_all_notes():
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            notes = line.split(";")[0]
            print(notes, end="\n")
    print("\n")


def search_note():
    name_note = input("Введите заголовок заметки: ")
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            if name_note.lower() in line.split(";")[0].lower():
                notes = line.replace(";", " - ")
                print(notes, end="")
    print("\n")


def search_date():
    date_note = input("Введите дату заметки (dd-MM-yyyy): ")
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            if date_note.lower() in line.split(";")[1].lower():
                notes = line.replace(";", " - ")
                print(notes, end="")
    print("\n")


def add_note():
    print("Введите данные заметки: ")
    name_note = input("Заголовок: ")
    date_note = datetime.now().strftime("%d-%m-%Y;%H:%M:%S")
    note = input("Содержимое заметки: ")
    with open(file_path, 'a', encoding="utf-8") as f:
        f.writelines(name_note + ";" + date_note + ";" + note + "\n")
    print("Заметка добавлена\n")


def delete_note():
    print("Введите заголовок заметки которую нужно удалить: ")
    name_note = input("Заголовок: ")
    temp = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            if not (name_note.lower() in line.split(";")[0].lower()):
                temp.append(line.strip())
    with open(file_path, 'w', encoding="utf-8") as f:
        for i in temp:
            f.writelines(i + "\n")
    print("Заметка удалена\n")


def edit_note():
    print("Введите заголовок заметки которую нужно редактировать: ")
    name_note = input("Заголовок: ")
    temp = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for line in f:
            if not (name_note.lower() in line.split(";")[0].lower()):
                temp.append(line.strip())
            else:
                print("Введите новые данные редактируемого контакта: ")
                name_note_edit = input("Заголовок: ")
                date_edit = datetime.now().strftime("%d-%m-%Y;%H:%M:%S")
                note_edit = input("Содержимое заметки: ")
                temp.append(name_note_edit + ";" + date_edit + ";" + note_edit)
    with open(file_path, 'w', encoding="utf-8") as f:
        for i in temp:
            f.writelines(i + "\n")
    print("Заметка отредактирована\n")


def main():
    while True:
        print("Выберите действие:\n"
              "1 - показать заметки;\n"
              "2 - найти заметку по заголовку;\n"
              "3 - найти заметку по дате;\n"
              "4 - добавить заметку;\n"
              "5 - удилить заметку;\n"
              "6 - редактировать заметку\n"
              "7 - выйти из приложения\n")
        select = input()
        if select == '1':
            show_all_notes()
        elif select == '2':
            search_note()
        elif select == '3':
            search_date()
        elif select == '4':
            add_note()
        elif select == '5':
            delete_note()
        elif select == '6':
            edit_note()
        elif select == '7':
            break


main()
