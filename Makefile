install:
	pip install -r requirements.txt
test-extract:
	python -m pytest tests/test_extract.py