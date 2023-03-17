# Composer how to use it

## Get Composer
[markdown ??](https://getcomposer.org/doc/01-basic-usage.md)

## make it command
```
sudo mv composer.phar /usr/local/bin/composer
```
## start new project
'''
composer init
'''

## Reflect changes
```
composer update
```

## Make autolaoder up to date
```
composer dump-autoload
```

## Require new module
perhaps slim
```
composer require slim/slim:^4.0
composer require slim/psr7
```

### Add autolaoder to PHP
```
require 'vendor/autoload.php';
```

[source](https://getcomposer.org/doc/03-cli.md#config)
