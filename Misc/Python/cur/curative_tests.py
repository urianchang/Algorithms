import unittest
import datetime
from solution import bill_for

user_signed_up = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

constant_users = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

new_plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_dollars': 4
}

no_users = []

# Note: the class must be called Test
class Test(unittest.TestCase):
    def test_works_when_the_customer_has_no_active_users_during_the_month(self):
      self.assertAlmostEqual(bill_for('2019-01', new_plan, no_users), 0.00, delta=0.01)

    def test_works_when_everything_stays_the_same_for_a_month(self):
      self.assertAlmostEqual(bill_for('2019-01', new_plan, constant_users), 8.00, delta=0.01)

    def test_works_when_a_user_is_activated_during_the_month(self):
      self.assertAlmostEqual(bill_for('2019-01', new_plan, user_signed_up), 10.84, delta=0.01)


