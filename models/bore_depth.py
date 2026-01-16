import lightning as pl

from models.depth_net import DepthNet


class BoreDepthLightning(pl.LightningModule):
    def __init__(self) -> None:
        super(BoreDepthLightning, self).__init__()

        # model
        self.depth_net = DepthNet()
        # self.pose_net = PoseNet()
