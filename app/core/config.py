from typing import Any, Dict, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, validator
import os


class Settings(BaseSettings):
    DB_USER: str = os.getenv('DB_USER', '')  
    print('DB_USER12==', DB_USER)
    DB_PASSWORD: str = os.getenv('DB_PASSWORD', '')  
    DB_HOST: str = os.getenv('DB_HOST', '')  
    DB_PORT: int = os.getenv('DB_PORT', '') 
    DB_NAME: str = os.getenv('DB_NAME', '')  
    
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",  
            username=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),  
            path=f"{values.get('DB_NAME')}", 
        ).unicode_string()
        
    model_config = SettingsConfigDict(env_file=".env",case_sensitive = True )

settings = Settings()
