.. install_ext_security:

Security
========

You have 2 options how to install security extension.

Package
^^^^^^^

Install it via Python package managers PIP or easy_install.

  .. code-block:: bash
  
     $ sudo pip install --no-binary :all: hydratk-ext-security
     
  .. code-block:: bash
  
     $ sudo easy_install hydratk-ext-security
     
  .. note::
  
     PIP needs option --no-binary to run setup.py install.
     Otherwise it runs setup.py bdist_wheel.     

Source
^^^^^^

Download the source code from GitHub or PyPi and install it manually.
Full PyPi URL contains MD5 hash, adapt sample code.

  .. code-block:: bash
  
     $ git clone https://github.com/hydratk/hydratk-ext-security.git
     $ cd ./hydratk-ext-security
     $ sudo python setup.py install
     
  .. code-block:: bash
  
     $ wget https://python.org/pypi/hydratk-ext-security -O hydratk-ext-security.tar.gz
     $ tar -xf hydratk-ext-security.tar.gz
     $ cd ./hydratk-ext-security
     $ sudo python setup.py install
     
  .. note::
  
     Source is distributed with Sphinx (not installed automatically) documentation in directory doc. 
     Type make html to build local documentation however is it recommended to use up to date online documentation.     
     
Requirements
^^^^^^^^^^^^     
     
Several python modules are used.
These modules will be installed automatically, if not installed yet.

* hydratk
* python-owasp-zap-v2.4
* simplejson    
     
Installation
^^^^^^^^^^^^

See installation example, Python 2.7.

  .. code-block:: bash
  
     running install
     running bdist_egg
     running egg_info
     creating src/hydratk_ext_security.egg-info
     writing src/hydratk_ext_security.egg-info/PKG-INFO
     writing top-level names to src/hydratk_ext_security.egg-info/top_level.txt
     writing dependency_links to src/hydratk_ext_security.egg-info/dependency_links.txt
     writing entry points to src/hydratk_ext_security.egg-info/entry_points.txt
     writing manifest file 'src/hydratk_ext_security.egg-info/SOURCES.txt'
     reading manifest file 'src/hydratk_ext_security.egg-info/SOURCES.txt'
     reading manifest template 'MANIFEST.in'
     writing manifest file 'src/hydratk_ext_security.egg-info/SOURCES.txt'
     installing library code to build/bdist.linux-x86_64/egg
     running install_lib
     running build_py
     creating build
     creating build/lib.linux-x86_64-2.7
     creating build/lib.linux-x86_64-2.7/hydratk
     copying src/hydratk/__init__.py -> build/lib.linux-x86_64-2.7/hydratk
     creating build/lib.linux-x86_64-2.7/hydratk/extensions
     copying src/hydratk/extensions/__init__.py -> build/lib.linux-x86_64-2.7/hydratk/extensions
     creating build/lib.linux-x86_64-2.7/hydratk/extensions/security
     copying src/hydratk/extensions/security/__init__.py -> build/lib.linux-x86_64-2.7/hydratk/extensions/security
     ...

     creating dist
     creating 'dist/hydratk_ext_security-0.1.0a0.dev0-py2.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
     removing 'build/bdist.linux-x86_64/egg' (and everything under it)
     Processing hydratk_ext_security-0.1.0a0.dev0-py2.7.egg
     removing '/usr/local/lib/python2.7/dist-packages/hydratk_ext_security-0.1.0a0.dev0-py2.7.egg' (and everything under it)
     creating /usr/local/lib/python2.7/dist-packages/hydratk_ext_security-0.1.0a0.dev0-py2.7.egg
     Extracting hydratk_ext_security-0.1.0a0.dev0-py2.7.egg to /usr/local/lib/python2.7/dist-packages
     hydratk-ext-security 0.1.0a0.dev0 is already the active version in easy-install.pth
     Installing security script to /usr/local/bin

     Installed /usr/local/lib/python2.7/dist-packages/hydratk_ext_security-0.1.0a0.dev0-py2.7.egg
     Processing dependencies for hydratk-ext-security==0.1.0a0.dev0
     Finished processing dependencies for hydratk-ext-security==0.1.0a0.dev0 
  
