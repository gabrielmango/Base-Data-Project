# Base Data Project

![ETL Pipeline](https://img.shields.io/badge/process-ETL%20%2F%20ELT-blue)
![Python](https://img.shields.io/badge/python-3.11%2B-green)
![Poetry](https://img.shields.io/badge/dependency%20manager-poetry-orange)

Base Data Project is a robust foundation for building scalable ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) pipelines. This project template provides an enterprise-ready architecture with best practices for data engineering workflows, allowing you to focus on business logic rather than boilerplate setup.

## Key Features

- 🏗️ **Modular Architecture**: Clear separation of extraction, transformation, and loading components
- ⚙️ **Configuration Management**: Environment-based configuration with dotenv
- 📊 **Multi-source Support**: Ready for PostgreSQL, MongoDB, and web scraping with Selenium
- 🚦 **Robust Error Handling**: Centralized error management with detailed logging
- ⏱️ **Performance Monitoring**: Automatic execution time tracking
- 🧪 **Testing Framework**: Built-in structure for unit and integration tests
- 📓 **Jupyter Integration**: Notebook support for data exploration
- 📦 **Poetry Dependency Management**: Reproducible environments and dependency resolution

## Project Structure

```plaintext
base-data-project/
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── pyproject.toml              # Poetry dependencies and project metadata
├── poetry.lock                 # Locked dependency versions
├── README.md                   # Project documentation
├── src/                        # Main source code
│   ├── main.py                 # Application entry point
│   ├── core/                   # Core ETL components
│   │   ├── connections/        # Database connection handlers
│   │   │   ├── postgres_conn.py
│   │   │   ├── mongo_conn.py
│   │   │   └── selenium_conn.py
│   │   ├── extractors/         # Data extraction modules
│   │   ├── transformers/       # Data transformation modules
│   │   └── loaders/            # Data loading modules
│   ├── utils/                  # Utility functions
│   │   ├── config.py           # Configuration management
│   │   ├── logging.py          # Logging setup
│   │   └── error_handling.py   # Error handler decorator
│   └── pipelines/              # ETL/ELT pipeline implementations
│       ├── base_pipeline.py    # Abstract pipeline class
│       ├── sales_pipeline.py   # Example sales pipeline
│       └── user_pipeline.py    # Example user pipeline
├── tests/                      # Test suite
│   ├── test_etl.py             # ETL process tests
│   ├── test_extractors.py      # Extractor tests
│   └── test_utils.py           # Utility tests
└── notebooks/                  # Exploration notebooks
    ├── exploration.ipynb       # Data exploration
    └── debugging.ipynb         # Pipeline debugging
```

## Getting Started

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) package manager
- PostgreSQL (optional for database pipelines)
- MongoDB (optional for NoSQL pipelines)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gabrielmango/Base-Data-Project.git
   cd base-data-project
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. Copy environment template:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your specific configurations

### Running Pipelines

Execute the main application:
```bash
poetry run python src/main.py
```

To run a specific pipeline:
```python
# In src/main.py
from src.pipelines.sales_pipeline import SalesPipeline

if __name__ == "__main__":
    SalesPipeline().run()
```

### Creating a New Pipeline

1. Create a new file in `src/pipelines/` (e.g., `product_pipeline.py`)
2. Implement the pipeline by extending `BasePipeline`:
   ```python
   from src.pipelines.base_pipeline import BasePipeline
   from src.core.extractors import APIExtractor
   from src.core.transformers import ProductTransformer
   from src.core.loaders import PostgresLoader

   class ProductPipeline(BasePipeline):
       def __init__(self):
           super().__init__("ProductPipeline")
           self.extractor = APIExtractor()
           self.transformer = ProductTransformer()
           self.loader = PostgresLoader(table="products")
       
       def run(self):
           # Extraction
           raw_data = self.extract()
           
           # Transformation
           transformed_data = self.transform(raw_data)
           
           # Loading
           self.load(transformed_data)
   ```
3. Add it to `src/main.py` to execute

## Configuration Management

The configuration system uses environment variables loaded from `.env`:

```python
# src/utils/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # PostgreSQL Configuration
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "mydatabase")
    DB_USER = os.getenv("DB_USER", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    
    # MongoDB Configuration
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    
    # Selenium Configuration
    SELENIUM_HEADLESS = os.getenv("SELENIUM_HEADLESS", "True") == "True"
    
    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "etl.log")
```

## Error Handling

The project includes a robust error handler decorator:

```python
from src.utils.error_handling import ErrorHandler

error_handler = ErrorHandler("DataProcessor")

class DataProcessor:
    @error_handler
    def process_data(self):
        # Your data processing logic here
        ...
```

This provides:
- Automatic error logging with tracebacks
- Execution time tracking
- Consistent error reporting
- Process lifecycle monitoring

## Database Connections

### PostgreSQL Connection
```python
from src.core.connections.postgres_conn import PostgresConnection

# Get a database session
session = PostgresConnection().get_session()
result = session.execute("SELECT * FROM sales")
```

### MongoDB Connection
```python
from src.core.connections.mongo_conn import MongoDBConnection

# Access a database and collection
db = MongoDBConnection().get_database("analytics")
collection = db["user_events"]
documents = collection.find({"status": "active"})
```

### Selenium WebDriver
```python
from src.core.connections.selenium_conn import SeleniumConnection

# Launch a browser instance
driver = SeleniumConnection().get_driver()
driver.get("https://example.com/data-feed")
```

## Testing

Run tests with pytest:
```bash
poetry run pytest
```

Example test case:
```python
# tests/test_extractors.py
from src.core.extractors.web_extractor import WebExtractor

def test_web_extraction():
    extractor = WebExtractor()
    data = extractor.extract("https://example.com/api/data")
    assert data is not None
    assert "records" in data
```

## Notebook Integration

For exploratory data analysis:
```bash
poetry run jupyter notebook
```

Create a kernel for the project:
```bash
poetry run python -m ipykernel install --user --name=base-data-project
```

## Dependency Management

Add new dependencies with Poetry:
```bash
poetry add pandas numpy
```

Add development dependencies:
```bash
poetry add --group dev pytest pytest-mock
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Base Data Project** provides a solid foundation for building production-ready data pipelines. Its modular design allows for easy extension and adaptation to various data sources and processing requirements, while the built-in error handling and logging ensure reliability in production environments.