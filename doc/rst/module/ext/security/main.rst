.. _module_ext_security_main:

Main
====

This sections contains module documentation of main security modules.

bootstrapper
^^^^^^^^^^^^

Module provides bootstrapper (method run_app) for Security extension. 
You can run it in standalone mode using method command security (i.e. installed to /usr/local/bin/security).
Unit tests available at hydratk/extensions/security/bootstrapper/01_methods_ut.jedi

security
^^^^^^^^

Modules provides class Extension inherited from class hydratk.core.extension.Extension.
Unit tests available at hydratk/extensions/security/security/01_methods_ut.jedi

**Methods** :

* _init_extension

Method sets extension metadata (id, name, version, author, year). 

* _check_dependencies

Method checks if all required modules are installed.

* _uninstall

Method returns additional uninstall data.

* _register_actions

Methods registers actions hooks according to profile htk (default mode) or security (standalone mode)

* _register_htk_actions

Method registers action hooks for default mode.

commands - sec-zap
long options - sec-action, sec-format, sec-host, sec-method, sec-output, sec-params, sec-path, sec-port, sec-type, sec-url

* _register_standalone_actions

Method registers action hooks for standalone mode.

commands - help, zap
long options - action, format, host, method, output, params, path, port, type, url
global options - config, debug, debug-channel, language, run-mode, force, interactive

* sec_zap

Method handles command zap. It uses option sec-action (action name, export|scan|spider|start|stop). Remaining options are optional:
sec-path (path to proxy control script, configurable, default zap.sh), sec-host (proxy host, configurable, default 127.0.0.1),
sec-port (proxy port, configurable, default 8080), sec-url (url), sec-method (HTTP method, default GET), sec-params (request parameters
in dict form key1:val1|key2:val2), sec-type (output type, alert|msg|url, default alert), sec-format (output format, har|html|json|md|xml,
default json), sec-output (output filename).

  .. code-block:: python
  
     # start zap
     htk --sec-action start --sec-path /usr/share/zaproxy/zap.sh --sec-host 127.0.0.1 --sec-port 8080 sec-zap
     
     # stop zap
     htk --sec-action stop sec-zap
     
     # spider
     htk --sec-action spider --sec-url http://localhost/mutillidae/index.php sec-zap

     # scan
     htk --sec-action scan --sec-url http://localhost/mutillidae/index.php?page=user-info.php 
     --sec-params "username:ZAP|password:ZAP|user-info-php-submit-button:View Account Details" sec-zap
     
     htk --sec-action scan --sec-url http://localhost/mutillidae/index.php?page=login.php --sec-method POST
     --sec-params "username:ZAP|password:ZAP|login-php-submit-button:Login" sec-zap
     
     # export
     htk --sec-action export --sec-type alert --sec-format html --sec-output alert.html sec-zap
     htk --sec-action export --sec-type msg --sec-format har --sec-output msg.har sec-zap
     htk --sec-action export --sec-type url --sec-format json --sec-output url.json sec-zap

configuration
^^^^^^^^^^^^^

Configuration is stored in /etc/hydratk/conf.d/hydratk-ext-security.conf   
It has separate configuration for each tool.

**zap**

* path - path to ZAP proxy control script, default zap.sh
* host - proxy host, default 127.0.0.1             
* port - proxy port, default 8080