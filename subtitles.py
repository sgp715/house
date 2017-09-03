import utils
import sys


if __name__ == "__main__":

    args = sys.argv
    if len(args) < 2:
        print("Not enough arguments. You must specify a file")
        exit()
    print("Getting data")
    filename = args[1]
    df = utils.load_data(filename)
    print(df.head())
