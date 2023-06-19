from os import path
import os
os.system('clear')

file_base = "base.txt"
last_id = 0
all_data = []


if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as f:
        pass

def read_rec():
    global last_id, all_data
    
    with open(file_base,"r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []

def show_all_rec():
    if all_data:
        print(*all_data, sep="\n")
    else:
         print("Телефонный справочник пуст\n")
    print("\n")

def add_new_record():
    global last_id
    
    arr = ['фамилия', 'имя', 'отчество', 'телефонный номер']
    answer = []
    
    for i in arr:
        answer.append(data_collection(i))
    
    if not exist_contact(0, " ".join(answer)):
        last_id += 1
        answer.insert(0, str(last_id))

        with open(file_base, "a", encoding="utf-8") as f:
            f.write(f'{" ".join(answer)}\n')
        print("Данные введены в телефонный справочник успешно\n")
    else:
        print("Данные были занесены ранее")

def exist_contact(rec_id, data):
    
    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def data_collection(num):
    answer = input(f"Введите {num}: ")
    while True:
        if num in "фамилия имя отчество":
            if answer.isalpha():
                break
        if num == "телефонный номер":
            if answer.isdigit() and len(answer) == 6:
                break
        answer = input(f"Ввод не верен!\n"
                       f"При вводе ФИО используйте только буквы\n"
                       f"В нашем городе телефонный номер состоит из 6 цифр\n"
                       f"Введите {num}: ")
    return answer  

def search_contact():
    search_data = exist_contact(0, input("Введите данные для поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Нечего нет")

def del_contact():
 
    global all_data

    symbol = "\n"
    show_all_rec()
    del_record = input("Введите id абонента: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена\n")
    else:
        print("Данные не верны!")

def edit_menu():
    
    add_dict = {"1": "фамилия", "2": "имя", "3": "отчество", "4": "телефонный номер"}

    show_all_rec()
    record_id = input("Введите id абонента: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. Фамилия\n"
                           "2. Имя\n"
                           "3. Отчество\n"
                           "4. Телефонный номер\n"
                           "5. Выход\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Данные не распознаны, введите заново")
    else:
        print("id неверен!")

def change_contact(data_tuple):

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Данные уже существуют!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Изменен успешно!\n")

def main_menu():
    
    play = True
    while play:
        
        read_rec()
        answer = input("ТЕЛЕФОННЫЙ СПРАВОЧНИК:\n"
                       "1. Показать все записи\n"
                       "2. Добавить записи\n"
                       "3. Изменить запись\n"
                       "4. Удалить запись\n"
                       "5. Найти запись\n"
                       "6. ВЫХОД\n")
        match answer:
            case "1":
                show_all_rec()
            case "2":
                add_new_record()
            case "3":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "4":
                del_contact()
            case "5":
                search_contact()
            case "6":
                play = False
                print("Досвидания!")
            case _:
                print("НЕВЕРНЫЙ ВЫБОР!")
    

main_menu()