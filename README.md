# flatpak-example-pywebview

This is a flatpak example using pywebview in flatpak


## Setup

### Install flatpak

Please follow Flathub's [setup](https://flathub.org/setup) for your OS distribution.

### Install flatpak-builder for building flatpak

Each OS distribution has **flatpak-builder** package:
* Alpine: `apk add flatpak-builder`
* Arch Linux: `pacman -S flatpak-builder`
* Debian: `apt install flatpak-builder`
* Fedora: `yum install flatpak-builder`
* Ubuntu: `apt install flatpak-builder`
* ...

### Get flatpak-pip-generator

Because this example is written in Python and uses [pywebview](https://github.com/r0x0r/pywebview), which depends on [bottle](https://bottlepy.org/) ..., and more.
The dependencies, like pywebview and bottle ... must be installed as part of the flatpak app as well.
So, we need [flatpak-builder-tools](https://github.com/flatpak/flatpak-builder-tools)'s **flatpak-pip-generator** to generate the required module’s meta information for the manifest.
```
$ git clone https://github.com/flatpak/flatpak-builder-tools
$ pip install requirements-parser
```


## Build

1. Get repository:
   ```
   git clone https://github.com/starnight/flatpak-example-pywebview
   ```
2. Install SDK.  The flatpak-example-pywebview uses GNOME 46 runtime now:
   ```
   flatpak install flathub org.gnome.Sdk//46
   ```
3. Use **flatpak-pip-generator** to generate `python3-requirements.json`, which lists dependencies as a module in the manifest `io.github.starnight.http.yml`:
   ```
   $ python3 ~/flatpak-builder-tools/pip/flatpak-pip-generator --requirements-file=requirements.txt
   ========================================================================
   Downloading sources
   ========================================================================
   Running: "pip3 download --exists-action=i --dest /tmp/pip-generator-python3-requirementssk5q_i_v -r /tmp/requirements.rlw03ctw"
   Collecting pywebview (from -r /tmp/requirements.rlw03ctw (line 1))
     Obtaining dependency information for pywebview from https://files.pythonhosted.org/packages/94/eb/fec1105c0e3b459266637bdc867bd064619eddb170dc0c9d12f20ad7690c/pywebview-4.4.1-py3-none-any.whl.metadata
     Downloading pywebview-4.4.1-py3-none-any.whl.metadata (4.0 kB)
   Collecting proxy-tools (from pywebview->-r /tmp/requirements.rlw03ctw (line 1))
     Using cached proxy_tools-0.1.0.tar.gz (3.0 kB)
     Preparing metadata (setup.py) ... done
   Collecting bottle (from pywebview->-r /tmp/requirements.rlw03ctw (line 1))
   {
       "name": "python3-pywebview",
       "buildsystem": "simple",
       "build-commands": [
           "pip3 install --verbose --exists-action=i --no-index --find-links=\"file://${PWD}\" --prefix=${FLATPAK_DEST} \"pywebview\" --no-build-isolation"
       ],
       "sources": [
           {
               "type": "file",
               "url": "https://files.pythonhosted.org/packages/bb/1f/5977ea88c6a3df6199db97d320e5da816d415d1eb75a987a1f6823d5cc9d/bottle-0.12.25-py3-none-any.whl",
               "sha256": "d6f15f9d422670b7c073d63bd8d287b135388da187a0f3e3c19293626ce034ea"
           },
           {
               "type": "file",
               "url": "https://files.pythonhosted.org/packages/f2/cf/77d3e19b7fabd03895caca7857ef51e4c409e0ca6b37ee6e9f7daa50b642/proxy_tools-0.1.0.tar.gz",
               "sha256": "ccb3751f529c047e2d8a58440d86b205303cf0fe8146f784d1cbcd94f0a28010"
           },
           {
               "type": "file",
               "url": "https://files.pythonhosted.org/packages/94/eb/fec1105c0e3b459266637bdc867bd064619eddb170dc0c9d12f20ad7690c/pywebview-4.4.1-py3-none-any.whl",
               "sha256": "575b1362953349104b6ec08eed115c5a51d0d8b8e029b35335458cfa759ced1b"
           },
           {
               "type": "file",
               "url": "https://files.pythonhosted.org/packages/24/21/7d397a4b7934ff4028987914ac1044d3b7d52712f30e2ac7a2ae5bc86dd0/typing_extensions-4.8.0-py3-none-any.whl",
               "sha256": "8f92fc8806f9a6b641eaa5318da32b44d401efaac0f6678c9bc448ba3605faa0"
           }
       ]
   }

   $ mv python3-requirements.json build-aux/flatpak/
   ```
   PS. This repository already provides `python3-requirements.json`.  So, this step can be skipped.
4. Build & package as flatpak **io.github.starnight.http** application with the manifest:
   ```
   flatpak-builder build-dir build-aux/flatpak/io.github.starnight.http.yml --force-clean --install --user
   ```
5. Show flatpak **io.github.starnight.http** application:
   ```
   $ flatpak info io.github.starnight.http
             ID: io.github.starnight.http
            Ref: app/io.github.starnight.http/x86_64/master
           Arch: x86_64
         Branch: master
         Origin: http-origin
     Collection:
   Installation: user
      Installed: 2.0 MB
        Runtime: org.gnome.Platform/x86_64/46
            Sdk: org.gnome.Sdk/x86_64/46

         Commit: ca09edd93f65d056abbfaa999efbf5ab2913abe1015bff8bdd85d04519a0fdef
        Subject: Export io.github.starnight.http
           Date: 2024-04-03 15:23:40 +0000
   ```


## Execute

Run flatpak **io.github.starnight.http** application:
`flatpak run io.github.starnight.http`

Or, you can click the application launcher on desktop!

If you want to remove it: `flatpak uninstall io.github.starnight.http`


## Reference

* [Flatpak document](https://docs.flatpak.org/en/latest/)
