import argparse


class Parser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Diver the backend')
        self._parser.add_argument('--port', default=8080, type=int, help='listening port')
        self._parser.add_argument('--model_dir', default=None, type=str, help='pretrained model dir')
        self._parser.add_argument('--log_dir', default='./log', type=bool, help='start testing')
        self._parser.add_argument('--log_level', default='INFO', type=str, help='log level')
        

    def parse(self):
        return self._parser.parse_args()


if __name__ == '__main__':
    parser = Parser()
    print("parser test")
    print(parser.parse())