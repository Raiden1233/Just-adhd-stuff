
import pyttsx3

def text_to_voice(args):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.say(args)
    engine.runAndWait()




if __name__ == '__main__':


    with open('To do list.txt', 'r') as f:
        reading_data_from_txt_file = f.readlines()

        count = 1
        for i in reading_data_from_txt_file:
            print(f'{count}: {i}')
            text_to_voice(i)
            count+= 1

        input("press eny key to exit.")    

