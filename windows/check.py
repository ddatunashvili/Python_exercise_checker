# -*- coding: utf-8 -*-

import pprint
# path

from py_files.ex import *
import os
import sys
from pathlib import Path
current_path = os.getcwd()

print("checking started ... \n")
def get_answers():
    answers_path = Path(current_path + r"\answers.txt")
    answer_sheet = {}
    with open(answers_path) as ans:
        answers = ans.read().split("\n")
        for a in answers:
            a = a.split("->")
            try:
                answer_sheet[a[0]] = a[1]
            except Exception as e:
                pass
                # print(e)

    return answer_sheet


answers = get_answers()


def check_code():
    result = {"score":0,"tests":0,"correct":0,"wrong":[],"problems_count":0,"problems":{}}
    for key in answers.keys():
        try:
            if str(eval(key)) == answers[key]:
                print(f"Passed! {key}")
                result["correct"]+=1
            else:
                if answers[key] == f'"{ str(eval(key)) }"' or answers[key] == f"'{ str(eval(key))}'":
                    # print(f"Passed! {key}")
                    result["correct"]+=1

                elif str(eval(key)) == None or str(eval(key)) == "None" or "None" in str(eval(key)) :
                    result["problems"][key.split("(")[0]] = "not writen"
                else:
                    if str(eval(key))[:-2] == answers[key]:
                        result["correct"]+=1
                        continue
                    print("-----")
                    print(f"Failed! function --> {key}")
                    print()
                    print("correct: ",str(eval(key)),"wrong: ", answers[key])
                    print("-----")
                    result["wrong"].append(key+" correct: "+answers[key]+" -> result: "+str(eval(key))) 

        except Exception as e:
            if "is not defined" in str(e):
                result["problems"][key.split("(")[0]] = "not writen"
                continue 
            print("------")
            print(key)
            print(e)
            result["problems"][key.split("(")[0]]= e
            print("------")

    result["tests"] = int(len(answers)/3)
   
    result["correct"] = round(result["correct"]/3,2 )

    result["score"] = f'{round( (result["correct"]/result["tests"] )  *100)}%'

    result["problems_count"] = int(len(result["problems"]))
    
    if int(result["score"][:-1]) >= 80:
        result["status"] = "Congrats! You have 3 points"
    elif int(result["score"][:-1]) >= 60:
        result["status"] = "Congrats! You have 2 points"
    elif int(result["score"][:-1]) >= 50:
        result["status"] = "Congrats! You have 1 point"
    return result


result = check_code()



print("------\n")
pprint.pprint(result)



print("\n------\n")
print("finished!")



