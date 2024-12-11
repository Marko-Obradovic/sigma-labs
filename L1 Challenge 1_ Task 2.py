name = input('What\'s your first name?: ')


def name_format(name):
    return name[0].upper() + name[1:].lower()


if name_format(name) == 'Chris':
    print('Sorry... You\'re not authorised to be greeted!')
if name_format(name) == 'Alice':
    print('Hello Alice!')