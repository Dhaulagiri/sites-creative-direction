import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("installer", Path(__file__).resolve().parents[1] / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skills = self.root / ".agents/skills"
        self.instructions = self.root / "AGENTS.md"

    def test_install_preserves_instructions_and_is_idempotent(self):
        existing = "# Team instructions\nKeep existing conventions.\n"
        self.instructions.write_text(existing)
        link, _ = installer.install(self.skills, self.instructions)
        first = self.instructions.read_text()
        installer.install(self.skills, self.instructions)
        self.assertEqual(first, self.instructions.read_text())
        self.assertTrue(first.startswith(existing))
        self.assertTrue((link / "SKILL.md").is_file())
        self.assertEqual(link.resolve(), installer.SOURCE)

    def test_existing_skill_is_not_overwritten(self):
        target = self.skills / installer.NAME
        target.mkdir(parents=True)
        sentinel = target / "mine.txt"
        sentinel.write_text("keep")
        with self.assertRaises(ValueError):
            installer.install(self.skills, self.instructions)
        self.assertEqual(sentinel.read_text(), "keep")
        self.assertFalse(self.instructions.exists())

    def test_shadowing_override_stops_before_changes(self):
        (self.root / "AGENTS.override.md").write_text("existing override")
        with self.assertRaises(ValueError):
            installer.install(self.skills, self.instructions)
        self.assertFalse(self.skills.exists())

    def test_malformed_managed_block_stops_before_changes(self):
        original = "Keep me\n" + installer.START
        self.instructions.write_text(original)
        with self.assertRaises(ValueError):
            installer.install(self.skills, self.instructions)
        self.assertEqual(self.instructions.read_text(), original)
        self.assertFalse(self.skills.exists())

    def test_update_preserves_surrounding_user_text(self):
        before = "prefix\n" + installer.START + "\nold\n" + installer.END + "\nsuffix\n"
        result = installer.update_text(before, installer.hook(Path("/example")))
        self.assertTrue(result.startswith("prefix\n"))
        self.assertTrue(result.endswith("\nsuffix\n"))
        self.assertNotIn("\nold\n", result)

    def test_symlinked_instructions_are_not_modified(self):
        other = self.root / "other.md"
        other.write_text("keep")
        self.instructions.symlink_to(other)
        with self.assertRaises(ValueError):
            installer.install(self.skills, self.instructions)
        self.assertEqual(other.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
