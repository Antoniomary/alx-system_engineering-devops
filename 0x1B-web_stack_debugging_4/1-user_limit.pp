# This manifest removes the limit placed on holberton user

exec { 'remove_holberton_limit' :
  command => "sed -i '/holberton/d' /etc/security/limits.conf",
  path    => ['/bin', '/usr/sbin'],
}

