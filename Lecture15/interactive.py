#!/usr/bin/python3
answer={}
def ask (q,a):
  answer[q]=a
questions="What's your name?","How old are you?","What is your favourite colour?","Do you like Python?","The world is flat: True or False?"
question=list(questions)
for q in question:
  a=input(q)
  ask(q,a)
for q,a in answer.items():
  print(q+"\n"+a)
