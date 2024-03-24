# SSH

## What is a server?
A server is a computer program or device that provides functionality to other programs or devices, known as clients, in a network. Servers can provide various services such as file storage, email hosting, website hosting, or database management, among others.

## Where do you find it?
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
* Press Ctrl + Shift + V to paste the contents into the editor.

Save and exit the editor:
* In vi, type :wq and press Enter to save and exit.
* In emacs, type C-x C-s C-x C-c to save and exit.

## Notes (Task 3)

### Having Trouble Logging Into the Server?
If you're having trouble logging in, here's what you should do:

* Check Your Private Key Path: Make sure the path to your private key is correct. You can do this by navigating to the .ssh directory (cd ~/.ssh) and checking if the school file is there.
* Verify Public Key Matching: Check if the public key on your computer matches the private key you're using. You can do this by typing cat ~/ssh/school.pub. It should be identical to what's on your profile.
* Using Previous Public Key: If you've used a public key from a previous project (~/.ssh/id_rsa_pub), log in with the corresponding private key id_rsa.
* Check Permissions: Ensure that the .ssh directory has restrictive permissions (700) and that the private key file has permissions set to 600.
* Review SSH Configuration: Take a look at the ssh_config file and make sure the permissions are set correctly.
* Number Authorized Keys in Vi: If you need to number your authorized keys in vi, type set number in the editor.
* Edit authorized_keys with sudo Permission: Remember to edit the authorized_keys file with sudo permission if necessary.
