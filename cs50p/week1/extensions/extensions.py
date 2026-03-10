response = input('$ ').lower().rstrip()
    # Split at '.' & get the first word from the last by indexing into [-1]
match response.split('.')[-1]:
    case 'gif':
        print('image/gif')
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case _:
        print('application/octet-stream')
