import subprocess

def cmd():
    subprocess.run(
        
        [
            "dumb-pypi",
            "--package-list", "package-list.txt",
            "--packages-url", "https://zap-09.github.io/my-pypi/packages/",
            "--output-dir", "."
      ]
    )

if __name__ == "__main__":
    cmd()