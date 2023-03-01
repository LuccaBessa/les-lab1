from os.path import join, dirname
from dotenv import load_dotenv

from api.getData import getData
from utils.generateCSV import generateCSV


def main():
    dotenv_path = join(dirname(dirname(__file__)), '.env')

    load_dotenv(dotenv_path)

    print('Getting repositories data...')
    repos = getData()

    generateCSV(repos, 'repos')
    print('Done')


if __name__ == "__main__":
    main()
