# api

1. Python 3.13.5

    ```bash
    python3.13 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Run the api server (requirement: needs the colbertv2.0 index to query)

    ```bash
    python server.py
    ```

3. Test it out.

    ```bash
    curl -s "http://0.0.0.0:5000/items?pageNumber=1" | jq .
    ```
