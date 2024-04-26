import wandb

__version__ = "0.1"

wandb.login(key="a7f6b11fc182ac2b92a2f4fb6bacb7916ea27f3a")
run = wandb.init(
    project="my-awesome-project"
)
