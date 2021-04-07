import unittest
import inspect
from agent.ebest import EBest
from agent.xa_session import XASession_EventHandler

class TestEBest(unittest.TestCase):
  def setUp(self):
    self.ebest = EBest('DEMO')
    self.ebest.connect_server()
    self.ebest.login()
    
  def tearDown(self):
    self.ebest.logout()
    
  def test_login(self):
    print(inspect.stack()[0][3])