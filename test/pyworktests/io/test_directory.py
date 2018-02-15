from unittest import TestCase

from pyworks.io.directory import Directory


class TestDirectory(TestCase):
    def test_exists_returns_true_on_current_directory(self) -> None:
        self.assertTrue(Directory.exists("."))

    def test_exists_returns_false_on_nonexistent_direcotry(self) -> None:
        self.assertFalse(Directory.exists("this_directory_does_not_exist"))
