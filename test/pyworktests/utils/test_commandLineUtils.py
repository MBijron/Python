from unittest import TestCase
from unittest.mock import patch

from pyworks.utils.command_line_utils import CommandLineUtils


class TestCommandLineUtils(TestCase):
    @patch('builtins.input', return_value='y')
    def test_prompt_for_yes_no_input_y_returns_true(self, anything) -> None:
        self.assertTrue(CommandLineUtils.prompt_for_yes_no("message"))

    @patch('builtins.input', return_value='n')
    def test_prompt_for_yes_no_input_n_returns_false(self, anything) -> None:
        self.assertFalse(CommandLineUtils.prompt_for_yes_no("message"))

    @patch('builtins.input', return_value='f')
    @patch("time.sleep", side_effect=InterruptedError)
    def test_prompt_for_yes_no_input_n_returns_false(self, param1, param2) -> None:
        self.assertRaises(InterruptedError, lambda : CommandLineUtils.prompt_for_yes_no("message"))