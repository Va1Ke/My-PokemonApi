from app.utils.general import get_env_value


class Settings:
    POSTGRES_USER: str = get_env_value("POSTGRES_USER")
    POSTGRES_PASSWORD: str = get_env_value("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = get_env_value("POSTGRES_HOST")
    POSTGRES_PORT: str = get_env_value("POSTGRES_PORT")
    POSTGRES_DB: str = get_env_value("POSTGRES_DB")
    MY_ALGORITHMS: str = get_env_value("MY_ALGORITHMS")
    SECRET: str = get_env_value("SECRET")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
