**README**

This project is a FastAPI application for managing student records stored in a MongoDB database. It provides CRUD (Create, Read, Update, Delete) operations for student entities through a RESTful API. The application uses Pydantic for data validation and serialization, pymongo for MongoDB interaction, and FastAPI for handling HTTP requests.

### Setup

1. **Dependencies Installation:**
   Make sure you have Python installed. Then, install the required Python packages by running:
   ```
   pip install fastapi pymongo uvicorn
   ```

2. **MongoDB Configuration:**
   Ensure you have a MongoDB instance running. Replace `"your mongo url"` in the `MongoClient` instantiation with your MongoDB connection URL.

3. **Run the Application:**
   Execute the following command in your terminal to start the FastAPI application:
   ```
   uvicorn main:app --reload
   ```
   This command runs the application using the Uvicorn ASGI server.

### Endpoints

- **POST /students/**
  - Creates a new student record.
  - Request Body: JSON object representing a student entity.
  - Response Body: JSON object containing the ID of the newly created student.
  - Status Code: 201 Created

- **GET /students/**
  - Retrieves a list of student records based on optional query parameters.
  - Query Parameters:
    - `country`: Filter students by country.
    - `age`: Filter students by age.
  - Response Body: JSON array containing student records.
  - Status Code: 200 OK

- **GET /students/{student_id}**
  - Retrieves a specific student record by ID.
  - Path Parameter: `student_id`: ID of the student to retrieve.
  - Response Body: JSON object representing the student.
  - Status Code: 200 OK

- **PATCH /students/{student_id}**
  - Updates an existing student record.
  - Path Parameter: `student_id`: ID of the student to update.
  - Request Body: JSON object representing the updated student entity.
  - Status Code: 204 No Content

- **DELETE /students/{student_id}**
  - Deletes an existing student record.
  - Path Parameter: `student_id`: ID of the student to delete.
  - Status Code: 200 OK

### Testing the Endpoints

You can test the endpoints using tools like curl, Postman, or writing unit tests using Python testing frameworks like pytest. Below are some examples of how to test the endpoints using curl:

1. **Create a Student:**
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 20, "address": {"city": "New York", "country": "USA"}}' http://localhost:8000/students/
   ```

2. **List Students:**
   ```
   curl -X GET http://localhost:8000/students/
   ```

3. **Get a Student by ID:**
   ```
   curl -X GET http://localhost:8000/students/{student_id}
   ```

4. **Update a Student:**
   ```
   curl -X PATCH -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 21, "address": {"city": "New York", "country": "USA"}}' http://localhost:8000/students/{student_id}
   ```

5. **Delete a Student:**
   ```
   curl -X DELETE http://localhost:8000/students/{student_id}
   ```

Replace `{student_id}` with the actual ID of the student you want to interact with.

### Unit Testing

To write unit tests for the endpoints, you can use the `pytest` framework. Create test files for each endpoint and use `pytest` to run the tests. Ensure to mock the database operations for testing purposes.

### Note

- Ensure that the MongoDB instance is running and accessible.
- Handle authentication and authorization if required for your application.
- Ensure input validation and error handling for robustness.
