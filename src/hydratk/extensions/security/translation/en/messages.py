# -*- coding: utf-8 -*-

"""This code is a part of Hydra Toolkit

.. module:: hydratk.extensions.security.translation.en
   :platform: Unix
   :synopsis: English language translation for Security extension
.. moduleauthor:: Petr Czaderna <pc@hydratk.org>

"""

language = {
    'name': 'English',
    'ISO-639-1': 'en'
}

msg = {
    'sec_received_cmd': ["Received command: '{0}'"],
    'sec_path_not_found': ["Path {0} not found"],
    'sec_missing_option': ["Missing option: {0}"],
    'sec_invalid_option_value': ["Invalid option {0} value, supported values: {1}"],
    'sec_start_failed': ["Failed to start {0}"],
    'sec_stop_failed': ["Failed to stop {0}"],
    'sec_msf_start': ["Starting MSF path: {0}, host: {1}, port: {2}, user: {3}, passw: {4}"],
    'sec_msf_started': ["MSF successfully started"],
    'sec_msf_not_started': ["MSF process not started"],
    'sec_msf_stop': ["Stopping MSF"],
    'sec_msf_stopped': ["MSF successfully stopped"],
    'sec_msf_call_req': ["Calling MSF method: {0}, params: {1}"],
    'sec_msf_call_res': ["MSF method returned {0}"],
    'sec_msf_connect_error': ["Failed to connect"],
    'sec_msf_call_error': ["Failed to call MSF method: {0}"],
    'sec_zap_start': ["Starting ZAP path: {0}, host: {1}, port: {2}"],
    'sec_zap_started': ["ZAP successfully started"],
    'sec_zap_stop': ["Stopping ZAP"],
    'sec_zap_stopped': ["ZAP successfully stopped"],
    'sec_zap_spider_start': ["Starting to spider URL: {0}, params:{1}"],
    'sec_zap_spider_finish': ["Spider finished"],
    'sec_zap_spider_urls_found': ["{0} url were found"],
    'sec_zap_scan_start': ["Starting to scan URL: {0}, method: {1}, params: {2}"],
    'sec_zap_scan_finish': ["Scan finished"],
    'sec_zap_scan_alerts_found': ["{0} alerts were found"],
    'sec_zap_export_start': ["Starting export type: {0}, format: {1}, output: {2}, url: {3}"],
    'sec_zap_export_finish': ["Export finished"],
    'sec_zap_export_generated': ["Export file {0} generated"],
    'sec_zap_progress': ["Progress {0}: {1}%"],
    'sec_zap_invalid_value': ["Invalid {0} {1}"],
    'sec_zap_invalid_value_for_value': ["Invalid {0} {1} for {2} {3}"],
    'sec_zap_action_error': ["Error within action {0}"]
}
