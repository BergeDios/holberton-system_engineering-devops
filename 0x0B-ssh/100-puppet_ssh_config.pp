# updating ssh config file via puppet

exec { 'echo>':
  path     => '/usr/bin',
  command  => 'echo "   IdentityFile ~/.ssh/school\n   PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
