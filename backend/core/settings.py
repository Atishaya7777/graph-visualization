import os


class Settings:
    PROJECT_NAME: str = "Graph Visualization Backend"
    # TODO: Change this to your own database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")


settings = Settings()
