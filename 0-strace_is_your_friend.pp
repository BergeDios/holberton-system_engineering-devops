# Fix error 500 when a GET HTTP method is requested to apache web server

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
