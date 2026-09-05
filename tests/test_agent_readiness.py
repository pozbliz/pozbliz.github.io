import json
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path


class JsonLdParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._inside_json_ld = False
        self._buffer = []
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self._inside_json_ld = True
            self._buffer = []

    def handle_data(self, data):
        if self._inside_json_ld:
            self._buffer.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._inside_json_ld:
            self.blocks.append(json.loads("".join(self._buffer)))
            self._inside_json_ld = False


class AgentReadinessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")

    def test_machine_readable_files_are_generated(self):
        for relative_path in ("llms.txt", "sitemap.xml"):
            with self.subTest(path=relative_path):
                path = self.site / relative_path
                self.assertTrue(path.is_file(), f"Missing {path}")
                self.assertGreater(path.stat().st_size, 0, f"Empty {path}")

    def test_llms_file_contains_usage_and_recovery_guidance(self):
        content = (self.site / "llms.txt").read_text(encoding="utf-8")
        self.assertIn("# Seb's Sandbox", content)
        self.assertIn("## When to use this site", content)
        self.assertIn("## How agents should use this site", content)
        self.assertIn("https://www.sebastianrotter.de/sitemap.xml", content)
        self.assertIn("https://www.sebastianrotter.de/posts/", content)

    def test_custom_404_contains_agent_recovery_links(self):
        content = (self.site / "404.html").read_text(encoding="utf-8")
        for target in ("/archives/", "/llms.txt", "/sitemap.xml", "/"):
            with self.subTest(target=target):
                self.assertIn(f'href="{target}"', content)

    def test_homepage_has_person_and_organization_identity(self):
        parser = JsonLdParser()
        parser.feed((self.site / "index.html").read_text(encoding="utf-8"))

        entities = []
        for block in parser.blocks:
            entities.extend(block.get("@graph", []))
            entities.append(block)

        by_type = {entity.get("@type"): entity for entity in entities}
        self.assertIn("WebSite", by_type)
        self.assertIn("Person", by_type)
        self.assertIn("Organization", by_type)

        person = by_type["Person"]
        self.assertEqual(person["name"], "Sebastian Rotter")
        self.assertEqual(person["url"], "https://www.sebastianrotter.de/")
        self.assertTrue(person["description"])

        organization = by_type["Organization"]
        self.assertEqual(organization["name"], "Seb's Sandbox")
        self.assertEqual(organization["url"], "https://www.sebastianrotter.de/")
        self.assertTrue(organization["description"])
        self.assertEqual(
            organization["contactPoint"]["email"],
            "sebs.sandbox.official@gmail.com",
        )
        self.assertTrue(organization["contactPoint"]["contactType"])


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
