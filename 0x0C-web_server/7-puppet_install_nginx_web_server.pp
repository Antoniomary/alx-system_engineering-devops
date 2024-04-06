# This manifest installs and configures Nginx to
#      -> liston on port 80
#      -> perform a 301 redirect when querying /redirect_me.

exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

package { 'nginx':
  ensure  => present,
  require => Exec['update'],
}

exec { 'index_html':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
  require  => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
