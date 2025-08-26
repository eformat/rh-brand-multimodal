# data prep

1. Python 3.13.5

    ```bash
    python3.13 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Download the Brand icons to a folder.

3. Export MaaS env vars

    ```bash
    export LLM_URL=https://qwen25-vl-7b-instruct-maas-apicast-production.apps.prod.<cluster domain>:443/v1
    export API_KEY=5e...
    export LLM_MODEL=openai/RedHatAI/Qwen2.5-VL-7B-Instruct-FP8-Dynamic
    ```

4. Use [DSPy](https://dspy.ai/) to generate jsonl file.

    ```bash
    python qwen-qa3.py
    ```
