build:
	docker-compose build

run:
	docker-compose up

rund:
	docker-compose up -d

br:
	docker-compose up -d --build

deploy:
	cd frontend
	npm install
	cd ..
	docker volume prune -f
	docker-compose up -d --build
