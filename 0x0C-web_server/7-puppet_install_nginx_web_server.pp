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
