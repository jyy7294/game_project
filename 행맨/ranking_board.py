class RankingBoard:
    def __init__(self):
        self.success = []
        self.failure = []
    def add_record(self,id):
        self.success.append(id)
        self.failure.append(id)
        
    def show_result(self):
        for n in self.success :
            print(f"승리한 사람: {n}")
        for m in self.failure :
            print(f"패배한 사람: {m}")