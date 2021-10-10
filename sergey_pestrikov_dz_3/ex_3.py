def thesaurus(*names):
    my_names = {name.title() for name in names}
    my_list = [name[0].upper() for name in my_names]
    my_dict = {k: list() for k in my_list}


    for name in my_names:
        my_dict[name[0]].append(name)

    return my_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Мария', 'Саша', 'Паша', 'Сережа'))