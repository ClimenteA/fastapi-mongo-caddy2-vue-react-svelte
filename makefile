dev:
	docker-compose up --remove-orphans --force-recreate

db:
	docker-compose up --remove-orphans --force-recreate mongo_db_local

api:
	docker-compose up --remove-orphans --force-recreate fast_api_local

prod:
	docker-compose -f docker-compose.prod.yml up --remove-orphans --force-recreate 

caddy2:
	docker-compose -f docker-compose.prod.yml up --remove-orphans --force-recreate caddy_prod
