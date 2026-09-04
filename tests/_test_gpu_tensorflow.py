import sys

def check_tensorflow():
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


if check_tensorflow():
    print("TensorFlow test passed")
    sys.exit(0)
else:
    print("TensorFlow test failed")
    sys.exit(1)
