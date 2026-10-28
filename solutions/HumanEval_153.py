import re

def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_extension = ''

    for extension in extensions:
        cap = len(re.findall(r'[A-Z]', extension))
        sm = len(re.findall(r'[a-z]', extension))
        strength = cap - sm

        if strength > max_strength or (strength == max_strength and extensions.index(extension) < extensions.index(strongest_extension)):
            max_strength = strength
            strongest_extension = extension

    return f'{class_name}.{strongest_extension}'