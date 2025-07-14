# Base Data Project

![ETL Pipeline](https://img.shields.io/badge/process-ETL%20%2F%20ELT-blue)
![Python](https://img.shields.io/badge/python-3.11%2B-green)
![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-orange)

**Base Data Project** is a robust foundation for building scalable ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) pipelines. This project template provides an enterprise-ready architecture with best practices for data engineering workflows, allowing you to focus on business logic rather than boilerplate setup.

---

## 🔑 Key Features

- 🏗️ **Modular Architecture**: Clear separation of extractors, transformers, and loaders
- 🧩 **Abstract Base Classes**: Unified base interfaces for pipeline components
- ⚙️ **Config Management**: `.env`-based configuration using `dotenv`
- 🗃️ **Multi-source Support**: Ready for PostgreSQL, MongoDB, APIs, and more
- 📋 **Centralized Logging**: Structured logging with rotating file support
- 🚦 **Robust Error Handling**: Decorator-based error logging with context
- ⏱️ **Performance Monitoring**: Automatic execution timing per function
- 🧪 **Testing Support**: Easy-to-extend test structure for core modules
- 📦 **Poetry-based**: Reproducible builds and isolated environments

---

## 📁 Project Structure

```plaintext
base-data-project/
├── .env.example                 # Environment template
├── .gitignore                  # Git ignore rules
├── pyproject.toml              # Poetry dependencies and project metadata
├── poetry.lock                 # Locked dependency versions
├── README.md                   # Project documentation
├── src/                        # Main source code
│   ├── main.py                 # Entry point
│   ├── core/                   # Core ETL logic
│   │   ├── connections/        # Database integrations
│   │   │   ├── mongo_connection.py
│   │   │   └── postgres_connection.py
│   │   ├── extractors/         # Base extractor classes
│   │   │   └── base_extractor.py
│   │   ├── transformers/       # Base transformer classes
│   │   │   └── base_transformer.py
│   │   ├── loaders/            # Base loader classes
│   │   │   └── base_loader.py
│   ├── pipelines/              # Custom pipeline implementations
│   │   └── base_pipeline.py    # Abstract pipeline class
│   ├── utils/
│   │   ├── base/               # Common base classes
│   │   │   └── base_component.py
│   │   ├── config/             # Configuration logic
│   │   │   └── base_config.py
│   │   ├── error_handling.py   # Error handler
│   │   └── logging.py          # Logging configuration
├── tests/                      # Unit tests
│   └── test_etl.py             # Test samples
````

---

## 🚀 Getting Started

### Prerequisites

* Python 3.11+
* [Poetry](https://python-poetry.org/)
* PostgreSQL and/or MongoDB (if applicable)

### Installation

```bash
# Clone the repository
git clone https://github.com/gabrielmango/Base-Data-Project.git
cd base-data-project

# Install dependencies
poetry install

# Activate environment
poetry shell

# Create your .env
cp .env.example .env
```

Then, edit `.env` to set your DB credentials, API keys, and configurations.

---

## 📦 Dependency Management

Install a new package:

```bash
poetry add pandas numpy
```

Install development dependencies:

```bash
poetry add --group dev pytest pytest-mock
```

---

## 🧪 Running Tests

```bash
poetry run pytest
```

Or with coverage:

```bash
poetry run pytest --cov=src
```

---

## 📌 Pipeline Execution

You can create custom pipelines by subclassing `BasePipeline` and calling `.execute()`:

```python
from src.pipelines.my_pipeline import MyPipeline

pipeline = MyPipeline()
pipeline.execute()
```

All logs and errors will be recorded and timestamped under `/logs/YYYY_MM_DD/`.

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push the branch: `git push origin feature/my-feature`
5. Open a pull request

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---
