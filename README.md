# FastAPI Student Management API

A simple and educational REST API built with FastAPI, designed to manage student records stored in an Excel file.
This project was created to help me understand the core concepts of modern API development using FastAPI, including routing, data processing, dependency handling, and API design principles.

## 🚀 Project Overview
This API simulates a student management system and uses an Excel file (students.xlsx) as a lightweight data source instead of a traditional database.
The API supports:
	- Retrieving all students
	- Fetching a student by ID
	- Filtering students by department
	- Getting top-performing students
	- Returning student statistics
	- Automatically generating the Excel file if it does not exist
Everything is returned in structured JSON format, making the API easy to consume from any frontend or automation script.

## 🎯 What I Learned From This Project
Through building this API, I gained hands-on experience with:
**✔️ FastAPI Fundamentals**
	- Creating routes and HTTP endpoints
	- Understanding request/response models
	- Using automatic documentation (/docs and /redoc)
**✔️ Data Handling with Pandas**
	- Reading and writing Excel files
	- Filtering, sorting, and aggregating tabular data
	- Converting DataFrames to JSON-compatible structures
**✔️ API Architecture Concepts**
	- Structuring a backend service
	- Implementing CORS configuration
	- Separating logic into clear functional steps
**✔️ Backend Development Skills**
	- Error handling
	- Returning status codes
	- Understanding how a web server (uvicorn) operates
	- Making a Python script behave like a real backend service
This project was a valuable step toward learning how real-world APIs are designed and how backend systems interact with data sources.
