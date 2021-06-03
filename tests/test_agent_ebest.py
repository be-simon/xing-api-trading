import unittest
import inspect
import time
from agent.ebest import EBest
from agent.xa_session import XASession_EventHandler

class TestEBest(unittest.TestCase):
  def setUp(self):
    self.ebest = EBest('DEMO')
    self.ebest.connect_server()
    self.ebest.login()

  def tearDown(self):
    # self.ebest.real_manager.real_disconnect_server()
    self.ebest.logout()
    
    
  @unittest.skip('login skip')
  def test_login(self):
    print('<' + inspect.stack()[0][3] + '>')
    
  @unittest.skip('get_stock_list skip')
  def test_get_stock_list(self):
    print('<' + inspect.stack()[0][3] + '>')
    result = self.ebest.query_manager.get_stock_list(1)
    print(result)
    
  # @unittest.skip('get_stock_top_capital skip')
  def test_get_stock_top_capital(self):
    print('<' + inspect.stack()[0][3] + '>')
    result = self.ebest.query_manager.get_stock_top_capital('001')
    print(result)
    
  @unittest.skip('get_real_news skip')
  def test_get_real_news(self):
    print('<' + inspect.stack()[0][3] + '>')
    result = self.ebest.real_manager.get_real_news()
    sleep(5)
    self.ebest.real_manager.real_disconnect_server()
    
    