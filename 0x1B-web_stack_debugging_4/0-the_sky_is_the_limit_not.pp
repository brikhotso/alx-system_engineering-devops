# Fix problem of high amount of requests

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep -q "15" /etc/nginx/nginx.conf'
}

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
