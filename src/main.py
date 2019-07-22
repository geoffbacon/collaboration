import json


def read(fname):
    """Read a JSON file called `file_name`."""
    with open(file_name) as f:
        return json.load(file)

def write(lines, file_name):
    """Write `lines` to file called `file_num`."""
    if lines:
        with open(file_name, 'r') as file:
            file.write('\n'.join(lines))

def show_user(name, age):
    """Print the details of a user."""
    print('{} is {} years old'.format(age, name))

if __name__ == '__main__':
    show_user('Ben', 25)
