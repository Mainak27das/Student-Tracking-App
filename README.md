# Student Tracking App (for tuition center)
## Description
A simple and powerful student management system designed for a tuition center. This application allows for efficient batch management, student tracking, and profile management.

## Features
- Add and manage students
- Create and manage batches
- Track payment status
- View detailed student profiles
- Responsive and user-friendly interface

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd project-name
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply the migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000` in your web browser.
- Log in as an admin to manage batches, students, and other entities.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Open a Pull Request

## Built With
Django - The web framework used.


