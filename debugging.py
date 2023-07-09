import sys
import torch

if __name__ == "__main__":
    out = sys.argv
    name = 3
    c = torch.cuda.device_count()
    torch.rand(-1)
    raise ZeroDivisionError
    name = 2
    