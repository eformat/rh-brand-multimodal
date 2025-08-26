# colbertv2.0

Train a [ColBERT](https://huggingface.co/colbert-ir/colbertv2.0) model to use as the index.

1. Python 3.9.23 (does not work with newer python)

    ```bash
    python3.9 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. You need a local GPU. I have a laptop NVIDIA GeForce RTX 4070. Train the index.

    ```bash
    python index.py
    ```

3. Run a test server using the index.

    ```bash
    python server.py
    ```

4. Test it out.

    ```bash
    curl -s "http://0.0.0.0/items?pageNumber=1" | jq .
    ```
