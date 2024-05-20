# Using vncserver

Performing a VNC installation requires a VNC viewer running on your workstation or another terminal computer. 

## Step 1: Installing VNC on Fedora

After connecting to your server with SSH, update your list of packages:

```bash
sudo dnf install tigervnc-server
```

Next, run the `vncserver` command to set a VNC access password, create the initial configuration files, and start a VNC server instance:

```bash
vncserver
```

You’ll be prompted to enter and verify a password to access your machine remotely:

```bash
Output
You will require a password to access your desktops.

Password:
Verify:
```

The password must be between six and eight characters long. Passwords more than 8 characters will be truncated automatically.


## Step 2: Connecting to the VNC Desktop Securely

VNC itself doesn’t use secure protocols when connecting. To securely connect to your server, you’ll establish an SSH tunnel and then tell your VNC client to connect using that tunnel rather than making a direct connection.

Create an SSH connection on your local computer that securely forwards to the `localhost` connection for VNC. You can do this via the terminal on Linux or macOS with the following `ssh` command:

```bash
ssh -L 59000:localhost:5901 -C -N -l sammy your_server_ip
```

Here’s what this ssh command’s options mean:
- `-L 59000:localhost:5901`: The `-`L switch specifies that the given port on the local computer (`59000`) is to be forwarded to the given host and port on the destination server (`localhost:5901`, meaning port `5901` on the destination server, defined as `your_server_ip`). Note that the local port you specify is somewhat arbitrary; as long as the port isn’t already bound to another service, you can use it as the forwarding port for your tunnel.
- `-C`: This flag enables compression which can help minimize resource consumption and speed things up.
- `-N`: This option tells `ssh` that you don’t want to execute any remote commands. This setting is useful when you just want to forward ports.
- `-l sammy your_server_ip`: The `-l` switch let’s you specify the user you want to log in as once you connect to the server. Make sure to replace `sammy` and `your_server_ip` with the name of your non-root user and your server’s IP address.


## Step 3: Use VNC Client on your local machine to access the server

Use `TigerVNC Viewer`to access `localhost:59000`.


## Source

- [How to Install and Configure VNC on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04#step-3-connecting-to-the-vnc-desktop-securely)
- [Installing Using VNC (fedoraproject.org)](https://docs.fedoraproject.org/en-US/fedora/f36/install-guide/advanced/VNC_Installations/)
