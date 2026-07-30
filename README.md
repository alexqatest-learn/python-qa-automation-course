# Python QA Automation Course Project

This repository contains an Automated Testing Framework built with **Python**, **Pytest**, **Requests**, and **Playwright**.

## 🛠 Project Structure

- `tests/api/`: API automation tests (GET, POST, PUT, DELETE) using `requests`.
- `tests/ui/`: UI automation tests using `pytest-playwright`.
- `conftest.py`: Shared Pytest fixtures (headers, tokens, setup & teardown logic).
- `requirements.txt`: Project dependencies.

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python 3.10+ installed.

### 2. Installation
Clone the repository and install the dependencies:

```bash
git clone [https://github.com/alexqatest-learn/python-qa-automation-course.git](https://github.com/alexqatest-learn/python-qa-automation-course.git)
cd python-qa-automation-course
pip install -r requirements.txt
playwright install