"""
Проверить, установлен ли пакет pillow в глобальном окружении.
Если да — зафиксировать версию. Установить самую свежую версию pillow, если ранее она не была установлена.
Сделать подтверждающий скриншот. Создать и активировать виртуальное окружение.
Убедиться, что в нем нет пакета pillow. Сделать подтверждающий скриншот.
Установить в виртуальное окружение pillow версии 7.1.1 (или другой, отличной от самой свежей).
Сделать подтверждающий скриншот. Деактивировать виртуальное окружение. Сделать подтверждающий скриншот.
Скрины нумеровать двухразрядными числами, например: «01.jpg», «02.jpg».
Если будут проблемы с pillow - можно поработать с другим пакетом: например, requests.

"""

# установка и проверка pillow

mac@MacBook-Air-mac 1824_GB_Python_1 % pip3 freeze
certifi==2021.5.30
Pillow==8.3.2

# создание и активация вируального окружения

mac@MacBook-Air-mac 1824_GB_Python_1 % sudo pip3 install virtualenv
Password:
WARNING: The directory '/Users/mac/Library/Caches/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting virtualenv
  Downloading virtualenv-20.8.1-py2.py3-none-any.whl (5.3 MB)
     |████████████████████████████████| 5.3 MB 4.6 MB/s
Collecting distlib<1,>=0.3.1
  Downloading distlib-0.3.3-py2.py3-none-any.whl (496 kB)
     |████████████████████████████████| 496 kB 11.3 MB/s
Collecting backports.entry-points-selectable>=1.0.4
  Downloading backports.entry_points_selectable-1.1.0-py2.py3-none-any.whl (6.2 kB)
Collecting platformdirs<3,>=2
  Downloading platformdirs-2.4.0-py3-none-any.whl (14 kB)
Collecting filelock<4,>=3.0.0
  Downloading filelock-3.3.0-py3-none-any.whl (9.7 kB)
Collecting six<2,>=1.9.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, platformdirs, filelock, distlib, backports.entry-points-selectable, virtualenv
Successfully installed backports.entry-points-selectable-1.1.0 distlib-0.3.3 filelock-3.3.0 platformdirs-2.4.0 six-1.16.0 virtualenv-20.8.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 21.2.3; however, version 21.3 is available.
You should consider upgrading via the '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 -m pip install --upgrade pip' command.

# установка в виртуальное окружение pillow

(venv) mac@MacBook-Air-mac 1824_GB_Python_1 % pip3 freeze
(venv) mac@MacBook-Air-mac 1824_GB_Python_1 % pip install pillow
Collecting pillow
  Using cached Pillow-8.3.2-cp39-cp39-macosx_10_10_x86_64.whl (3.0 MB)
Installing collected packages: pillow
Successfully installed pillow-8.3.2
(venv) mac@MacBook-Air-mac 1824_GB_Python_1 %

# деактивация виртуального окружения

(venv) mac@MacBook-Air-mac 1824_GB_Python_1 % deactivate
mac@MacBook-Air-mac 1824_GB_Python_1 %
