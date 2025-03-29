#!/bin/bash
pip install torch --index-url https://download.pytorch.org/whl/cpu/
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 10000
