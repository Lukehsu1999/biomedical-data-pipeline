import pandas as pd
import sys

try:
    # Read from stdin
    file = pd.read_csv(sys.stdin)
    df = pd.DataFrame(file)
    
    # Write to stdout
    df.to_csv(sys.stdout, index=False)
    
    # Ensure proper exit
    sys.exit(0)
except Exception as e:
    # Write errors to stderr
    print(str(e), file=sys.stderr)
    sys.exit(1)
