# FastAPI with Asynchronous SQLAlchemy  
A modern FastAPI application showcasing seamless integration with Asynchronous SQLAlchemy, enabling efficient CRUD operations with PostgreSQL.  

## Features
- 🚀 FastAPI for high-performance API development
- 🐘 Async SQLAlchemy for database operations
- 🗄️ PostgreSQL database support
- 📄 Alembic for database migrations
- 🛠️ Pydantic for data validation and serialization
- 🧩 Modular architecture with clear separation of concerns

## Getting Started  
### Clone the Repository  
To get started, clone the repository to your local machine:  
```bash
git clone https://github.com/Khailas12/FastAPI-with-Asynchronous-SQLAlchemy.git
cd FastAPI-with-Asynchronous-SQLAlchemy
```  
## Project Structure
```
├── app/                     # Main application directory
│ ├── alembic/               # Database migration scripts
│ ├── core/                  # Core configurations
│ ├── db/                    # Database models and session management
│ ├── services/              # Business logic and API endpoints
│ ├── utils/                 # Utility functions
│ ├── alembic.ini            # Alembic configuration
│ ├── main.py                # Application entry point
│ └── __init__.py            # Package initialization
├── .env                     # Environment variables
└── README.md                # Project documentation
```

## Setup
1. **Install Dependencies**  
   Install the required Python packages:  
   ```bash
   pip install -r requirements.txt
   ```  

2. **Create the PostgreSQL Database**  
   Before running the application, ensure the database is created. You can do this using:  

   - **Command Line (psql)**:  
     ```bash
     psql -U your_db_user -h your_db_host -p 5432 -c "CREATE DATABASE your_db_name;"
     ```  
     Replace `your_db_user`, `your_db_host`, and `your_db_name` with your actual credentials.  

   - **DBeaver**:  
     1. Open DBeaver and connect to your PostgreSQL server.  
     2. Right-click on "Databases" in the navigation tree.  
     3. Select "Create New Database".  
     4. Enter the database name (e.g., `fastapi_db`) and click "OK".  

   - **pgAdmin**:  
     1. Open pgAdmin and connect to your PostgreSQL server.  
     2. Expand the "Databases" node in the browser tree.  
     3. Right-click on "Databases" and select "Create > Database".  
     4. Enter the database name (e.g., `fastapi_db`) and click "Save".  

3. **Verify Database Connection**  
   Ensure the database is accessible using:  

   - **Command Line (psql)**:  
     ```bash
     psql -U your_db_user -h your_db_host -p 5432 -d your_db_name
     ```  
     If successful, you’ll be able to interact with the database directly.  

   - **DBeaver**:  
     1. Open DBeaver and connect to your PostgreSQL server.  
     2. Expand the "Databases" node and verify the new database appears.  
     3. Test the connection by running a simple query (e.g., `SELECT 1;`).  

   - **pgAdmin**:  
     1. Open pgAdmin and connect to your PostgreSQL server.  
     2. Expand the "Databases" node and verify the new database appears.  
     3. Open the Query Tool and run a simple query (e.g., `SELECT 1;`) to test the connection.  

4. **Environment Variables**  
   Create a `.env` file with the following variables to configure your PostgreSQL database connection:  
   ```env
   DB_USER=your_db_user          # PostgreSQL username (e.g., "postgres")
   DB_PASSWORD=your_db_password  # PostgreSQL password
   DB_HOST=your_db_host          # Database host (e.g., "localhost" or "127.0.0.1")
   DB_PORT=5432                  # Default PostgreSQL port
   DB_NAME=your_db_name          # Database name (e.g., "fastapi_db")
   ```

3. **Database Migrations**
   ```bash
   alembic upgrade head
   ```

4. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

## Database Migrations with Alembic
### Initializing Alembic
To initialize Alembic in your project, run:
```bash
alembic init alembic
```

This creates the following structure:
```
alembic/
├── env.py
├── script.py.mako
└── versions/
alembic.ini
```

### Configuration
1. **alembic.ini** - Main configuration file
   - Update `sqlalchemy.url` to use your database connection string
   - Configure other settings like logging and migration paths

2. **env.py** - Migration environment script
   - Set up your SQLAlchemy models and database connection
   - Configure the target metadata for migrations

### Creating Migrations
To create a new migration:
```bash
alembic revision --autogenerate -m "description of changes"
```

This will:
1. Compare your models with the current database state
2. Generate a migration script in the `versions/` directory
3. Include the necessary SQL operations to update the schema

### Applying Migrations
To apply pending migrations:
```bash
alembic upgrade head
```

### Common Commands
- **Check current revision**: `alembic current`
- **Upgrade to specific revision**: `alembic upgrade <revision>`
- **Downgrade migrations**: `alembic downgrade <revision>`
- **Show migration history**: `alembic history`
- **Create empty migration**: `alembic revision -m "description"`


### Best Practices
1. Always review auto-generated migrations before applying them
2. Test migrations in a development environment before production
3. Use descriptive migration messages
4. Keep migrations small and focused
5. Never modify migrations after they've been applied to production


## CRUD API Endpoints
### Items
- `POST /items/` - Create a new item
- `GET /items/{item_id}` - Get item details
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete an item


## Technologies Used
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [Uvicorn](https://www.uvicorn.org/)


## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeatureName`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeatureName`)
5. Open a pull request

## License
MIT License