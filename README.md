# Flask MongoDB CRUD API

A scalable Flask application that provides REST API endpoints for CRUD operations on a User resource using MongoDB. (Made as an assignment for CoRider)

## Project Structure
```bash
sde-intern-assignment/
├── Dockerfile
├── README.md
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── services.py
├── docker-compose.yml
├── requirements.txt
├── run.py
└── .env.example
```

## Prerequisites
Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Postman (for API testing)](https://www.postman.com/downloads/)


## Installation

- Clone the Repository
```bash
git clone https://github.com/saatvik1512/sdeInternAssignement_coRider.git
cd sdeInternAssignement_coRider/
```
- Create a .env file in the project root:
```bash
cp .env.example .env
```
- Edit the .env file with your desired environment variables:
```bash
MONGO_URI=mongodb://localhost:27017/user_management
FLASK_ENV=development
```

## Running the Application

### Using Docker (Recommended)

- Start the application using Docker Compose
```bash
docker-compose up --build
```
- The application will be available at: http://localhost:5000

- MongoDB will be available at: mongodb://localhost:27017/user_management

### Without Docker (For Development)

- Install Dependencies
```bash
pip install -r requirements.txt
```
- Run the Application
```bash
flask run
```
- The application will be available at:http://localhost:5000

## Testing
### Create a user (POST /users)
```bash
http://localhost:5000/users
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

### Get All Users (GET /users):
```bash
http://localhost:5000/users
// Expected Response
[
  {
    "id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "name": "John Doe",
    "email": "john@example.com"
  }
]
```

### Get a Specific User (GET /users/<id>):
```bash
http://localhost:5000/users/a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8
// Expected Response
{
  "id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Update a User (PUT /users/<id>):
```bash
http://localhost:5000/users/a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}

// Expected Response
{
  "id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

### Delete a User (DELETE /users/<id>):
```bash
http://localhost:5000/users/a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8
// Expected Response
{
  "message": "User deleted successfully"
}
```
## Additional
Built as a Cargo Pro Assignment