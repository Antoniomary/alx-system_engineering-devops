# This manifest set up your client SSH configuration file
# so that you can connect to a server without typing a password

file_line { 'private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '        PasswordAuthentication no',
}

file_line { 'file to read':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '        IdentityFile ~/.ssh/school',
}
