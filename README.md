# Cinema
# About project
## Models
   
   - CustomUser 
     - Default django UserModel fields 
     - age
   - Halls
     - title
     - slug (depends on the title, generate automatically) 
     - rows
     - columns
   - Genres
     - title
   - Actors
     - name
   - Producers
     - name 
   - Movies 
     - title 
     - slug (depends on the title, generate automatically)
     - poster (Image)
     - description
     - year
     - description
     - duration
     - genres (ManyToManyField with Genres)
     - actors (ManyToManyField with Actors)
     - producer (ManyToManyField with Producers)
     - age_rating 
     - in_rental
   - Sessions
     - movie (ForeignKey to Movie)
     - hall (ForeignKey to Hall)
     - date
     - start_at
     - end_at
     - ticket_price
     - is_active
   - Tickets
     - session (ForeignKey to Sessions)
     - owner (ForeignKey to CustomUser)
     - column 
     - row
     - sold
     - ticket_price
     - is_active
## Urls
   - Home page
     - / - Home page
   - Users
     - users/{id}/ - User detail 
   - Halls
     - halls/ - Halls list
   - Sessions
     - sessions/ - Sessions list
     - sessions/{id}/ - Session dy id
     - sessions/search/ - Page for search session by params
     - sessions/{movie_slug}/ - Sessions by movie slug
     - sessions/{session_id}/buy/ticket/ - Page for buy ticket
   - Movies
     - movies/ - All movies in rental list
     - movies/{slug} - Movie by slug
   - API 
     - swagger/ - Swagger documentation for API 
## Setup 

1. Clone the repository:
    ```sh
    $ mkdir app
    $ cd app 
    $ git clone https://github.com/gocardless/sample-django-app.git
    ```
2. Up docker container
    ```sh
   $ docker-compose build
   $ docker-compose up
   ```
3. Create superuser form admin app:
    
    !!! In new terminal 
    ```sh
   $ docker ps
   $ docker exec -it {contaienr_id}  python manage.py createsuperuser
   ```
Now Your can to search site
