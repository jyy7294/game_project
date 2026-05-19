class RankingBoard:
    def __init__(self):
        self.rank = []

    def add_record(self, nickname, count):
        record = {
            "name" : nickname,
            "count" : count
        }

        self.rank.append(record)

    def show_ranking(self):
        if len(self.rank) == 0:
            print("등록된 기록이 없습니다.")
            return
        
        self.rank.sort(key=lambda z: (z["count"], z["name"]))

        print("----명예의 전당----")

        for i in range(min(3, len(self.rank))):
            print(f"{i+1}위 {self.rank[i]['name']} {self.rank[i]['count']}회")