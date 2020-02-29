from src.bubble import Bubble
from src.bubble_types import BubbleTypes

class TestBubble:

  def test_current_hp(self):
    empty_bubble = Bubble(BubbleTypes.Empty)
    red_bubble = Bubble(BubbleTypes.Red)
    blue_bubble = Bubble(BubbleTypes.Blue)

    assert empty_bubble.current_hp() == 0
    assert red_bubble.current_hp() == 1
    assert blue_bubble.current_hp() == 4

  def test_decrement_hp(self):
    bubble = Bubble(BubbleTypes.Yellow)

    bubble.decrement_hp()
    assert bubble.type == BubbleTypes.Green

    bubble.decrement_hp()
    assert bubble.type == BubbleTypes.Red

    bubble.decrement_hp()
    assert bubble.type == BubbleTypes.Empty

    bubble.decrement_hp()
    assert bubble.type == BubbleTypes.Empty