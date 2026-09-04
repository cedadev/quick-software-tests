import sys

def check_pytorch():
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


if check_pytorch():
    print("PyTorch test passed")
    sys.exit(0)
else:
    print("PyTorch test failed")
    sys.exit(1)
