# -*- coding: utf-8 -*-

"""This code is a part of Hydra Toolkit

.. module:: hydratk.extensions.security.translation.en.help
   :platform: Unix
   :synopsis: English language translation for Security extension help generator
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""
language = {
    'name': 'English',
    'ISO-639-1': 'en'
}

''' Security Commands '''
help_cmd = {
    'sec-msf': 'run MSF (MetaSploit Framework) command',
    'sec-zap': 'run ZAP (Zed Attack Proxy) command',

    # standalone with option profile security
    'msf': 'run MSF (MetaSploit Framework) command',
    'zap': 'run ZAP (Zed Attack Proxy) command'
}

''' Security Options '''
help_opt = {
    'sec-action': {'{h}--sec-action <string>{e}': {'description': 'action - export|scan|spider|start|stop', 'commands': ('sec-zap')}},
    'sec-format': {'{h}[--sec-format <string>]{e}': {'description': 'output format - har|html|json|md|xml, default json, supported for action export', 'commands': ('sec-zap')}},
    'sec-host': {'{h}[--sec-host <string>]{e}': {'description': 'proxy host, default 127.0.0.1', 'commands': ('sec-zap')}},
    'sec-method': {'{h}[--sec-method <string>]{e}': {'description': 'HTTP method, default GET, supported for action scan', 'commands': ('sec-zap')}},
    'sec-output': {'{h}[--sec-output <filename>]{e}': {'description': 'output filename, supported for action export', 'commands': ('sec-zap')}},
    'sec-params': {'{h}[--sec-params <dict>]{e}': {'description': 'request parameters key1:val1|key2:val2, supported for actions scan|spider', 'commands': ('sec-zap')}},
    'sec-path': {'{h}[--sec-path <path>]{e}': {'description': 'proxy path, default zap.sh, supported for action start', 'commands': ('sec-zap')}},
    'sec-port': {'{h}[--sec-port <number>]{e}': {'description': 'proxy port, default 8080', 'commands': ('sec-zap')}},
    'sec-type': {'{h}[--sec-type <string>]{e}': {'description': 'output type - alert|msg|url, default alert, supported for action export', 'commands': ('sec-zap')}},
    'sec-url': {'{h}[--sec-url <string>]{e}': {'description': 'URL, supported for actions export|scan|spider', 'commands': ('sec-zap')}},

    # standalone with option profile security
    'action': {'{h}--action <string>{e}': {'description': 'action - export|scan|spider|start|stop', 'commands': ('zap')}},
    'format': {'{h}[--format <string>]{e}': {'description': 'output format - har|html|json|md|xml, default json, supported for action export', 'commands': ('zap')}},
    'host': {'{h}[--host <string>]{e}': {'description': 'proxy host, default 127.0.0.1', 'commands': ('zap')}},
    'method': {'{h}[--method <string>]{e}': {'description': 'HTTP method, default GET, supported for action scan', 'commands': ('zap')}},
    'output': {'{h}[--output <filename>]{e}': {'description': 'output filename, supported for action export', 'commands': ('zap')}},
    'params': {'{h}[--params <dict>]{e}': {'description': 'request parameters key1:val1|key2:val2, supported for actions scan|spider', 'commands': ('zap')}},
    'path': {'{h}[--path <path>]{e}': {'description': 'proxy path, default zap.sh, supported for action start', 'commands': ('zap')}},
    'port': {'{h}[--port <number>]{e}': {'description': 'proxy port, default 8080', 'commands': ('zap')}},
    'type': {'{h}[--type <string>]{e}': {'description': 'output type - alert|msg|url, default alert, supported for action export', 'commands': ('zap')}},
    'url': {'{h}[--url <string>]{e}': {'description': 'URL, supported for actions export|scan|spider', 'commands': ('zap')}}
}
