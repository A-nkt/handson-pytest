from tempfile import TemporaryDirectory

def hello():
    with open('hello.txt', 'w') as f:
        f.write('Hello World!\n')

def hellov2():
    with TemporaryDirectory() as dir:
        with open('{}/hello.txt'.format(dir), 'w') as f:
            f.write('Hello World!\n')
        with open('{}/hello.txt'.format(dir), 'r') as f:
            data = f.read()
        print(data)


if __name__ == '__main__':
    hellov2()