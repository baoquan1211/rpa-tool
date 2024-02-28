from pydantic import BaseModel
import json

class Task(BaseModel):
    func_name: str
    args: list = []
    kwargs: dict = {}
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
