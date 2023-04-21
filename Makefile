install:
	pip install -r requirements.txt
extract:
	python src/etl/extract.py
test-extract:
	python -m pytest tests/test_extract.py
transform:
	python src/etl/transform.py
test-transform:
	python -m pytest tests/test_transform.py