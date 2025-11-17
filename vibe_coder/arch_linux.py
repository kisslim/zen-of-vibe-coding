from .terminal import SudoTerminal

class ArchLinuxEnvironment:
    def __init__(self):
        self.terminal = SudoTerminal()
        self.available_tools = self._detect_tools()
    
    def _detect_tools(self) -> dict:
        """Detect available development tools on the system"""
        tools = {}
        
        # Check programming languages
        for lang, cmd in [
            ('python', 'python3 --version'),
            ('node', 'node --version'),
            ('gcc', 'gcc --version'),
            ('rust', 'rustc --version'),
            ('go', 'go version'),
            ('java', 'java -version')
        ]:
            stdout, stderr, code = self.terminal.execute_command(cmd)
            tools[lang] = code == 0
        
        # Check build tools
        for tool, cmd in [
            ('make', 'make --version'),
            ('cmake', 'cmake --version'),
            ('cargo', 'cargo --version'),
            ('npm', 'npm --version'),
            ('pip', 'pip3 --version')
        ]:
            stdout, stderr, code = self.terminal.execute_command(cmd)
            tools[tool] = code == 0
        
        # Check system tools
        for tool, cmd in [
            ('git', 'git --version'),
            ('docker', 'docker --version'),
            ('vim', 'vim --version'),
            ('nano', 'nano --version')
        ]:
            stdout, stderr, code = self.terminal.execute_command(cmd)
            tools[tool] = code == 0
        
        return tools
    
    def install_package(self, package: str) -> Tuple[bool, str]:
        """Install a package using pacman"""
        stdout, stderr, code = self.terminal.execute_command(f"sudo pacman -S --noconfirm {package}")
        return code == 0, stdout + stderr
    
    def create_project_structure(self, project_name: str, structure: dict) -> Tuple[bool, str]:
        """Create a project directory structure"""
        try:
            # Create main directory
            self.terminal.execute_command(f"mkdir -p {project_name}")
            self.terminal.execute_command(f"cd {project_name}")
            
            # Create files and subdirectories
            for item, content in structure.items():
                if item.endswith('/'):
                    # It's a directory
                    self.terminal.execute_command(f"mkdir -p {project_name}/{item}")
                else:
                    # It's a file
                    success, message = self.terminal.write_file(f"{project_name}/{item}", content)
                    if not success:
                        return False, message
            
            return True, f"Project structure created for {project_name}"
        except Exception as e:
            return False, f"Error creating project structure: {str(e)}"