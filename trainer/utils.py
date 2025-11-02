import os
import json
import random
import numpy as np
import torch
from datetime import datetime

def set_seed(seed: int):
    """Set random seeds for reproducibility (as much as possible)."""
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except Exception:
        pass

def make_run_dir(base_dir: str, env_id: str, algo: str) -> str:
    """Create a run directory with a timestamp and return its path."""
    safe_env = env_id.replace("/", "_")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join(base_dir, f"{safe_env}_{algo}_{ts}")
    os.makedirs(run_dir, exist_ok=True)
    return run_dir

def save_config(cfg: dict, out_path: str):
    """Save configuration dict to YAML/JSON for reproducibility. Uses JSON for simplicity."""
    with open(out_path, "w") as f:
        json.dump(cfg, f, indent=2)

def pretty_print_cfg(cfg: dict):
    print("=== Experiment config ===")
    for k, v in cfg.items():
        print(f"{k}: {v}")
    print("=========================")
