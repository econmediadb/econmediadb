# Fedora Maintenance

## Suspend mode

Fedora Workstation goes into suspend mode, which is not handy if you want to use the computer as server.
The following command suspends this action.
```bash
sudo systemctl mask suspend.target
```

If you want the restore the previous suspend mode, you canuse this command
```bash
sudo systemctl unmask suspend.target
```

## Install Kodi on Fedora

https://www.linuxcapable.com/how-to-install-kodi-on-fedora-linux/

