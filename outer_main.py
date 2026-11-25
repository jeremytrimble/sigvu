import multiprocessing

from sigvu.main import main

if __name__ == "__main__":
    # Under "spawn" each worker re-imports this module, so main() must not run
    # at import time. freeze_support() is a no-op when not frozen.
    multiprocessing.freeze_support()
    main()
