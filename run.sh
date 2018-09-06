docker-compose up -d
docker-compose exec openid-rp1 ./manage.py migrate
docker-compose exec openid-rp2 ./manage.py migrate
docker-compose exec openid-op ./manage.py migrate
docker-compose exec openid-op ./manage.py loaddata ./op/fixtures/initial_data.json
docker-compose exec openid-op ./manage.py creatersakey
docker-compose exec openid-op ./manage.py createsuperuser
