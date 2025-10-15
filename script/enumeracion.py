import socket
import argparse
import requests

parser = argparse.ArgumentParser(description='Enumeración pasiva y activa de dominios')
parser.add_argument('--domain', required=True, help='Dominio a analizar')
args = parser.parse_args()
domain = args.domain

# Enumeración pasiva: consulta DNS
print('Enumeración pasiva:')
try:
    ip = socket.gethostbyname(domain)
    print(f'DNS {domain}: {ip}')
except Exception as e:
    print(f'Error DNS: {e}')

# Whois (puerto 43)
try:
    import whois
    w = whois.whois(domain)
    print(f'Whois {domain}: {w.text[:200]}...')
except Exception as e:
    print(f'Error Whois: {e}')

# Enumeración activa: escaneo de puertos
print('\nEnumeración activa:')
target = ip if 'ip' in locals() else domain
ports = [21, 22, 80, 443]
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'Puerto abierto: {port}')
        else:
            print(f'Puerto cerrado: {port}')
    except Exception as e:
        print(f'Error escaneando puerto {port}: {e}')
    s.close()