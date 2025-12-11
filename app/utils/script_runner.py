import subprocess
import tempfile

def run_script_dynamic(code: str, context: dict = None):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
        tmp.write(code.encode("utf-8"))
        tmp.flush()
        try:
            proc = subprocess.run(
                ["python3", tmp.name],
                capture_output=True,
                text=True,
                timeout=30
            )
            return {
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "returncode": proc.returncode,
                "context_echo": context
            }
        except Exception as e:
            return {"error": str(e)}
