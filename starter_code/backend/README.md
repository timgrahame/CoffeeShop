# Coffee Shop Backend

Coffee Shop is a web application that allows the management of a small drinks shop.

The application allows three levels of a user with different permissions for each.  These are:

	1. 	A general user - Can only view the drinks available. No login required
	2.	A Barista - Can view drinks available and view the ingredients.
	3. 	A Manager - Can view drinks available and view the ingredients.  Can also create, amend and delete drinks.
	
The application uses Auth0 to manage the authenticated users.

## Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration

- Authentication: Authentication is not required for a general user.  Baristas and Managers are authenticated by Auth0.

## Key Dependencies
	
	 - [PostgreSql] (https://www.postgresql.org/)  PostgreSQL is a powerful, open source object-relational database.
	
	 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

	 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

	 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 
	 
	 - [POSTMAN] http://www.postman.com) is used for testing the authentication processes from Auth0. 

### Installing Dependencies


	1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
	
	2. **PostgreSql** - Follow instrctions to install the latest version of PostgreSql at https://www.postgresql.org/download/.
	
	3. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). For Windows and Linux users, the process is as follows:

		 **Windows users in Bash**

		Ensure you're in the Backend folder in Bash and follow the following.

		``` bash
		Python -m venv venv
		source venv/scripts/activate
		```
		
		**Linux users in Bash**
		
		Ensure you're in the Backend folder in Bash and follow the following.
		``` bash
		Python -m venv venv
		source venv/bin/activate	
		```
	4. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
	
	```bash
	pip install -r requirements.txt
	```
	
	This will install all of the required packages included within the `requirements.txt` file.

## Database setup
	 
	5.	Start Postgres, in windows this is achieved by typing the following in a bash window:
		
		pg_ctl -d "C:\program files\postgresql\10\data" start  	substitute the number 10 for the version number of postgresql you have installed.
		
		Then using a bash window and with PostgreSql installed, create a new database by typing:
			
		```bash
		createdb drinks
		```
		
		within the api.py script there is a single line that needs commenting out before first run:
		```
		# Get Drinks-detail Endpoint
		```
		This will create the necessary tables and install a single record as a sample.  Once run, uncomment the line to prevent your database being erased.

		
## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
pg_ctl -D "c:\program files\postgresql\10\data" start
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Error handling

	8.	Errors will be returned in the following json format:
	
		```
		json
			  {
			   'success': False,
			   'error': 404,
			   'message': 'Resource not found, we searched everywhere'
			  }
		```
		
	9.	The error codes currently returned are:
	
	* 400 - Bad Request Error
	* 404 - Resource not Found Error
	* 500 - Internal Server Error
	* 422 - Unprocessable Error
	* AuthError - handled by Auth.py in the frontend to confirm if a user has correct permissions.
	
	11. Authentication processes were checked using Postman (https://www.postman.com) and a script that can be imported into Postman is made available in the backend directory labelled: udacity-fsnd-udaspicelatte.postman_collection.json
	
##	Endpoints

	10.	The following endpoints are used within the App:

	** GET / drinks
	-	General:
		Displays drinks available to the user
	
	** GET / drinks-detail
	-	General:
		Displays drinks to any authenticated user that has the 'get:drinks-detail permission' allocated to them via Auth0
		
	** POST /drinks
	-	General:
		Allows the adding of drinks by authenticated users with the permission 'post:drinks' allocated to them via Auth0
		
	** PATCH /Drinks/<int:id>
	-	General:
		Allows the amending of drinks by an authenticated user with the permission 'patch:drinks' allocated to them via Auth0
		
	** DELETE /Drinks/<int:id>
		General:
		Allows the deletion of drinks by an authenticated user with the permission 'delete:drinks' allocated to them via Auth0
	
	
### Setup Auth0

	11. Auth0 (https://auth0.com) is an external website that can provide for the management of users and permissions and was chosen as this Webapp's authentication method.  It has been set up using the following details:
	```
		AUTH0_DOMAIN = 'fsnd-tgrahame.eu.auth0.com'
		ALGORITHMS = ['RS256']
		API_AUDIENCE = 'coffee'
	```
## Authors
	- 	Udacity created the starter files for the project for the backend and the frontend.
	
	-	Tim Grahame worked the API and produced the full functionality. 