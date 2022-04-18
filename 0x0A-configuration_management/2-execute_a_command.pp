# executing a command with puppet to kill a procces killemnow

exec { '/killmenow':
  command  => 'pkill killmenow',
  path     => '/usr/bin',
  provider => shell,
}
