import json

# from numpy import False_

Stage_file = open('Stages3.json')
Stage_data = json.load(Stage_file)

class Stage:
    def __init__(self, Stage_key):
        Stage_obj = Stage_data[Stage_key]
        self.Text = Stage_obj["Text"]
        self.childStages = Stage_obj["ChildStages"]
        if self.childStages ==[]:
            self.isEnding = True
        else: self.isEnding = False

    def GetChildStage(self, child_Index):
        childStage_name = self.childStages[child_Index -1]
        childStage = Stage(childStage_name)
        return childStage

def inputValid(input,Stage):
    try: 
        input = int(input)
        if input > len(Stage.childStages):
            return False
        else:
            return True
    except ValueError:
        return False

currentStage = Stage("Stage0")
print(currentStage.Text)
while currentStage.isEnding == False:
    choice_txt = input("enter your choice:")
    while inputValid(choice_txt,currentStage) == False:
        choice_txt = input("enter a valid choice:")
    choice_int = int(choice_txt)
    currentStage = currentStage.GetChildStage(choice_int)
    print(currentStage.Text)
print ('the end')





# while currentStage != None:
#     user_choice = ''
#     while user_choice not in ['1','2']:
#         user_choice = input("enter your choice:")
#     currentStage = currentStage.GetChildStage(user_choice)
#     print(currentStage.Text)
# print ('Ending')

# print(currentStage.ChildStage1)
# testStage = currentStage.GetChildStage(1)
# print(testStage.Text)