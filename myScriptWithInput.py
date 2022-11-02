import os
import sys


def main():
    badhash = sys.argv[1]
    goodhash = sys.argv[2]
    os.system('git bisect start %s %s'%(badhash, goodhash))
    os.system('git bisect run python manage.py test')
    os.system('git bisect reset')


if __name__ == '__main__':
    main()
