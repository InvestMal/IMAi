import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "InvestMal AI"
    ENV: str = os.getenv("ENV", "development")

    # ----------- API KEYS -----------
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # ----------- AI CONFIG -----------
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4.1-mini")
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", 1024))

    # ----------- APP CONFIG -----------
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()
