from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key : str = "" 
    algorithm : str =  "" 
    access_token_expires_minutes : int = 30

    model_config = SettingsConfigDict(env_file='.env')
