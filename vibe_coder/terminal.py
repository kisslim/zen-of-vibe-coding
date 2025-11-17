import subprocess
import shlex
from typing import Tuple, List, Optional
import pexpect
import os

class SudoTerminal:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.history: List[str] = []
    
    def execute_command(self, command: str, timeout: int = 30) -> Tuple[str, str, int]:
        """Execute a command with sudo privileges and return output"""
        self.history.append(command)
        
        try:
            if command.startswith('cd '):
                # Handle directory changes
                new_dir = command[3:].strip()
                if new_dir == "~":
                    new_dir = os.path.expanduser("~")
                os.chdir(new_dir)
                self.current_dir = os.getcwd()
                return f"Changed directory to {self.current_dir}", "", 0
            
            # Use pexpect for sudo commands that might need password
            if command.startswith('sudo '):
                child = pexpect.spawn('/bin/bash', ['-c', command], timeout=timeout)
                # For demo purposes, we'll assume passwordless sudo
                # In production, you'd handle password prompts here
                child.expect(pexpect.EOF)
                output = child.before.decode('utf-8', errors='ignore')
                return output, "", child.exitstatus
            
            # Regular commands
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=self.current_dir
            )
            
            return result.stdout, result.stderr, result.returncode
            
        except subprocess.TimeoutExpired:
            return "", f"Command timed out after {timeout} seconds", -1
        except Exception as e:
            return "", f"Error executing command: {str(e)}", -1
    
    def execute_script(self, script_path: str, interpreter: str = "python") -> Tuple[str, str, int]:
        """Execute a script file"""
        return self.execute_command(f"{interpreter} {script_path}")
    
    def write_file(self, filepath: str, content: str) -> Tuple[bool, str]:
        """Write content to a file"""
        try:
            with open(filepath, 'w') as f:
                f.write(content)
            return True, f"File {filepath} written successfully"
        except Exception as e:
            return False, f"Error writing file: {str(e)}"
    
    def read_file(self, filepath: str) -> Tuple[bool, str]:
        """Read content from a file"""
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            return True, content
        except Exception as e:
            return False, f"Error reading file: {str(e)}"
    
    def get_current_directory(self) -> str:
        return self.current_dir