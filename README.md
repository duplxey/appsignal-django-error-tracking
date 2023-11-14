# Track Errors in Django with AppSignal

...

Read at: []()

## Development Setup

1. Create a new virtual environment and activate it:
   
    ```sh
    $ python -m venv venv && source venv/bin/activate
    ```

1. Install the dependencies:

    ```sh
    $ pip install -r requirements.txt
    ```
   
1. Create a *.env* file with the following contents:

    ```sh
    APPSIGNAL_PUSH_API_KEY=<your_push_api_key>
    ```
   
1. Migrate the database:

    ```sh
    $ python manage.py migrate
    ```
   
1. Run the development server:

    ```sh
    $ python manage.py runserver
    ```
   
1. Visit [http://localhost:8000/movies](http://localhost:8000/movies) in your favorite web browser.
