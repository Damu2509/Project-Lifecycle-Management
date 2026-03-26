.PHONY: install run dev clean

install:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run:
	. venv/bin/activate && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

dev:
	. venv/bin/activate && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
	rm -rf venv
