from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

path_to_env = Path(__file__).parent.parent.parent.absolute() / ".evn"


class Settings(BaseSettings):
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_file="/Users/pavelfedorenko/python programs/shop back/.env",
        env_file_encoding="utf-8",
    )


setting = Settings()

if __name__ == "__main__":
    print(setting.db_url)
