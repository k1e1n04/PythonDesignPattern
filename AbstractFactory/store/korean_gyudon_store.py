from store.gyudon_store import GyudonStore
from utls.common import *
from gyudon.korean_gyudon import *

class KoreanGyudonStore(GyudonStore):
    def create_gyudon(self, gyudon_type):
        if gyudon_type == GYUDON_TYPE_NORMAL:
            return KoreanGyudon()
        elif gyudon_type == GYUDON_TYPE_CHEESE:
            return KoreanCheeseGyudon()
        elif gyudon_type == GYUDON_TYPE_KIMUCHI:
            return KoreanKimuchiGyudon()
        else:
            return None
        