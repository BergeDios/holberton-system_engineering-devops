exec { 'apt-get update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['sudo apt-get install -y nginx'],
}

exec { 'sudo apt-get install -y nginx':
  provider => shell,
  command  => 'sudo apt-get install -y nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider => shell,
  command  => "sudo sed -i '/^\tinclude /etc/nginx/sites-enabled/*;/a \n\tadd_header X-Served-By ${HOSTNAME};' /etc/nginx/nginx.conf",
  before   => Exec['service nginx restart'],
}

exec { 'service nginx restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
