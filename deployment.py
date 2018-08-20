import argparse
import os

if __name__ == '__main__':
    filename = 'commit_list.txt'
    if not os.path.isfile(filename):
        f = open(filename, 'w')
        f.close()
    parser = argparse.ArgumentParser(description='Great Description To Be Here', add_help=True)