import click
import requests
from requests.exceptions import HTTPError
import time
import datetime
import os


def clear_console():
  os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def render_output(output_array):
  clear_console()
  for output in output_array:
    print('\n' + output);


def replace(array, index, item):
  if index < len(array):
    array[index] = item;
  else: 
    array.insert(index, item)
  return array


def ping_server(url, name):
  try: 
    response = requests.get(url);
    response.raise_for_status()
  except HTTPError as http_err: 
    time_only = datetime.datetime.now().time()
    return f'{url} {name.upper()} {time_only} \nHTTP error: {http_err}'
  except Exception as err:
    time_only = datetime.datetime.now().time()
    return f'{url} {name.upper()} {time_only} \nNon HTTP error: {err}'
  else:
    return f'{url} {name.upper()} is OK'


def main_cycle(urls, names): 
  iterator = 0
  status = []

  while (iterator) < len(urls):
    status = replace(status, iterator, ping_server(urls[iterator], names[iterator]))
    iterator = iterator + 1
    
  render_output(status)
  iterator = 0
  
  while (iterator) < len(urls):
    status = replace(status, iterator, ping_server(urls[iterator], names[iterator]))
    render_output(status)

    if (iterator) == len(urls) - 1: 
      iterator = 0
    else: 
      iterator = iterator + 1
    time.sleep(60 * 10)


@click.command()
@click.option('--urls', '-u', help='Urls to ping over time', prompt='Enter urls of servers')
@click.option('--names', '-n', help='Names of servers to ping', prompt='Enter names for servers')
def health(urls, names):
  '''
  Cli to ping servers over time

  '''
  urls = urls.split()
  names = names.split()

  main_cycle(urls, names);
