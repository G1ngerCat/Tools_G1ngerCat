# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Mauro Soria

from socket import getaddrinfo

_dns_cache = {}


def set_custom_dns(domain, addr):
    _dns_cache[domain] = getaddrinfo(addr, 65535)


def cached_getaddrinfo(*args, **kwargs):
    """
    Replacement for socket.getaddrinfo, they are the same but this function
    does cache the answer to improve the performance
    """

    host = args[0]
    if host not in _dns_cache:
        _dns_cache[host] = getaddrinfo(*args, **kwargs)

    return _dns_cache[host]
