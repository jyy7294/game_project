class LoginManager:
    def __init__(self,correct_id,correct_pw):
        self.correct_id = correct_id
        self.correct_pw = correct_pw

    def login(self):
        for count in range(3):
            id = input("ID를 입력하세요: ")
            pwd = input("PASSWORD를 입력하세요: ")

            if(id == self.correct_id) and (pwd == self.correct_pw):
                print("로그인 되었습니다.")
                return True
            
            else:
                print("아이디 또는 비밀번호가 틀렸습니다.")

        print("로그인 3회 실패로 프로그램이 종료됩니다.")
        return False