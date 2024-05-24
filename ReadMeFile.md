ReadMe File

Setup Instructions:

1. Clone the Repository:
   Clone your project repository containing the FastAPI application (`main.py`), database models (`models.py`), and other necessary files.

2. Install Dependencies:
   Navigate to the project directory and install the required dependencies using pip. Create a virtual environment first.

3. Set Up the Database:
   Make sure PostgreSQL database server is running. If not, start it.

4. Create Tables in the Database:
   Run the `create_db.py` script to create the necessary tables in PostgreSQL database.

Running the FastAPI Application:

1. Run the FastAPI Application:
   Start the FastAPI application using `uvicorn`. Make sure to specify the module containing the FastAPI `app` object (in this case, it's `main`) and use the `--reload` option for automatic reloading on code changes.

   uvicorn main:app --reload

2. Accessing the API:
   Once the FastAPI application runs, you can access the API endpoints using a web browser or Postman. By default, the API will be available at `http://127.0.0.1:8000`.

Running the Tests:

1. Prepare the Test Environment:
   Ensure that your test database is set up and clean.

2. Run the Tests:
   Use pytest to run the test cases defined in `test_main.py`. Ensure FastAPI application runs in the background while executing the tests.

   pytest
  

   This command will search for test files in the current directory and subdirectories and execute their test functions.

By following these setup and run instructions, you should be able to set up, run, and test FastAPI project successfully.