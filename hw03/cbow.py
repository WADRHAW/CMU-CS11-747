from collections import defaultdict
import math
import time
import random
import torch

class cbow(torch.nn.Module):
    def __init__(self, nwords, emb_size):
        super(cbow, self).__init__()

        self.emb = torch.nn.Embedding(nwords, emb_size)
        torch.nn.init.uniform_(self.emb.weight, -0.25, 0.25)

        self.projection = torch.nn.Linear(emb_size, nwords)
        torch.nn.init.uniform_(self.projection.weight, -0.25, 0.25)

    def forward(self, words):
        emb = self.emb(words)
        
        emb_sum = torch.sum(emb, dim=0) # emb_size
        emb_sum = emb_sum.view(1, -1) # 1, emb_size
        out = self.projection(emb_sum)
        return out