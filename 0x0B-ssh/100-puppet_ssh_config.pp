# Connect to a server without typing a password
# Configure using the private key ~/.ssh/school
# Refuse to authenticate using a password


$ssh_config_content = '
Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
'

file { 'ssh_config':
  path    => '/etc/ssh/ssh_config',
  content => $ssh_config_content,
}
