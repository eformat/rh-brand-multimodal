# rh-brand-multimodal

Welcome to the RedHat Icon Finder App. Search using natural language for you the icon you need.

## data prep

Try out various MaaS VL models (Qwen2.5-VL-7B-Instruct-FP8-Dynamic, Granite-Vision-3.2, Llama-4-Scout-17B-16E-W4A16) using brand icon images to generate textual representation.

Output to jsonl.

## colbertv2.0 model index

[ColBERT](https://huggingface.co/colbert-ir/colbertv2.0) is a fast and accurate retrieval model, enabling scalable BERT-based search over large text collections in tens of milliseconds.

Train a colbert model used for search using the jsonl as input.

## api

Python API for serving up data to the UI.

## ui

An IMDB Movie search UX Clone using next.js, react, tailwind. Modified to work with icons 🙈

![images/icon-finder.png](images/icon-finder.png)
