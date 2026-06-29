#!/usr/bin/env python3
"""
check_gpu_frameworks.py
Checks whether PyTorch, TensorFlow, and JAX are installed and can see CUDA/GPUs.
"""

import sys
import socket

def section(title):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print('='*50)


def check_pytorch():
    section("PyTorch")
    try:
        import torch
        print(f"  ✓ Installed       : {torch.__version__}")
        cuda_available = torch.cuda.is_available()
        print(f"  {'✓' if cuda_available else '✗'} CUDA available   : {cuda_available}")
        if cuda_available:
            n = torch.cuda.device_count()
            print(f"  ✓ GPU count       : {n}")
            for i in range(n):
                name = torch.cuda.get_device_name(i)
                mem  = torch.cuda.get_device_properties(i).total_memory / 1024**3
                print(f"    [{i}] {name}  ({mem:.1f} GB)")
            # Quick tensor op on GPU
            x = torch.tensor([1.0, 2.0]).cuda()
            print(f"  ✓ Tensor on GPU   : {x.device}")
            return True
        else:
            print("  ✗ No GPU detected — running on CPU only.")
            return False
    except ImportError:
        print("  ✗ PyTorch is NOT installed.")
        return False

def check_tensorflow():
    section("TensorFlow")
    try:
        import os
        # Suppress TF's noisy startup logs
        os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
        import tensorflow as tf
        print(f"  ✓ Installed       : {tf.__version__}")
        gpus = tf.config.list_physical_devices("GPU")
        if gpus:
            print(f"  ✓ GPU count       : {len(gpus)}")
            for gpu in gpus:
                print(f"    {gpu.device_type}: {gpu.name}")
            # Quick op on GPU
            with tf.device("/GPU:0"):
                x = tf.constant([1.0, 2.0])
            print(f"  ✓ Tensor on GPU   : {x.device}")
            return True
        else:
            print("  ✗ No GPU detected — running on CPU only.")
            return False
    except ImportError:
        print("  ✗ TensorFlow is NOT installed.")
        return False


def check_jax():
    section("JAX")
    try:
        import os
        os.environ.setdefault("JAX_PLATFORMS", "")  # allow auto-detection
        import jax
        print(f"  ✓ Installed       : {jax.__version__}")
        devices = jax.devices()
        gpu_devices = [d for d in devices if d.platform in ("gpu", "tpu")]
        if gpu_devices:
            print(f"  ✓ GPU/TPU count   : {len(gpu_devices)}")
            for d in gpu_devices:
                print(f"    {d}")
            # Quick op on GPU
            import jax.numpy as jnp
            x = jnp.array([1.0, 2.0])
            print(f"  ✓ Default backend : {jax.default_backend()}")
            return True
        else:
            print(f"  ✗ No GPU/TPU detected — default backend: {jax.default_backend()}")
            print(f"    Available devices: {devices}")
            return False
    except ImportError:
        print("  ✗ JAX is NOT installed.")
        return False


def summary():
    ret = True
    section("Summary")
    results = {}
    frameworks = {
        "PyTorch":    ("torch",      lambda t: t.cuda.is_available()),
        "TensorFlow": ("tensorflow", lambda t: len(t.config.list_physical_devices("GPU")) > 0),
        "JAX":        ("jax",        lambda j: any(d.platform in ("gpu","tpu") for d in j.devices())),
    }
    for name, (mod, gpu_check) in frameworks.items():
        try:
            import importlib
            m = importlib.import_module(mod)
            has_gpu = gpu_check(m)
            results[name] = ("✓", "✓" if has_gpu else "✗")
            if not has_gpu:
                ret = False
        except ImportError:
            results[name] = ("✗", "✗")
            ret = False

    col = 14
    print(f"  {'Framework':<{col}} {'Installed':<12} {'GPU Visible'}")
    print(f"  {'-'*col} {'-'*11} {'-'*11}")
    for name, (inst, gpu) in results.items():
        print(f"  {name:<{col}} {inst:<12} {gpu}")
    print()
    return ret


if __name__ == "__main__":
    print(f"\nPython {sys.version}")
    print(f"Running tests on {socket.gethostname()}")
    success = True
    success &= check_pytorch()
    success &= check_tensorflow()
    success &= check_jax()
    success &= summary()
    sys.exit(0 if success else 1)
