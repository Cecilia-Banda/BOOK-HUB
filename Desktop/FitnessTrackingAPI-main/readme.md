# Fitness Tracking API

This is a RESTful API for tracking workouts and exercises. The API allows users to create and manage workouts, add exercises to workouts, and track their progress over time.

## Installation

- Clone the repository to your local machine.
`git clone https://github.com/your-username/fitness-tracking-api.git`

- Set up the database.

`python manage.py makemigrations`

`python manage.py migrate`

- Create a superuser.

`python manage.py createsuperuser`

- Run the development server.

`python manage.py runserver`

- The API will be accessible at http://localhost:8000/ by default.

## Usage

### Authentication

To access the API endpoints, you need to authenticate using the token authentication method. You can obtain a token by sending a POST request to the `/api-token-auth/` endpoint with your username and password in the request body. The API will respond with a token that you can use to authenticate subsequent requests.

### Endpoints

#### Workouts

- `GET /workouts/`: Returns a list of all workouts.
- `POST /workouts/`: Creates a new workout.
- `GET /workouts/{id}/`: Returns the details of a specific workout.
- `PUT /workouts/{id}/`: Updates a specific workout.
- `DELETE /workouts/{id}/`: Deletes a specific workout.

#### Exercises

- `GET /exercises/`: Returns a list of all exercises.
- `POST /exercises/`: Creates a new exercise.
- `GET /exercises/{id}/`: Returns the details of a specific exercise.
- `PUT /exercises/{id}/`: Updates a specific exercise.
- `DELETE /exercises/{id}/`: Deletes a specific exercise.

## Acknowledgements

This API was developed using the Django REST Framework.