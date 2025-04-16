import sys
import traceback

class Redirect:
    def __init__(self, *, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        self.old_stdout = None
        self.old_stderr = None

    def __enter__(self):
        if self.stdout:
            self.old_stdout = sys.stdout
            sys.stdout = self.stdout
        if self.stderr:
            self.old_stderr = sys.stderr
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.stdout:
            sys.stdout = self.old_stdout
        if self.stderr:
            sys.stderr = self.old_stderr
        if exc_type:
            traceback.print_exception(exc_type, exc_val, exc_tb, file=sys.stderr)
