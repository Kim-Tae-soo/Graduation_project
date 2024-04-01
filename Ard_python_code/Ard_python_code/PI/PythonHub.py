from serial import Serial
import pyrebase
import nltk
import time

class PythonHub:
    __sDefComName = 'COM7'
    __nDefComBps = 9600
    __defWaitTime = 0.5
    
    def __init__(self, sComName = __sDefComName, nComBps = __nDefComBps): # constructor
        self.config = {
            "apiKey" : "AIzaSyBQtOBghGbgHpDYG3WLwjMZePxp0k4FFzE",
            "authDomain" : "atpproject-885d7.firebaseapp.com",
            "databaseURL" : "https://atpproject-885d7-default-rtdb.asia-southeast1.firebasedatabase.app",
            "projectId" : "atpproject-885d7",
            "storageBucket" : "atpproject-885d7.appspot.com",
            "messagingSenderId" : "943299899143",
            "appId" : "1:943299899143:web:a4e3d23d8389764353dfa2"
            }
        self.ard = Serial(sComName, nComBps)
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.userId = None
        self.clearSerial()

    def __del__(self): #destructor
        try:
           if self.ard.isOpen():
               self.ard.close()
        except AttributeError:
            pass
        
    #Public Methods
    def wait(self):
        time.sleep(self.__defWaitTime)

    # Serial Methods
    def readSerial(self):
        nRead = self.ard.inWaiting()
        if nRead > 0:
            btResult = self.ard.read(nRead)
            sResult = btResult.decode()
            return sResult
        else: return ''

    def writeSerial(self, sCmd):
        btCmd = sCmd.encode()
        return self.ard.write(btCmd)

    def clearSerial(self):
        self.wait()
        self.readSerial()

    def talk(self, sCmd):
        return self.writeSerial(sCmd + '\n')
    
    def listen(self):
        self.wait()
        sResult = self.readSerial()
        return sResult.strip()
    
    def talkListen(self, sCmd):
        self.talk(sCmd)
        return self.listen()

    # FireBase Methods
    def sendData(self):
        read = self.readSerial()
        tokens = nltk.word_tokenize(read)
        
        graphtok = int(tokens[1])
        temptok = float(tokens[0])
        bpmtok = int(float(tokens[2]))
        
        bpm = {"bpm" : bpmtok}
        temp = {"temperature" : temptok}
        self.db.child("users").child(self.userId).child("bpm").push(bpm)
        self.db.child("users").child(self.userId).child("temperature").push(temp)

        print("데이터 전송 : " + str(bpm) + " " + str(temp)+ " " + str(graphtok)) 

    # 사용자 로그인
    def login(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            self.userId = user['localId']
            
        except Exception as e:
            error_message = str(e)
            if "INVALID_EMAIL" in error_message:
                print("이메일이 올바르지 않습니다.")
            elif "INVALID_PASSWORD" in error_message:
                print("비밀번호가 올바르지 않습니다.")
            else:
                return False, error_message
        
        if self.userId:
            return True, self.userId

        else:
            raise SystemExit
