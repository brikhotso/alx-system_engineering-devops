# SSH

## What is a server?
A server is a computer program or device that provides functionality to other programs or devices, known as clients, in a network. Servers can provide various services such as file storage, email hosting, website hosting, or database management, among others.

## Where do you find it:
Servers are typically housed in data centers or server rooms with controlled environments optimized for their operation. These locations provide appropriate cooling, power supply, and security measures to ensure the servers' smooth functioning.

## What is SSH?
SSH stands for Secure Shell. It is a cryptographic network protocol used for secure communication between a client and a server over an unsecured network. SSH provides encrypted connections, authentication, and tunneling capabilities, making it a widely used protocol for accessing remote systems securely.

## How to create an SSH RSA key pair:
You can create an SSH RSA key pair using the ssh-keygen command-line tool.

```
ssh-keygen -t rsa -b 4096 -f id_rsa -N brenda
```

* t: type of key to create, in this case, RSA.
* b: Number of bits in the key. The longer the legth the more secure.
* f: filename of the generated key files. private key will usually take the name as is and matching public key will have a .pub extension (id_rsa.pub.
* N: passphrase to encrypt the private key.Think of it as private key password.

## How to connect to a remote host using an SSH RSA key pair :
To connect use ssh command followed by the username and hostname of the remote host.

```
ssh -i /path/to/private_key username@hostname
```

Replace /path/to/private_key with the path to your private key file, username with your username on the remote host, and hostname with the hostname or IP address of the remote host.

## SSH config:
The ssh_config file typically contains configuration options for SSH client behavior. Some common configurations include:

* Host: Specifies options for a particular host. You can define multiple host blocks with different configurations.
* Hostname: Specifies the hostname or IP address of the remote host.
* User: Specifies the username to use when connecting to the remote host.
* IdentityFile: Specifies the path to the private key file to use for authentication.
* Port: Specifies the port number to connect to on the remote host.
* ForwardAgent: Enables SSH agent forwarding, allowing authentication to be passed through to remote hosts.


## How to add a public key to authorized keys:
To add a public key to the authorized_keys file on the remote host, you can manually append the public key to the file. Here's an example:

### method_1

Log into the server using password authentication:

```
ssh -i /path/to/private_key username@hostname
```

Once logged in, use the following command to append the public key to the authorized_keys file:

```
echo "PASTE_YOUR_PUBLIC_KEY_HERE" >> ~/.ssh/authorized_keys
```

### method_2

Log into the server using password authentication:

```
ssh -i /path/to/private_key username@hostname
```

Once logged in, use the following command to append the public key to the authorized_keys file:

```
sudo vi ~/.ssh/authorized_keys
```

Paste the copied public key into the file:
Press Ctrl + Shift + V to paste the contents into the editor.

Save and exit the editor:
In vi, type :wq and press Enter to save and exit.
In emacs, type C-x C-s C-x C-c to save and exit.

## Notes (task 3)

### issues logging into server?

* check that you private key path is correct ( eg for ~/.ssh/school) cd ~/.ssh ,ls and check if school file is there
* check if public key in the intranet matches that private key (cat ~/ssh/school.pub) this this be identical to whats on your intranet profile
* if you decide to use the public key generated from previous project(~/.ssh/id_rsa_pub) login with the corresponding private key id_rsa
* check permissions. The .ssh directory restrictive permissions (700), and the private_key_file  permissions set to 600.
* check ssh_config file and set the correct permmissions
* to number your authorised keys in vi (ect ,type set number)
* remember to edit authorised_keys with sudo permission
