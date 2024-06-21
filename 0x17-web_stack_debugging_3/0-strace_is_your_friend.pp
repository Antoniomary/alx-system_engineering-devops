# A puppet manuscript to replace a line in a file on a server

$file = '/var/www/html/wp-settings.php'

#replaces "phpp" with "php" in file
exec { 'replace_line':
  command => "sed -i 's/phpp/php/' ${file}",
  path    => ['/bin','/usr/bin']
}
