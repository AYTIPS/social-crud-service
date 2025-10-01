#from pydantic import BaseSettings
from pydantic_settings import BaseSettings
from pydantic import Field 

class Settings(BaseSettings):
    database_hostname: str = Field(..., env=("database_hostname", "DATABASE_HOSTNAME"))
    database_port: str      = Field(..., env=("database_port", "DATABASE_PORT"))
    database_password: str  = Field(..., env=("database_password", "DATABASE_PASSWORD"))
    database_name: str      = Field(..., env=("database_name", "DATABASE_NAME"))
    database_username: str  = Field(..., env=("database_username", "DATABASE_USERNAME"))
    secret_key: str         = Field(..., env=("secret_key", "SECRET_KEY"))
    algorithm: str          = Field(..., env=("algorithm", "ALGORITHM"))
    access_token_expire_minutes: int = Field(..., env=("access_token_expire_minutes", "ACCESS_TOKEN_EXPIRE_MINUTES"))

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
