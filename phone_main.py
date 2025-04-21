# Подключение собственных модулей по проверке номеров
import phone_files
import phone_proof

# Главная функция реализует интерфейс с пользователем
def main():
    print("Программа проверки «красивых» телефонных номеров")
    punkt = '?'
    while(punkt != 'Q'):
        if punkt == '?':
           # Вывод меню
           print("\nГлавное меню:",
                 "\nS. Поиск номеров от заданного",
                 "\nC. Выполнить командную строку",
                 "\nN. Проверка введенного номера",
                 "\nD. Проверка диапазона номеров",
                 "\nL. Вывести содержание директории",
                 "\nG. Пакетная файловая обработка номеров",
                 "\nF. Пакетная файловая обработка диапазонов",
                 "\nQ. Завершить и выйти из программы")
        # Выбор действия
        elif punkt == 'S':  phone_proof.scanNumbers()
        elif punkt == 'N':  phone_proof.checkNumber()
        elif punkt == 'D':  phone_proof.checkRanges()
        elif punkt == 'G':  phone_files.checkNumber()
        elif punkt == 'F':  phone_files.checkRanges()
        elif punkt == 'L':  phone_files.Directories()
        elif punkt == 'C':  phone_files.callCommand()
        else:
           print("Такой команды нет")

        # Выбор пункта
        punkt = (input("Введите команду [?-меню]:>")).upper()

    print('Программа завершена')

# Запуск главной функции
if __name__ == '__main__':
    main()
