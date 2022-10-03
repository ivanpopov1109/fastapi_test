

class Some_db:

    database = {}
    _pk = 0
    @classmethod
    def put_db(cls, x1, x2):
        Some_db._pk+=1
        Some_db.database[Some_db._pk] = f'{x1}*{x2} = {x1*x2}'

    @classmethod
    def get(self):
        return Some_db.database

    @classmethod
    def delete(self, pk):
        if pk in Some_db.database.keys():
            del Some_db.database[pk]

