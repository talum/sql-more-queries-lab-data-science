import unittest
from sql_runner import SQLRunner
import sys
sys.path.insert(0, '..')
from selects import *

sql_runner = SQLRunner()
table = sql_runner.execute_create_file()
table = sql_runner.execute_seed_file()

sql_runner = SQLRunner()
table = sql_runner.execute_create_file()
table = sql_runner.execute_seed_file()

class TestSQLMoreQueries(unittest.TestCase):

    def test_select_all_female_dogs_name_and_breed(self):
        result = [('Little Ann', 'coonhound'), ('Pickles', 'black lab'), ('Lassie', 'collie'), ('Snowy', 'fox terrier')]
        self.assertEqual(table.execute(select_all_female_dogs_name_and_breed()).fetchall(), result)

    def test_select_all_dogs_names_in_alphabetical_order(self):
        result = [(None,), ('Clifford',), ('Lassie',), ('Little Ann',), ('McGruff',), ('Pickles',), ('Scooby',), ('Snoopy',), ('Snowy',)]
        self.assertEqual(table.execute(select_all_dogs_names_in_alphabetical_order()).fetchall(), result)

    def test_select_nameless_dog(self):
        result = [(9, None, 4, 'M', 'golden retriever', 'playful', 1)]
        self.assertEqual(table.execute(select_nameless_dog()).fetchall(), result)

    def test_select_hungry_dogs_name_and_breed_ordered_by_youngest_to_oldest(self):
        result = [('Snoopy', 'beagle'), ('Clifford', 'big red'), (None, 'golden retriever'), ('Scooby', 'great dane'), ('Lassie', 'collie'), ('Pickles', 'black lab')]
        self.assertEqual(table.execute(select_hungry_dogs_name_and_breed_ordered_by_youngest_to_oldest()).fetchall(), result)

    def test_select_name_age_and_temperament_of_oldest_dog(self):
        result = [('Pickles', 13, 'mischievous')]
        self.assertEqual(table.execute(select_name_age_and_temperament_of_oldest_dog()).fetchall(), result)

    def test_select_name_and_age_of_three_youngest_dogs(self):
        result = [('Snoopy', 3), ('Clifford', 4), (None, 4)]
        self.assertEqual(table.execute(select_name_and_age_of_three_youngest_dogs()).fetchall(), result)

    def test_select_name_and_breed_of_dogs_between_age_five_and_ten_ordered_by_oldest_to_youngest(self):
        result = [('McGruff', 'bloodhound'), ('Snowy', 'fox terrier'), ('Lassie', 'collie'), ('Scooby', 'great dane'), ('Little Ann', 'coonhound')]
        self.assertEqual(table.execute(select_name_and_breed_of_dogs_between_age_five_and_ten_ordered_by_oldest_to_youngest()).fetchall(), result)

    def test_select_select_name_age_and_hungry_of_hungry_dogs_between_age_two_and_seven_in_alphabetical_order(self):
        result = [(None, 4, 1), ('Clifford', 4, 1), ('Lassie', 7, 1), ('Scooby', 6, 1), ('Snoopy', 3, 1)]
        self.assertEqual(table.execute(select_name_age_and_hungry_of_hungry_dogs_between_age_two_and_seven_in_alphabetical_order()).fetchall(), result)
