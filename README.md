# Job Portal - Django Project

A simple and elegant job portal built with Django where recruiters can post jobs and job seekers can browse available positions.

## Features

- **User Registration & Authentication**
  - Separate user types: Recruiters and Job Seekers
  - Secure login/logout functionality
  - Logout confirmation page

- **For Recruiters**
  - Post new job openings
  - View and manage posted jobs
  - Edit job details
  - Delete job postings

- **For Job Seekers**
  - Browse all active job listings
  - Search jobs by title, company, location, and job type
  - View detailed job descriptions
  - Filter by job type (Full Time, Part Time, Contract, Internship)

- **Modern UI**
  - Bootstrap 5 responsive design
  - Font Awesome icons
  - Clean and professional interface

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps to Run

1. **Navigate to the project directory**
   ```bash
   cd job-portal
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # OR
   venv\Scripts\activate  # On Windows
   ```

3. **The database is already set up**, but if you need to reset it:
   ```bash
   python manage.py migrate
   ```

4. **Load dummy data (optional but recommended)**
   ```bash
   python manage.py create_dummy_jobs
   ```
   This creates:
   - A demo recruiter account (username: `demo_recruiter`, password: `demo1234`)
   - 10 sample job postings across different categories

5. **Create a superuser (admin) account**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

   **Demo Account:**
   - Username: `demo_recruiter`
   - Password: `demo1234`
   - Type: Recruiter (can post jobs)

## Usage Guide

### For Recruiters

1. **Register an account**
   - Click "Register" in the navigation
   - Fill in your details
   - Select "Recruiter" as your user type
   - Optionally add your company name

2. **Post a job**
   - After logging in, click "Post Job" in the navigation
   - Fill in the job details:
     - Job Title
     - Company Name
     - Location
     - Job Type
     - Salary Range (optional)
     - Job Description
     - Requirements

3. **Manage your jobs**
   - Click "My Jobs" to see all your posted jobs
   - Edit or delete jobs as needed
   - View job details and applicant interest

### For Job Seekers

1. **Register an account**
   - Click "Register" in the navigation
   - Fill in your details
   - Select "Job Seeker" as your user type

2. **Browse jobs**
   - Visit the homepage to see all available jobs
   - Use the search filters to find specific jobs:
     - Search by job title or company name
     - Filter by location
     - Filter by job type

3. **View job details**
   - Click "View Details" on any job card
   - Read the full job description and requirements

## Project Structure

```
job-portal/
├── jobportal/          # Main project settings
│   ├── settings.py     # Django settings
│   └── urls.py         # Main URL configuration
├── jobs/               # Jobs application
│   ├── models.py       # Database models (UserProfile, Job)
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   ├── urls.py         # App URL patterns
│   ├── admin.py        # Admin configuration
│   └── templates/      # HTML templates
│       └── jobs/
│           ├── base.html
│           ├── home.html
│           ├── job_detail.html
│           ├── post_job.html
│           ├── my_jobs.html
│           ├── edit_job.html
│           ├── delete_job.html
│           ├── login.html
│           └── register.html
├── venv/               # Virtual environment
├── db.sqlite3          # SQLite database
└── manage.py           # Django management script
```

## Database Models

### UserProfile
- Links to Django's User model
- `user_type`: recruiter or job_seeker
- `company`: company name (optional)
- `phone`: phone number (optional)

### Job
- `recruiter`: Foreign key to User
- `title`: job title
- `company`: company name
- `location`: job location
- `job_type`: full_time, part_time, contract, or internship
- `description`: detailed job description
- `requirements`: job requirements
- `salary_range`: salary information (optional)
- `posted_date`: auto-generated timestamp
- `is_active`: boolean flag for active/inactive jobs

## Technologies Used

- **Backend**: Django 5.2.8
- **Frontend**: Bootstrap 5, Font Awesome 6
- **Database**: SQLite (default, easily switchable to PostgreSQL/MySQL)
- **Authentication**: Django's built-in authentication system

## Future Enhancements

- Job application system
- Resume upload functionality
- Email notifications
- Advanced search filters
- Company profiles
- Applicant tracking for recruiters
- Saved jobs for job seekers

## License

This is a simple educational project. Feel free to use and modify as needed.
