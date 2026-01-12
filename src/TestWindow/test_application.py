"""Test application helper.

Provides a TestApplication class that subclasses `QApplication` and
manages a `TestWindow` instance.
"""

import sys
from typing import Optional

from PySide6.QtWidgets import QApplication

from TestWindow.test_window import TestWindow


class TestApplication(QApplication):
	"""A small QApplication subclass that owns and shows a TestWindow.

	Example:
		app = TestApplication()
		sys.exit(app.run())
	"""

	def __init__(self, argv: Optional[list] = None) -> None:
		# If argv is None, pass through sys.argv so command-line args work.
		super().__init__(argv if argv is not None else sys.argv)
		self.window = TestWindow()

	def run(self) -> int:
		"""Show the main window and run the Qt event loop.

		Returns the application exit code (the value from `exec()`).
		"""
		self.window.show()
		return self.exec()
