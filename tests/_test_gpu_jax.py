import sys

def check_jax():
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


if check_jax():
    print("JAX test passed")
    sys.exit(0)
else:
    print("JAX test failed")
    sys.exit(1)
