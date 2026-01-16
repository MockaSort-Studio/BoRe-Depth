from loss_vegas.trainer import Trainer
from models.bore_depth import BoreDepthLightning


def main() -> None:
    trainer = Trainer(model=BoreDepthLightning())
    print("Trainer initialized:", trainer)


if __name__ == "__main__":
    main()
