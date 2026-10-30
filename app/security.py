import ipaddress
import socket
from urllib.parse import urlparse

class UnsafeURLError(ValueError):

def validate_url(url: str) -> str:
    parsed = urlparsed(url)

    if parsed.scheme not in ("http", "https"):
       raise UnsafeURLError("Solo se permiten URLs http o https.")


    if not parsed.hostname:
       raise UnsafeURLError("La URL no tiene un host válido.")

    try:
        infos = socket.getaddrinfo(parsed.hostname, None)
    except socket.gaierror:


        raise UnsafeURLError("No se pudo resolver el dominio.")

    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if (

            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
            or ip.is_unspecified
        ):

            raise UnsafeURLError("La URL apunta a una dirección interna no permitida.")
return url
