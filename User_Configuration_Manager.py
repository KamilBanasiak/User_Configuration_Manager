def add_setting(settings, new_pair):
    key, value = new_pair
    key = key.lower()
    value = value.lower()
    for i in settings.keys():
        if i == key:
            return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    settings.update({key: value})
    return f'Setting \'{key}\' added with value \'{value}\' successfully!'

def update_setting(settings, updated_pair):
    key, value = updated_pair
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        settings.update({key: value})
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        settings.pop(key)
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(settings):
    if settings == {}:
        return 'No settings available.'
    else:
        view = f'Current User Settings:\n'
        for key, value in settings.items():
            view += f'{key.title()}: {value}\n'
        return view

test_settings = {'theme': 'dark',
                 'notifications': 'enabled',
                 'volume': 'high'}

#print(add_setting(test_settings, ('language', 'Polish')))
#print(add_setting(test_settings, ('volume', 'low')))
#print(update_setting(test_settings, ('Volume', 'LOW')))
#print(update_setting(test_settings, ('language', 'Polish')))
#print(delete_setting(test_settings, 'theme'))
#print(delete_setting(test_settings, 'language'))
#print(view_settings(test_settings))
#print(view_settings({}))