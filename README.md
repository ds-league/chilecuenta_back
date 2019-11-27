# APP ChileCuenta ![https://travis-ci.com/ds-league/chilecuenta.svg?branch=master](https://travis-ci.com/ds-league/chilecuenta.svg?branch=master)

## Requirments: 
- docker 
- ![docker-compose](https://docs.docker.com/compose/install/)

## First execution instructions
1. Clone the repository: ```git clone https://github.com/ds-league/chilecuenta.git```
2. Enter the root folder: ```cd chilecuenta```
3. Build the docker image: ```docker build .```
4. Create an image by using docker-compose especifications: ```docker-compose build```

## Run commands 
- create the app (this is not necessary because we already have the application created): ```docker-compose run app sh -c "django-admin.py startproject app ."```
- up the app: ```docker-compose up```
