import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from lightning.fabric import Fabric


class Trainer:
    def __init__(
        self,
        model: nn.Module,
        optimizer: optim.Optimizer = None,
        data_loader: data.DataLoader = None,
    ) -> None:
        self.fabric = Fabric()
        if self.fabric.world_size > 1:
            raise NotImplementedError("Distributed training is not supported yet.")
        print("Setting up model...")
        self.model = self.fabric.setup_module(model)
        # self.optimizer = self.fabric.setup_optimizers(optimizer)
        # self.data_loader = self.fabric.setup_dataloaders(data_loader)

    def train(self) -> None:
        # Placeholder for training logic
        pass
