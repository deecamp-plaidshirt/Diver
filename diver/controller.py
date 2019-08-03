import os 
from parser import Parser
from sanic import Sanic
from sanic.response import json


class Controller:
    def __init__(self):
        self.parser = Parser()
        self.server = Sanic()
        self.args = self.parser.parse()
        self.buildRouter()

    def buildRouter(self):
        @self.server.route('/')
        async def test(request):
            return json({"hello": "world"})
        @self.server.post('/')
        async def main(request):
            return json({"hello": "post"})

    def run(self):
        self.server.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    controller = Controller()
    print("start controller test")
    controller.run()

