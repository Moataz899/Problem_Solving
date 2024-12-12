url = input()

parameters = url.split('?')[1].split('&')

for param in parameters:
    key, value = param.split('=')
    print(f'{key}: {value}')
    