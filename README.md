# Cleveland Guardians Hiring Challenge

## Project Overview
This project is a web application that combines two main components:
1. A Flask-based web application for managing employee requests and departments
2. A Star Wars API integration for planet data collection and analysis

## Features

### Employee Management System
- View employee requests based on employee ID or department
- Admin access for viewing all requests
- Department-based filtering of requests
- JSON-based data storage for employees and requests

### Star Wars Planet Data Collection
- Automated data collection from SWAPI (Star Wars API)
- Data cleaning and validation
- CSV export functionality
- Pagination support for handling large datasets

## Technical Stack
- **Backend Framework**: Flask 2.2.5
- **Data Storage**: JSON files (Employees.json, Requests.json)
- **API Integration**: Requests library
- **Data Processing**: CSV handling
- **Scheduling**: Schedule library for automated tasks

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application
```bash
python app.py
```
The web application will be available at `http://localhost:5000`

### Running the Planet Data Collection
```bash
python cleguardians.py
```
This will fetch planet data from SWAPI and save it to `planets.csv`

## Project Structure
- `app.py`: Main Flask application
- `cleguardians.py`: Star Wars API integration
- `templates/`: HTML templates for the web interface
- `Employees.json`: Employee data storage
- `Requests.json`: Request data storage
- `requirements.txt`: Project dependencies

## Data Models

### Employee Data
Stored in `Employees.json` with fields:
- employee_id
- department
- isAdmin

### Request Data
Stored in `Requests.json` with fields:
- employee_id
- request details

### Planet Data
Exported to `planets.csv` with fields:
- Name
- Diameter
- Gravity
- Climate
- Population

## Contributing
Feel free to submit issues and enhancement requests.
