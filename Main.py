import json

Stage_file = open('Stages.json')
Stage_data = json.load(Stage_file)

class Stage:
    def __init__(self, Stage_key):
        Stage_obj = Stage_data[Stage_key]
        self.Text = Stage_obj["Text"]
        self.options = Stage_obj["Options"]
        if self.options ==[]:
            self.isEnding = True
        else: self.isEnding = False

    def GetChildStage(self, child_Index):
        childStage_name = self.options[child_Index -1]["ChildStage"]
        childStage = Stage(childStage_name)
        return childStage

def inputValid(input,Stage):
    try: 
        input = int(input)
        if input > len(Stage.options):
            return False
        else:
            return True
    except ValueError:
        return False
def printStory(stage):
    print(stage.Text)
    for option in stage.options:
        print(option["OptionText"])
    

currentStage = Stage("Stage0")
printStory(currentStage)
while currentStage.isEnding == False:
    choice_txt = input("enter your choice:")
    while inputValid(choice_txt,currentStage) == False:
        choice_txt = input("enter a valid choice:")
    choice_int = int(choice_txt)
    currentStage = currentStage.GetChildStage(choice_int)
    printStory(currentStage)
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