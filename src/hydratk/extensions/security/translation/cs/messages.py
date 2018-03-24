# -*- coding: utf-8 -*-

"""This code is a part of Hydra Toolkit

.. module:: hydratk.extensions.security.translation.cs
   :platform: Unix
   :synopsis: Czech language translation for Security extension
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>

"""

language = {
    'name': 'Čeština',
    'ISO-639-1': 'cs'
}


msg = {
    'sec_received_cmd': ["Obdržen příkaz: '{0}'"],
    'sec_path_not_found': ["Cesta {0} nenalezena"],
    'sec_missing_option': ["Chybí volba: {0}"],
    'sec_invalid_option_value': ["Neplatná hodnota volby: {0}, podporované hodnoty: {1}"],
    'sec_start_failed': ["Chyba při spuštění {0}"],
    'sec_stop_failed': ["Chyba při zastavení {0}"],
    'sec_msf_start': ["Spouštím MSF cesta: {0}, host: {1}, port: {2}, user: {3}, heslo: {4}"],
    'sec_msf_started': ["MSF úspěšně spuštěn"],
    'sec_msf_not_started': ["MSF proces nebyl spuštěn"],
    'sec_msf_stop': ["Zastavuji MSF"],
    'sec_msf_stopped': ["MSF úspěšně zastaven"],
    'sec_msf_call_req': ["Volám MSF metodu: {0}, parametry: {1}"],
    'sec_msf_call_res': ["MSF metoda vrátila {0}"],
    'sec_msf_connect_error': ["Chyba spojení"],
    'sec_msf_call_error': ["Chyba při volání MSF metody: {0}"],
    'sec_zap_start': ["Spouštím ZAP cesta: {0}, host: {1}, port: {2}"],
    'sec_zap_started': ["ZAP úspěšně spuštěn"],
    'sec_zap_stop': ["Zastavuji ZAP"],
    'sec_zap_stopped': ["ZAP úspěšně zastaven"],
    'sec_zap_spider_start': ["Pouštím spider na URL: {0}, parametry: {1}"],
    'sec_zap_spider_finish': ["Spider dokončen"],
    'sec_zap_spider_urls_found': ["Bylo nalezeno {0} url"],
    'sec_zap_scan_start': ["Pouštím scan na URL: {0}, metoda: {1}, parametry: {2}, url: {3}"],
    'sec_zap_scan_finish': ["Scan dokončen"],
    'sec_zap_scan_alerts_found': ["Bylo nalezeno {0} varování"],
    'sec_zap_export_start': ["Spouštím export typ: {0}, formát: {1}, output: {2}"],
    'sec_zap_export_finish': ["Export dokončen"],
    'sec_zap_export_generated': ["Exportní soubor {0} byl vytvořen"],
    'sec_zap_progress': ["Průběh {0}: {1}%"],
    'sec_zap_invalid_value': ["Neplatný {0} {1}"],
    'sec_zap_invalid_value_for_value': ["Neplatný {0} {1} pro {2} {3}"],
    'sec_zap_action_error': ["Chyba při akci {0}"]
}
