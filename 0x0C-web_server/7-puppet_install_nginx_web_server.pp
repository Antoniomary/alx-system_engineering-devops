# This manifest installs and configures Nginx to
#      -> liston on port 80
#      -> perform a 301 redirect when querying /redirect_me.

package { 'nginx':
  ensure => 'present',
}

-> exec { 'ufw_allow_http':
  command  => "sudo ufw allow 'Nginx HTTP'",
  provider => shell,
}

-> exec { 'ufw_allow_tcp':
  command  => 'sudo ufw allow ssh',
  provider => shell,
}

-> file_line { 'redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default':
  line   => 'rewrite /redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

-> service { 'ufw':
  ensure  => running,
  enable  => true,
}

-> service { 'nginx':
  ensure  => running,
}
