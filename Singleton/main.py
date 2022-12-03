class Singleton(object):
    def __new__(cls, *args, **kargs):
        # インスタンス が存在する場合は最初のインスタンスをそのまま返す
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class DBConnection(Singleton):
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    one = DBConnection("MySQL")
    print("one.name={0}".format(one.name))
    two = DBConnection("Postgres")
    print("one.name={0}, two.name={1}".format(one.name, two.name))
    one.name = "Sqlite3"
    print("one.name={0}, two.name={1}".format(one.name, two.name))