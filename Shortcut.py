def shortcut(fname, name='mehrshad', folder='', form='.pdf'):
    if name == 'mehrshad':
        path = f"C:\\Documents\\Mehrshad\\User Intent Modeling\\{folder}"
        if folder != '':
            path += '\\'
    return path + str(fname) + form