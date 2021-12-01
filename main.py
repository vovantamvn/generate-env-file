import sys


def main(file_name):
    variables = []

    with open(file_name) as file:
        for line in file.readlines():
            pair = line.split('=')
            if len(pair) == 2:
                variables.append(pair[0])

    file_output = f'{file_name}.env'

    with open(file_output, 'w') as file:
        for variable in variables:
            file.write(variable + '=${' + variable + '}')


if __name__ == '__main__':
    if len(sys.argv) == 0:
        sys.stderr('You should pass the file name')
        sys.exit(1)

    main(sys.argv[1])
