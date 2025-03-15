import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from src.dataset import get_dataloaders
from src.model import SimpleNN
import matplotlib.pyplot as plt
