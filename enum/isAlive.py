import requests
import argparse
from decouple import config
import warnings
warnings.filterwarnings(action='ignore') #supress verify=False ssl certificates


def options() -> dict:

    '''
    Function to define arguments.

    Parameters
    ----------
    None

    Returns
    -------
    arg:dict Dict of arguments
    '''

    option = argparse.ArgumentParser()
    option.add_argument('-f', '--file', dest='file', help='file with url list in')
    arg = vars(option.parse_args())
    
    return arg

def isAlive(url:str) -> int:
    
    try:
        get_request = requests.get(url, verify=False)
        return get_request.status_code
    
    except Exception:
         pass

def write_to_file(file_name:str, list_of_alive_responses:list) -> None:
    
    '''
    Function to write lists to text files.

    Parameters
    ----------
    file_name:str Name of file
    list_of_alive_responses:str List of subdomains to be written to file

    Returns
    -------
    None (writes to file)
    '''

    file = open(file_name, 'w')

    for url in list_of_alive_responses:
        file.write(url)
        file.write('\n')
    file.close()


if __name__ == '__main__':
    args = options()

    alive = []
    redirect = []
   
    with open(args['file']) as file:
        for url in file:
            url = url.strip('\n')
            resp = isAlive(url)
            if resp == 200:
                alive.append(url)
            if resp == 301:
                redirect.append(url)

    folder = config('enum_outputs')
    write_to_file(folder + '/isAlive.txt', alive)
    write_to_file(folder + '/redirect.txt', redirect)


