# This manifest installs and configures Nginx to
#      -> liston on port 80
#      -> perform a 301 redirect when querying /redirect_me.

package { 'nginx':
  ensure   => installed,
  provider => 'apt-get',
}

exec { 'ufw_allow_http':
  command  => "sudo ufw allow 'Nginx HTTP'",
  require  => Package['nginx'],
  provider => shell,
}

exec { 'ufw_allow_tcp':
  command  => 'sudo ufw allow ssh',
  require  => Package['nginx'],
  provider => shell,
}

file_line { 'redirection':
  ensure => present,
  path   => '/etc/nginx/sites-available/default':
  line   => 'rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'ufw':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']

