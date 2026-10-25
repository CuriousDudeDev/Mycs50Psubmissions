name = input('Enter the file name: ')
match name.lower().strip():
    case name if name.endswith('gif'):
        print('image/gif')
    case name if name.endswith(('jpg' , 'jpeg')):
        print('image/jpeg')
    case name if name.endswith('png'):
        print('image/png')
    case name if name.endswith('pdf'):
        print('application/pdf')
    case name if name.endswith('txt'):
        print('text/plain')
    case name if name.endswith('zip'):
        print('application/zip')
    case name:
        print('application/octet-stream')
