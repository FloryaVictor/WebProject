FROM library/postgres
ENV POSTGRES_DB shop_db
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
COPY init/init.sql /docker-entrypoint-initdb.d/