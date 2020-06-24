import unittest
from unittest.mock import MagicMock
from LeadConverter import LeadConverter


class LeadConverterTest(unittest.TestCase):
    def test_lead_id(self):
        lead = LeadConverter()
        self.assertEqual("Olá lead abc", lead.get_lead_id("abc"))

    def test_count(self):
        lead = LeadConverter()
        lead.count_leads = MagicMock(return_value=5)
        self.assertEqual(5, lead.count_leads())
