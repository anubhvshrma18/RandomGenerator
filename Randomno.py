import datetime

def random_generator():
    random_no= datetime.datetime.now().timestamp()
    no = int(random_no)
    return no%10

if __name__ == '__main__':
    print(random_generator())
