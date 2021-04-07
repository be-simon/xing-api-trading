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
    
  @unittest.skip('login skip')
  def test_login(self):
    print('<' + inspect.stack()[0][3] + '>')
    
  def test_get_stock_list(self):
    print('<' + inspect.stack()[0][3] + '>')
    result = self.ebest.query_manager.get_stock_list(1)
    print(result)