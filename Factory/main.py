from utls.common import *
from store.japanese_gyudon_store import *
from store.korean_gyudon_store import *

if __name__ == "__main__":
    japan = JapaneseGyudonStore()
    gyudon = japan.order(GYUDON_TYPE_NORMAL)
    gyudon = japan.order(GYUDON_TYPE_CHEESE)
    gyudon = japan.order(GYUDON_TYPE_KIMUCHI)

    korea = KoreanGyudonStore()
    gyudon = korea.order(GYUDON_TYPE_NORMAL)
    gyudon = korea.order(GYUDON_TYPE_CHEESE)
    gyudon = korea.order(GYUDON_TYPE_KIMUCHI)