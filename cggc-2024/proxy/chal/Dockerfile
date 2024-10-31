From nginx:latest

RUN apt update && apt install php-fpm php-intl php-curl -y

RUN ln -s /usr/sbin/php-fpm* /usr/sbin/php-fpm

RUN echo 'php-fpm' > docker-entrypoint.d/40-php-fpm.sh && \
    chmod +x docker-entrypoint.d/40-php-fpm.sh

RUN usermod -a -G www-data nginx

