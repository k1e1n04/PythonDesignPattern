from store.gyudon_store import GyudonStore
from utls.common import *
from gyudon.japanese_gyudon import *

class JapaneseGyudonStore(GyudonStore):
    def create_gyudon(self, gyudon_type):
        if gyudon_type == GYUDON_TYPE_NORMAL:
            return JapaneseGyudon()
        elif gyudon_type == GYUDON_TYPE_CHEESE:
            return JapaneseCheeseGyudon()
        elif gyudon_type == GYUDON_TYPE_KIMUCHI:
            return JapaneseKimuchiGyudon()
        else:
            return None
        