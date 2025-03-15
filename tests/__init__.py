# tests/__init__.py
# This file marks the tests directory as a package.

import sys
import os

# Add the src directory to the system path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
