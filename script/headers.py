import requests
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='Recoge cabeceras de seguridad de un sitio web')
parser.add_argument('--url', required=True, help='URL a analizar')
args = parser.parse_args()
url = args.url

response = requests.get(url, verify=False)
print('Cabeceras de seguridad:')
for header in ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options']:
    print(f'{header}: {response.headers.get(header)}')