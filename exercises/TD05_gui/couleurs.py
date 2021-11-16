def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
print(get_color(10,10,10))