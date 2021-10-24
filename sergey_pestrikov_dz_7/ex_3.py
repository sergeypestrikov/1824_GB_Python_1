import os
from shutil import copy2

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)

def show_stat(f_path):
    stat = os.stat(f_path)
    print('{f_p}:\n\tperm - {perm}, modify {m_t:.0f}, access {a_t:.0f}'.format(
        f_p=f_path,
        perm=oct(stat.st_mode),
        m_t=stat.st_mtime,
        a_t=stat.st_atime,
    ))


add_folder = ['mainapp', 'authapp']
project_dir = '/Users/mac/PycharmProjects/1824_GB_Python_1/sergey_pestrikov_dz_7/my_project_3'

new_dir_templates = os.path.join(project_dir, 'templates')
if not os.path.exists(new_dir_templates):
    os.makedirs(new_dir_templates)

for f in add_folder:
    folder = os.path.join(new_dir_templates, f)
    if not os.path.exists(folder):
        os.makedirs(folder)

rout_1 = '/Users/mac/PycharmProjects/1824_GB_Python_1/sergey_pestrikov_dz_7/my_project_3/templates/authapp'
rout_2 = '/Users/mac/PycharmProjects/1824_GB_Python_1/sergey_pestrikov_dz_7/my_project_3/templates/mainapp'


# authapp_file_base = os.path.join(rout_1, 'base.html')
# authapp_file_index = os.path.join(rout_1, 'index.html')
# mainapp_file_base = os.path.join(rout_2, 'base.html')
# mainapp_file_index = os.path.join(rout_2, 'index.html')


src_1 = '/Users/mac/PycharmProjects/1824_GB_Python_1/sergey_pestrikov_dz_7/my_project_3/authapp/templates/authapp/base.html'
src_2 = '/Users/mac/PycharmProjects/1824_GB_Python_1/sergey_pestrikov_dz_7/my_project_3/authapp/templates/authapp/index.html'

show_stat(copy2(src_1, rout_1))
show_stat(copy2(src_1, rout_2))
show_stat(copy2(src_2, rout_1))
show_stat(copy2(src_2, rout_2))

# show_stat(copy2(src_1, mainapp_file_base))
# show_stat(copy2(src_2, mainapp_file_index))