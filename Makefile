.PHONY: init capture pdf

init:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

capture:
	.venv/bin/python3 screenshot_clicker.py

pdf:
	.venv/bin/python3 make_pdf.py
