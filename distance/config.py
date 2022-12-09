from pydantic import BaseSettings

class Config(BaseSettings):
    MYSQL_HOST: str = "127.0.0.1"
    MYSQL_PORT: int = 33306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "123qwe"
    MYSQL_DATABASE: str = "vtk"
    POSTGRES_HOST: str = "127.0.0.1"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "app"
    POSTGRES_PASSWORD: str = "123qwe"
    POSTGRES_DATABASE: str = "vtk"
    CLICKHOUSE_HOST: str = "127.0.0.1"
    VERTICA_HOST: str = "127.0.0.1"
    VERTICA_PORT: int = 5433
    VERTICA_USER: str = "app"
    VERTICA_PASSWORD: str = "123qwe"

    class Config:
        env_file = '../.env'

settings = Config()
