import requests
import os

from utils.json import simplify_json

class FigmaClient:
    def __init__(self):
        self.token = os.getenv("FIGMA_TOKEN")
        self.base_url = "https://api.figma.com/v1"

    def get_file_nodes_json(self, file_key):
        headers = {"X-Figma-Token": self.token}
        response = requests.get(
            f"{self.base_url}/files/{file_key}",
            headers=headers
        )
        data_dict = response.json()
        res = data_dict
        if "document" in data_dict:
            res = simplify_json(data_dict["document"])
        print(res)
        return res