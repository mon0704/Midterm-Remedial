
# Blood Donation Project

## Overview

The Blood Donation Project is a Django-based web application that serves as a hub for individuals who are seeking blood donors in emergencies and for people who wish to donate blood. The project features three main apps:

1. **Account**: User registration, login, and profile management.
2. **Blood**: Blood donation requests and listings.
3. **Admin**: Administrative dashboard for managing users and requests.

The project uses Bootstrap for styling, with Django template inheritance to manage layout consistency. Users are authenticated and have profiles with detailed information for blood donation.

## Features

### 1. User Registration & Profile Creation
- Users register using a custom user model with fields like email, password, etc.
- After registration, users are required to complete their profile (e.g., first name, last name, weight, height, blood type, region, etc.).
- The profile information is linked, with JavaScript dynamically loading provinces and municipalities based on the region selected.

### 2. User Login
- Before logging in, the system checks if the user has a completed profile.
- If the profile is incomplete, users are redirected to a form to fill in the missing details.

### 3. Profile Page
- Users can view and update their profiles, except for the blood type field.
- The system checks the user’s last blood donation date. Users must wait 56 days between donations, and an error is shown if they try to change their availability prematurely.

### 4. Blood Donation Requests
- Users can create, view, update, and delete blood donation requests.
- Depending on whether the user is donating or looking for blood, fields are either auto-filled from the profile or need to be entered manually.
- A list and detailed view of all blood donation requests is available, with filtering by location and blood type.

### 5. Admin Dashboard
- The admin dashboard allows authorized administrators to manage users and blood donation requests.
- Admins can create, edit, and delete all requests and user accounts.

## Installation

1. Clone the repository:
   \`\`\`bash
   git clone <repository-url>
   cd blood-donation-project
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Run database migrations:
   \`\`\`bash
   python manage.py migrate
   \`\`\`

4. Create a superuser (admin):
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

5. Run the development server:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

6. Access the application at \`http://127.0.0.1:8000\`.

## Technologies Used

- **Django**: Backend web framework for Python.
- **Bootstrap**: Frontend styling framework.
- **SQLite**: Default database (can be replaced with PostgreSQL/MySQL if needed).
- **JavaScript**: For dynamic form handling (region/province/municipality linking).

## How to Use

### User Functions
- Register as a user and complete your profile.
- Create a blood donation request by choosing whether you're donating or looking for blood.
- Update your availability to donate after the required waiting period.

### Admin Functions
- Manage users and blood donation requests via the Admin Dashboard.

## License

Hello sir eto po yung remedial quiz ko :)
