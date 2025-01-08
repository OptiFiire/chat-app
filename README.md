# Chat App

A real-time chat application built with Django, Vue.js, and Djoser for token-based authentication.

## Features

- **Real-time Messaging**: Engage in instant conversations with other users.
- **User Authentication**: Secure sign-up and login using Djoser token authentication.
- **User Profiles**: Personalize your profile with a unique username, display name, avatar, and biography.
- **Responsive Design**: Enjoy a seamless experience across various devices.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/OptiFiire/chat-app.git
   cd chat-app
   ```

2. **Backend Setup**:

   - *Navigate to the backend directory*:

     ```bash
     cd server
     ```

   - *Create a virtual environment and activate it*:

     ```bash
     python -m venv .venv
     source .venv/bin/activate  # On Windows: .venv\Scripts\activate
     ```

   - *Install dependencies*:

     ```bash
     pip install -r requirements.txt
     ```

   - *Apply migrations*:

     ```bash
     python manage.py migrate
     ```

   - *Create a superuser*:

     ```bash
     python manage.py createsuperuser
     ```

   - *Start the development server*:

     ```bash
     python manage.py runserver
     ```

3. **Frontend Setup**:

   - *Navigate to the frontend directory*:

     ```bash
     cd ../client
     ```

   - *Install dependencies*:

     ```bash
     npm install
     ```

   - *Start the development server*:

     ```bash
     npm run dev
     ```

## Usage

- **Access the Application**: Open your browser and navigate to `http://localhost:8000` for the backend and `http://localhost:5173` for the frontend.
- **Sign Up**: Create a new account using the sign-up page.
- **Log In**: Access your account using your credentials.
- **Chat**: Start real-time conversations with other users.

## API Endpoints

- **User Registration**: `POST /auth/users/`
- **User Login**: `POST /auth/token/login/`
- **User Details**: `GET /auth/users/me/`
- **Chat Messages**: `GET /api/messages/`

For detailed API documentation, refer to the [Djoser documentation](https://djoser.readthedocs.io/).