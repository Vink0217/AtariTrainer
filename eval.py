#!/usr/bin/env python
"""
Evaluate a saved Stable-Baselines3 model on an Atari environment.

Usage:
    python eval.py path/to/model.zip --env "ALE/Pong-v5" --episodes 10 --render
"""
import argparse
import gymnasium as gym
import ale_py
import os
import time

from stable_baselines3 import PPO

def evaluate(model_path: str, env_id: str = "ALE/Pong-v5", n_episodes: int = 10, render: bool = False):
    # Ensure ALE envs are registered
    try:
        gym.register_envs(ale_py)
    except Exception:
        pass

    # Create a normal (non-vectorized) env for evaluation
    render_mode = "human" if render else None
    env = gym.make(env_id, render_mode=render_mode)
    model = PPO.load(model_path)

    rewards = []
    durations = []
    for ep in range(n_episodes):
        obs, info = env.reset()
        done = False
        total_reward = 0.0
        start = time.time()
        while True:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += float(reward)
            if terminated or truncated:
                break
            if render:
                # rendering handled by env
                pass
        duration = time.time() - start
        rewards.append(total_reward)
        durations.append(duration)
        print(f"[Eval] Episode {ep+1}/{n_episodes} reward={total_reward:.2f} time={duration:.2f}s")

    env.close()
    mean_reward = sum(rewards) / len(rewards) if rewards else float("nan")
    mean_time = sum(durations) / len(durations) if durations else float("nan")
    print(f"[Eval] Mean reward over {n_episodes} episodes: {mean_reward:.2f}")
    print(f"[Eval] Mean episode duration: {mean_time:.2f}s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model", help="Path to a saved SB3 model zip (e.g., runs/.../best_model.zip)")
    parser.add_argument("--env", default="ALE/Pong-v5", help="Environment id")
    parser.add_argument("--episodes", type=int, default=10, help="Number of episodes to run")
    parser.add_argument("--render", action="store_true", help="Render environment to screen")
    args = parser.parse_args()

    if not os.path.exists(args.model):
        raise FileNotFoundError(f"Model not found: {args.model}")

    evaluate(args.model, env_id=args.env, n_episodes=args.episodes, render=args.render)
