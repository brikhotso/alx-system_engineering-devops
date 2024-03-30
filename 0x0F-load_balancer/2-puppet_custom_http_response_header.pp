# Puppet manifest to install nginx with custom HTTP header

package { 'nginx':
  ensure => installed,
}

file_line { 'nginx_redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;",
}

file_line { 'header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $HOSTNAME;',
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
