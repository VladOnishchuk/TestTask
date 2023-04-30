## Setup 

1. Clone the repository:
    ```sh
    $ git clone git@github.com:VladOnishchuk/TestTask.git
    ```
2. Populate env.example and end.db.example files and rename it on .env and .env.db
3. Build and run containers by command:
    ```sh
    $ make build 
    ```
## To get started
By url http://0.0.0.0:8000/swagger/ there is swagger doc.

You have to create new user by /auth/users/ endpoint and then create jwt token for it by /auth/jwt/create/ endpoint.
After got response from /auth/jwt/create/ copied access token and open Postman.
In the tab Authorization choose type "Bearer Token" and paste access token from API.
Now you have access for endpoints.
