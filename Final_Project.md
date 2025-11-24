# Final Project: Building a Full-Stack Application with FARM Stack

## Project Overview

In this final project, you will apply the skills you have learned throughout the course by building a full-stack web application using the FARM stack (FastAPI, React, and MongoDB). The application will be a used car sales platform where users can display, create, and manage car advertisements.

## Objectives

1. **Create a Backend with FastAPI**: Build a RESTful API that supports CRUD operations for managing car listings, user authentication, and image uploads.
2. **Set Up MongoDB**: Use MongoDB to store car listings and user information.
3. **Develop a Frontend with React**: Create a dynamic frontend that interacts with the backend API, using React Router for navigation and forms for user input.
4. **Implement User Authentication**: Secure your application by adding user registration and login functionality that utilizes JSON Web Tokens (JWT).
5. **Deploy the Application**: Deploy your frontend and backend to suitable hosting services (e.g., Netlify for the frontend, Render.com for the backend).

## Project Steps

### Step 1: Backend Development

1. **Set Up FastAPI**:
   - Initialize your FastAPI project.
   - Create a virtual environment and install necessary packages, including FastAPI, uvicorn, and Pydantic.

2. **Define Pydantic Models**:
   - Create models for the user and car data that handle validation and serialization.

3. **Create API Endpoints**:
   - Implement CRUD endpoints for car listings:
     - `GET /cars` - Retrieve all car listings.
     - `POST /cars` - Create a new car listing.
     - `GET /cars/{id}` - Retrieve a specific car listing.
     - `PUT /cars/{id}` - Update a car listing.
     - `DELETE /cars/{id}` - Delete a car listing.
   - Implement authentication endpoints:
     - `POST /register` - Register a new user.
     - `POST /login` - User login and JWT generation.

4. **Integrate MongoDB**:
   - Connect your FastAPI application to a MongoDB instance (Atlas or local).
   - Use Beanie or PyMongo to perform database operations.

### Step 2: Frontend Development

1. **Set Up React Application**:
   - Create a new Vite React application.
   - Install Tailwind CSS for styling.

2. **Implement Routing**:
   - Use React Router to set up different routes in your application (Home, Login, Register, Cars, etc.).

3. **Create Components**:
   - Develop the following components:
     - `Home`: A landing page to showcase available car listings.
     - `Login`: A form for users to log in.
     - `Register`: A form for new users to create an account.
     - `CarListing`: Displays individual car listings.
     - `NewCar`: A form to create a new car listing.

4. **Manage State and Data**:
   - Use the Context API to handle user sessions and authentication state.
   - Implement data fetching from the FastAPI backend using `fetch` or `axios`.

### Step 3: Authentication

1. **Implement JWT Authentication**:
   - On the backend, create functions to handle JWT encoding and decoding.
   - On the frontend, manage authentication state and store JWT in local storage or cookies.

2. **Protect Routes**:
   - Use a higher-order component (HOC) or a context provider to protect routes that require authentication.

### Step 4: Deployment

1. **Deploy Backend**:
   - Deploy the FastAPI application to Render.com or a similar service.
   - Ensure that your environment variables (e.g., MongoDB connection string) are set.

2. **Deploy Frontend**:
   - Deploy the React application to Netlify.
   - Perform any necessary configurations for CORS to allow communication between the frontend and backend.

## Deliverables

- A fully functional application following the FARM stack architecture.
- Source code hosted on a version control platform such as GitHub.
- A deployment URL for both the frontend and backend.
- Documentation explaining your project structure, how to run it locally, and any API endpoints.

## Conclusion

This project aims to consolidate your learning experience by applying theoretical knowledge to a tangible product. Make sure to test each component thoroughly and think critically about the technologies you use. Good luck, and have fun building your application!