# Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику: просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.


def total(argv):
    program, *arg = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if (len(sys.argv)-1) == 0:
            lines = f.readlines()
            for i in range(len(lines)):
                print(f'{str(i + 1)} : {lines[1].strip()}')
        elif (len(sys.argv)-1) == 1:
            start = int(''.join(arg[0]))
            for i in range(start - 1, len(lines)):
                print(f'{str(i + 1)} : {lines[i].strip()}')
        elif (len(sys.argv)-1) == 2:
            start = int(''.join(arg[0]))
            end = int(''.join(arg[1]))
            if end <= len(lines):
                for i in range(start - 1, end):
                    print(f'{str(i + 1)} : {lines[i].strip()}')
            else:
                for i in range(start - 1, len(lines)):
                    print(f'{str(i + 1)} : {lines[i].strip()}')



if __name__ == '__main__':
    import sys
    exit(total(sys.argv))
