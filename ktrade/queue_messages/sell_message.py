from ktrade.queue_messages.queue_message import QueueMessage
from ktrade.models import Trade

class SellMessage(QueueMessage):
  def __init__(self, trade: Trade, amount: float):
    super().__init__(type='SELL')
    self.trade = trade
    self.amount = amount