Application installs following (paths depend on your OS configuration)

* security command in /usr/local/bin/security
* modules in /usr/local/lib/python2.7/dist-packages/hydratk_ext_security-0.1.0-py2.7.egg
* configuration file in /etc/hydratk/conf.d/hydratk-ext-security.conf   
     
Run
^^^

When installation is finished you can run the application.

Check hydratk-ext-security module is installed.   

  .. code-block:: bash
  
     $ pip list | grep hydratk-ext-security
     
     hydratk-ext-security (0.1.0)
     
Check installed extensions

  .. code-block:: bash
  
     $ htk list-extensions
     
     Security: Security v0.1.0 (c) [2017-2017 Petr Rašek <bowman@hydratk.org>, HydraTK team <team@hydratk.org>]
     
Type command htk help and detailed info is displayed.
Type man security to display manual page. 

  .. code-block:: bash
  
     $ htk help
     
     Commands:    
       sec-zap - run ZAP (Zed Attack Proxy) command
         Options:
           --sec-action <string> - action - export|scan|spider|start|stop
           [--sec-format <string>] - output format - har|html|json|md|xml, default json, supported for action export
           [--sec-host <string>] - proxy host, default 127.0.0.1
           [--sec-method <string>] - HTTP method, default GET, supported for action scan
           [--sec-output <filename>] - output filename, supported for action export
           [--sec-params <dict>] - request parameters key1:val1|key2:val2, supported for actions scan|spider
           [--sec-path <path>] - proxy path, default zap.sh, supported for action start
           [--sec-port <number>] - proxy port, default 8080
           [--sec-type <string>] - output type - alert|msg|url, default alert, supported for action export
           [--sec-url <string>] - URL, supported for actions export|scan|spider                     
           
You can run Security also in standalone mode.  

  .. code-block:: bash
  
     $ security help
     
     Security v0.1.0
     (c) 2017-2017 Petr Rašek <bowman@hydratk.org>, HydraTK team <team@hydratk.org>
     Usage: security [options] command

     Commands:
        help - prints help
        zap - run ZAP (Zed Attack Proxy) command
           Options:
              --action <string> - action - export|scan|spider|start|stop
              [--format <string>] - output format - har|html|json|md|xml, default json, supported for action export
              [--host <string>] - proxy host, default 127.0.0.1
              [--method <string>] - HTTP method, default GET, supported for action scan
              [--output <filename>] - output filename, supported for action export
              [--params <dict>] - request parameters key1:val1|key2:val2, supported for actions scan|spider
              [--path <path>] - proxy path, default zap.sh, supported for action start
              [--port <number>] - proxy port, default 8080
              [--type <string>] - output type - alert|msg|url, default alert, supported for action export
              [--url <string>] - URL, supported for actions export|scan|spider


     Global Options:
        -c, --config <file> - reads the alternate configuration file
        -d, --debug <level> - debug turned on with specified level > 0
        -e, --debug-channel <channel number, ..> - debug channel filter turned on
        -f, --force - enforces command
        -i, --interactive - turns on interactive mode
        -l, --language <language> - sets the text output language, the list of available languages is specified in the docs
        -m, --run-mode <mode> - sets the running mode, the list of available modes is specified in the docs
                                
Upgrade
=======

Use same procedure as for installation. Use command option --upgrade for pip, easy_install, --force for setup.py.
If configuration file differs from default settings the file is backuped (extension _old) and replaced by default. Adapt the configuration if needed.

Uninstall
=========    

Run command htkuninstall security Use option -y if you want to uninstall also dependent Python modules (for advanced user).                                