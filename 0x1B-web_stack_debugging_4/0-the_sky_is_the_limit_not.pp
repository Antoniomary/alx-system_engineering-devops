# This manifest increases the max number of file nginx can open

exec { 'increase_max_open_file' :
  command => "sed -i 's/-n 15/-n 1000/g' /etc/default/nginx",
  path    => ['/bin', '/usr/sbin'],
}

exec { 'restart_nginx' :
  command  => 'service nginx restart',
  provider => shell,
}
