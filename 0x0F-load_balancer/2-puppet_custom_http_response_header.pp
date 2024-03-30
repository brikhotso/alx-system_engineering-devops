# Puppet manifest to install nginx with custom HTTP header

package { 'nginx':
  ensure => installed,
}

nginx::resource::vhost { 'default':
  ensure       => present,
  www_root     => '/var/www/html',
  index_files  => ['index.html'],
  listen_port  => '80',
  server_name  => 'localhost',
  rewrite      => {
    'redirect_me' => {
      'from' => '^/redirect_me',
      'to'   => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
    },
  },
  custom_config => {
    'add_header X-Served-By' => $facts['hostname'],
  },
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
