import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description='Ejecuta los scripts de enumeración, cabeceras y servidor HTTP')
parser.add_argument('--domain', required=True, help='Dominio para enumeracion')
parser.add_argument('--url', required=True, help='URL para cabeceras')
args = parser.parse_args()

print('Ejecutando enumeracion.py...')
subprocess.run([sys.executable, 'enumeracion.py', '--domain', args.domain])

print('\nEjecutando headers.py...')
subprocess.run([sys.executable, 'headers.py', '--url', args.url])

print('\nEjecutando server.py...')
print('Presiona Ctrl+C para detener el servidor.')
subprocess.run([sys.executable, 'server.py'])