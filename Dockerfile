FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf

COPY heart.csv /usr/share/nginx/html/heart.csv