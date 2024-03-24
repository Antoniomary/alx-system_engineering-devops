# This manifest set up your client SSH configuration file
# so that you can connect to a server without typing a password
file { '~/.ssh/config':
  ensure => present,
}

file_line { 'host name':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'Host 35.153.232.249',
}

file_line { 'private key':
  ensure => present,
  path   => '~/.ssh/config',
  line   => '        PasswordAuthentication no',
}

file_line { 'file to read':
  ensure => present,
  path   => '~/.ssh/config',
  line   => '        IdentityFile ~/.ssh/school',
}
