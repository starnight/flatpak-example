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


## Build

1. Get repository:
   ```
   git clone https://github.com/starnight/flatpak-example-pywebview
   ```
2. Install SDK.  The flatpak-example-pywebview uses GNOME 45 runtime now:
   ```
   flatpak install flathub org.gnome.Sdk//45
   ```
3. Build & package as flatpak **io.github.starnight.http** application with the manifest:
   ```
   flatpak-builder build-dir build-aux/flatpak/io.github.starnight.http.yml --force-clean --install --user
   ```
4. Show flatpak **io.github.starnight.http** application:
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
        Runtime: org.gnome.Platform/x86_64/45
            Sdk: org.gnome.Sdk/x86_64/45

         Commit: 61171a2702e63df512a97b5fe527f54a348cca07a4aac61a18746c2984c85458
         Parent: c62a8fd3816cfe0dcbfb249934a8389ee5024cfffee6b04db29df3ef5cf82bdd
        Subject: Export io.github.starnight.http
           Date: 2023-10-29 15:58:08 +0000
   ```


## Execute

Run flatpak **io.github.starnight.http** application:
`flatpak run io.github.starnight.http`

Or, you can click the application launcher on desktop!

If you want to remove it: `flatpak uninstall io.github.starnight.http`


## Reference

* [Flatpak document](https://docs.flatpak.org/en/latest/)
