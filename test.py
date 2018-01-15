from src import *

args = ModelOptions().parse()

torch.manual_seed(args.seed)
if args.cuda:
    torch.cuda.manual_seed(args.seed)

pw_network = PatchWiseNetwork1()
iw_network = ImageWiseNetwork1()

pw_model = ImageWiseModel(args, iw_network, pw_network)
pw_model.test(args.test_path)
