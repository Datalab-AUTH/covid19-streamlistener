## covid19-streamlistener

This is a python script that listens for new tweets for certain hashtags
and adds them to a mongodb instance.

## Requirements

A Python 3.x installation is needed, with additional modules listed in
`requirements.txt`. Install everything needed with:

```
pip install -r requirements.txt
```

## Execution

You have to set a few envirnment variables to run this. These include:

* `MONGOURL`: A URL pointing to your MongoDB installation, including
	username, password, port and database. Example:
	"mongodb://user:pass@servername:port/dbname"
* `MONGODB`: The database you want to access. Example: "dbname"
* `MONGOCOLLECTION`: The collection within the database. Example: "mycollection"
* `CONSUMER_KEY`: Twitter consumer key
* `CONSUMER_SECRET`: Twitter consumer secret
* `ACCESS_KEY`: Twitter access key
* `ACCESS_SECRET`: Twitter access secret


## Deployment

Deployment is done using Docker. There is a docker image at
`datalabauth/covid19-streamlistener`.
```
export MONGOURL="mongodb://user:pass@servername:port/dbname"
export MONGODB="dbname"
export MONGOCOLLECTION="mycollection"
export CONSUMER_KEY="myconsumerkey"
export CONSUMER_SECRET="myconsumersecret"
export ACCESS_KEY="myaccesskey"
export ACCESS_SECRET="myaccesssecret"
docker run \
	-e MONGOURL \
	-e MONGODB \
	-e MONGOCOLLECTION \
	-e CONSUMER_KEY \
	-e CONSUMER_SECRET \
	-e ACCESS_KEY \
	-e ACCESS_SECRET \
	datalabauth/covid19-streamlistener
```

This will run the python script within the docker container.

