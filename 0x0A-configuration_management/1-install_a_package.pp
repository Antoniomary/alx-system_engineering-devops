# This manifest installs flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

# gets werkzerg v. 2.1.1 as it can work with the above flask version
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
