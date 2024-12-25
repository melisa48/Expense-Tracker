# Expense Tracker

## Description
Expense Tracker is a web application designed to help users track their personal expenses. It allows users to add, view, and delete expenses while categorizing them for better financial management. The application also provides a visual representation of expenses through simple charts.

## Features
- Add new expenses with details such as amount, category, and description.
- View a list of all expenses in a tabular format.
- Delete expenses that are no longer needed.
- Visualize expenses by category with a simple bar chart.
- Built with Flask for the backend and SQLite for data storage.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Flask
- **Database**: SQLite
- **Libraries**: Flask-SQLAlchemy for ORM

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip (Python package installer)

### Steps to Install
1. Clone the repository:
- git clone <repository-url>
- cd expense_tracker


2. Create a virtual environment (optional but recommended):
- python -m venv venv
- source venv/bin/activate # On Windows use venv\Scripts\activate


3. Install the required packages:
- pip install flask flask-sqlalchemy

4. Initialize the database:
- python app.py


## Usage
1. Run the application:
- python app.py

2. Open your web browser and go to `http://localhost:5000`.

3. Use the interface to add new expenses, view existing ones, and delete any that are no longer needed.


 
## Contributing
- Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## Acknowledgments
- Thanks to Flask and SQLAlchemy for providing an easy-to-use framework for web development.
