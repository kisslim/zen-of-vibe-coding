import pytest
import tempfile
import os
from unittest.mock import Mock, patch

from vibe_coder.core import VirtualVibeCoder
from vibe_coder.terminal import SudoTerminal


class TestVirtualVibeCoder:
    def test_initialization(self):
        """Test that the vibe coder initializes correctly"""
        with patch('vibe_coder.core.Ollama'):
            coder = VirtualVibeCoder(model_name="test-model")
            assert coder.model_name == "test-model"
            assert isinstance(coder.environment.terminal, SudoTerminal)

    def test_process_request_format(self):
        """Test that requests are formatted correctly"""
        with patch('vibe_coder.core.Ollama') as mock_llm:
            mock_llm.return_value.invoke.return_value = "Test response"
            coder = VirtualVibeCoder(model_name="test-model")
            
            response = coder.process_request("test request")
            
            assert "## Vibe Coder Response" in response
            assert "## Execution Results" in response

    def test_conversation_history(self):
        """Test that conversation history is maintained"""
        with patch('vibe_coder.core.Ollama') as mock_llm:
            mock_llm.return_value.invoke.return_value = "Test response"
            coder = VirtualVibeCoder(model_name="test-model")
            
            # Process multiple requests
            coder.process_request("first request")
            coder.process_request("second request")
            
            assert len(coder.conversation_history) == 4  # 2 user + 2 assistant


class TestSudoTerminal:
    def test_execute_basic_command(self):
        """Test basic command execution"""
        terminal = SudoTerminal()
        stdout, stderr, code = terminal.execute_command("echo 'test'")
        
        assert code == 0
        assert 'test' in stdout

    def test_file_operations(self):
        """Test file read/write operations"""
        terminal = SudoTerminal()
        
        # Use temp file for testing
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            test_file = f.name
            test_content = "test content"
        
        try:
            # Test write
            success, message = terminal.write_file(test_file, test_content)
            assert success
            assert "written successfully" in message
            
            # Test read
            success, content = terminal.read_file(test_file)
            assert success
            assert content == test_content
        finally:
            # Cleanup
            os.unlink(test_file)

    def test_directory_change(self):
        """Test directory change functionality"""
        terminal = SudoTerminal()
        original_dir = terminal.get_current_directory()
        
        # Test changing to home directory
        stdout, stderr, code = terminal.execute_command("cd ~")
        new_dir = terminal.get_current_directory()
        
        assert code == 0
        assert new_dir != original_dir