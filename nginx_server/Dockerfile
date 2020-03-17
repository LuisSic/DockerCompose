FROM ubuntu:latest
RUN apt-get update
RUN apt-get install nginx -y
COPY /app /var/www/html/
CMD ["nginx","-g","daemon off;"