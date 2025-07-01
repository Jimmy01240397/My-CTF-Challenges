FROM debian:bookworm as builder

RUN apt update && apt install -y --no-install-recommends gcc make libc6-dev && apt clean && rm -rf /var/lib/apt/lists/*

COPY readflag /src

WORKDIR /src

RUN make clean && make

FROM debian:bookworm as release

RUN apt update && \
    apt install -y --no-install-recommends apache2 python3 python3-pip && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install jinja2 --break-system-packages

RUN rm -rf /usr/lib/cgi-bin/* && \
    rm -rf /var/www/html && \
    rm -rf /var/log/apache2/* && \
    ln -s /dev/null /var/log/apache2/access.log && \
    ln -s /dev/null /var/log/apache2/error.log && \
    ln -s /dev/null /var/log/apache2/other_vhosts_access.log && \
    a2enmod cgid && \
    a2enmod rewrite && \
    a2enmod actions

COPY --from=builder /src/bin/readflag /readflag
COPY cgi-bin /usr/lib/cgi-bin
COPY apache2/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY src /var/www/html

RUN chown -R www-data:www-data /var/www && chmod +x /docker-entrypoint.sh /usr/lib/cgi-bin/* && chmod 4755 /readflag

CMD ["/docker-entrypoint.sh"]



