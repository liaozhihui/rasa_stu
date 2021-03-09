from bert_serving.server.helper import get_args_parser
from bert_serving.server import BertServer
args = get_args_parser().parse_args(['-model_dir', 'G:/data/chinese_L-12_H-768_A-12'])

server = BertServer(args)
server.start()
