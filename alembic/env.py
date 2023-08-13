from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Add the project path to the Python path
import os
import sys
sys.path.append("C:/vs-code-projects/fastapi_twoDB")

# Import your metadata objects and models
from app.models import main_metadata, cache_metadata

# ... (other imports and code) ...

# Set up the Alembic Config object
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Define the engines as in your database.py file
from app.database import engine as main_engine, cache_engine

# Create a dictionary of the engines
engines = {
    'engine': main_engine,
    'cache_engine': cache_engine,
}

def run_migrations_online():
    for name, engine in engines.items():
        with engine.connect() as connection:
            if name == 'engine':
                target_metadata = main_metadata
            elif name == 'cache_engine':
                target_metadata = cache_metadata

            with context.begin_transaction():
                context.configure(
                    connection=connection,
                    target_metadata=target_metadata
                )
                with context.begin_transaction():
                    context.run_migrations(engine_name=name)

# ... (rest of your code) ...
