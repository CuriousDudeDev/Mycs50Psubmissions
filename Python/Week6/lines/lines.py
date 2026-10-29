import sys

if len(argv) < 2:
    sys.exit('Too few command-line arguments')
if len(argv) > 2:
    sys.exit('Too many command-line arguments')
if len(argv) == 2 and not (argv.endswith('.py')):
    sys.exit('Not a Python file')
else:
    try:
        file = open(argv[1] , 'r')
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        
