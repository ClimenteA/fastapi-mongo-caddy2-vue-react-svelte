dev:
	docker-compose up --remove-orphans --force-recreate

db:
	docker-compose up --remove-orphans --force-recreate mongo_db_local


api:
	docker-compose up --remove-orphans --force-recreate fast_api_local