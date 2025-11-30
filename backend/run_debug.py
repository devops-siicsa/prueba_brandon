import subprocess

with open('error_log.txt', 'w', encoding='utf-8') as f:
    try:
        subprocess.run(['python', 'debug_db.py'], stdout=f, stderr=f, check=True)
        print("Execution successful")
    except subprocess.CalledProcessError as e:
        print(f"Execution failed with code {e.returncode}")
    except Exception as e:
        f.write(f"\nWrapper error: {e}")
        print(f"Wrapper error: {e}")
