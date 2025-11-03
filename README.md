# AtariTrainer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Framework: SB3](https://img.shields.io/badge/Framework-Stable_Baselines3-brightgreen)](https://stable-baselines3.readthedocs.io/en/master/)
[![Gymnasium](https://img.shields.io/badge/Env-Gymnasium-ffC000)](https://gymnasium.farama.org/)

A robust, configurable, and extensible training pipeline for Atari agents using Gymnasium and Stable-Baselines3. This repository provides a full framework for training, evaluating, and watching agents on any Atari game.



---

## ✨ Key Features

* **Multi-Algorithm Support:** Train state-of-the-art agents using PPO, DQN, or A2C right out of the box.
* **Config-Driven:** All hyperparameters are managed in simple `*.yaml` files.
* **Flexible CLI:** Override any config setting (like `algo`, `env_id`, or `total_timesteps`) directly from the command line.
* **Resume Training:** Stop and resume training from any saved checkpoint (`.zip` file) using the `--load-model` flag.
* **Automatic Evaluation:** The `EvalCallback` saves the `best_model.zip` based on performance, not just the final model.
* **Rotating Checkpoints:** Automatically deletes old checkpoints to save disk space, keeping only the most recent ones.
* **Generic Watch Script:** A single `game.py` script that can load any trained model and play back its performance for any Atari game.

---

## 💻 Project Structure

AtariTrainer/
├── configs/
│   ├── base.yaml         # Main hyperparameter config file
│   └── smooth.yaml
├── trainer/
│   ├── __init__.py       # Makes 'trainer' a Python package
│   ├── runner.py         # The main Trainer class
│   ├── envs.py           # Environment creation factory
│   ├── callbacks.py      # Custom callbacks (EarlyStopping, RotatingCheckpoints)
│   └── utils.py          # Helper functions (seeding, logging)
├── .gitignore            # Tells Git what to ignore (e.g., /runs)
├── .python-version       # <-- Your Python version pin
├── game.py               # Your CLI script to WATCH a trained agent
├── eval.py               # Your script for running evaluations
├── train.py              # Your main CLI script for TRAINING
├── pyproject.toml        # <-- Your main project config/dependencies
├── uv.lock               # <-- Your dependency lock file
├── requirements.txt      # List of Python dependencies (pip install -r ...)
└── README.md             # Your new professional project homepage


---

## 🚀 Getting Started

### 1. Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Vink0217/AtariTrainer.git](https://github.com/Vink0217/AtariTrainer.git)
    cd AtariTrainer
    ```

2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Monitoring with TensorBoard

Before you start, open a separate terminal and run TensorBoard to watch your agent learn in real-time.

```bash
tensorboard --logdir ./runs
🎮 How to Use (The Commands)
This pipeline is run from the command line.

To Train a New Agent (from Scratch)
Use train.py to start a new training run. The script will create a unique, timestamped folder inside ./runs/ to store logs and models.

Bash

# Train the default PPO agent on Pong for 10 million steps
python train.py --config configs/base.yaml --algo PPO --total-timesteps 10000000 --device cuda
You can easily train any algorithm on any game by changing the flags:

Bash

# Train a DQN agent on Breakout for 10 million steps
python train.py --config configs/base.yaml --algo DQN --env "ALE/Breakout-v5" --total-timesteps 10000000 --device cuda
To Resume Training
Use the --load-model flag to load a previously saved model (.zip file) and continue training. This is perfect for fine-tuning or resuming an interrupted run.

Bash

# Load your 'best_model.zip' and fine-tune it for 5 million more steps
python train.py --config configs/base.yaml --total-timesteps 5000000 --device cuda --load-model "./runs/ALE_Pong-v5_PPO_.../best_model.zip"
To Watch Your Trained Agent
Use game.py to load any saved model and watch it play.

The script takes the path to the model as the first argument. If the game is not Pong, you must specify it with the --env flag.

Bash

# Watch your best Pong agent
python game.py "./runs/ALE_Pong-v5_PPO_.../best_model.zip"

# Watch a trained Breakout agent
python game.py "./runs/ALE_Breakout-v5_DQN_.../best_model.zip" --env "ALE/Breakout-v5"
📈 Future Work (Roadmap)
This project is the perfect foundation for more advanced RL concepts. The next planned steps are:

[ ] Hyperparameter Sweeps: Integrate Optuna to find the optimal hyperparameters for each game.

[ ] AI-vs-AI Arena: Modify the environment to enable self-play between two policies.

[ ] Continuous Integration: Add a GitHub Action to automatically run a short test on every push.

[ ] Web UI Dashboard: Build a simple Flask/FastAPI app to display results.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.


---

### ## Final Step: Create Your `LICENSE` File

You mentioned an "MIT License" in your GitHub badges. To make this official, create one last file named `LICENSE` (no extension) in your main folder.

**Copy-paste this text into your `LICENSE` file:**