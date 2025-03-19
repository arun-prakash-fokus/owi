import os

from pydantic import BaseModel, Field


class Pipe:
    class Valves(BaseModel):
        BASE_URL: str = Field(
            default=os.getenv("MYPIPE_BASE_URL", ""), description="Base URL for accessing the MYPIPE application."
        )
        API_KEY: str = Field(
            default=os.getenv("MYPIPE_API_KEY", ""),
            description="API key for authenticating requests to the MYPIPE application.",
        )
        MODEL_ID: str = Field(
            default=os.getenv("MYPIPE_DEFAULT_MODEL_ID", ""),
            description="Default model for generating the response in the MYPIPE application.",
        )

    def __init__(self):
        self.valves = self.Valves()

    def pipe(self, body: dict):
        # Logic goes here
        print(self.valves, body)  # This will print the configuration options and the input body
        return "Hello, World!"
