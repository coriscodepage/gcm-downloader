import sys

import app

if __name__ == "__main__":
    if len(sys.argv) == 1:
        app.CLI()
    else:
        app.main(str(sys.argv[1]))