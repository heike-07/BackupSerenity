FROM alpine:latest
LABEL author="heike07"
WORKDIR /usr/local
COPY ./nginx-1.24.0 /usr/local/nginx-1.24.0
COPY ./ngx-fancyindex-0.5.2 /usr/local/ngx-fancyindex-0.5.2
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add --no-cache gcc libc-dev make openssl-dev pcre-dev zlib-dev linux-headers curl \
    && cd /usr/local/nginx-1.24.0/ \
    && ./configure --prefix=/etc/nginx \
        --sbin-path=/usr/sbin/nginx \
        --modules-path=/usr/lib/nginx/modules \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --pid-path=/var/run/nginx.pid \
        --lock-path=/var/run/nginx.lock \
        --http-client-body-temp-path=/var/cache/nginx/client_temp \
        --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
        --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
        --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
        --conf-path=/etc/nginx/nginx.conf \
        --with-http_ssl_module \
        --add-module=/usr/local/ngx-fancyindex-0.5.2 \
        --with-compat \
        --with-file-aio \
        --with-threads \
        --with-http_addition_module \
        --with-http_auth_request_module \
        --with-http_dav_module \
        --with-http_flv_module \
        --with-http_gunzip_module \
        --with-http_gzip_static_module \
        --with-http_mp4_module \
        --with-http_random_index_module \
        --with-http_realip_module \
        --with-http_secure_link_module \
        --with-http_slice_module \
        --with-http_ssl_module \
        --with-http_stub_status_module \
        --with-http_sub_module \
        --with-http_v2_module \
        --with-mail \
        --with-mail_ssl_module \
        --with-stream --with-stream_realip_module \
        --with-stream_ssl_module \
        --with-stream_ssl_preread_module \
    && make \
    && make install \
    && mkdir -p /var/cache/nginx/client_temp \
    && rm -rf /usr/local/nginx-1.24.0 \
    && rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
EXPOSE 80
CMD ["/bin/sh","-c","nginx -g 'daemon off;'"]