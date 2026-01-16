from torch.optim import Adam

from loss_vegas.trainer import Trainer
from models.bore_depth import BoreDepthLightning


def main() -> None:
    model = BoreDepthLightning()
    optimizer = Adam(model.parameters(), lr=0.001)

    trainer = Trainer(model=model, optimizer=optimizer)
    print("Trainer initialized:", trainer)


if __name__ == "__main__":
    main()
