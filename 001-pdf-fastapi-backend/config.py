import os
import boto3
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    app_name: str = "Full Stack PDF CRUD App"

    AWS_KEY: str
    AWS_SECRET: str
    AWS_S3_BUCKET: str = "pdf-basic-app-dimopapi"
    AWS_S3_REGION: str  # <- se cargará de .env (eu-west-3)

    class Config:
        env_file = ".env"
        extra = "ignore"

    def get_db_url(self) -> str:
        return (
            f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )

    @staticmethod
    def get_s3_client():
        settings = Settings()
        return boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_KEY,
            aws_secret_access_key=settings.AWS_SECRET,
            region_name=settings.AWS_S3_REGION,
        )
