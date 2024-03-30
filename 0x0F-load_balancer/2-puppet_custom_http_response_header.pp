# Puppet manifest to install nginx with custom HTTP header

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => present,
}

file_line { 'nginx_redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;",
}

file_line { 'header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'listen 80 default_server;',
  match  => 'http {',
  line   => "add_header X-Served-By \"${hostname}\";",
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
