ei_response = []
sn_response = []
tf_response = []
jp_response = []


# def name():
#     # ei_response = 0
#     response = input("Enter your name: ")
#     if response == response:
#         ei_response[0] = response


def question_one():
    response = input("""
    1). 
    A. expand energy, enjoy groups, 
    B. Conserve energy, enjoy one-on-one: """)
    response_question_one(response)
    question_two()


def response_question_one(response):
    global ei_response
    if response == "a" or response == "b":
        ei_response += [response]
    else:
        print("Invalid choice")
        question_one()


def question_two():
    response = input("""
   2) 
    A. Interpret literally, 
    B. Look for meaning and possibilities: """)
    response_question_two(response)
    question_three()


def response_question_two(response):
    global sn_response
    if response == "a" or response == "b":
        sn_response += [response]

    else:
        print("Invalid choice")
        question_two()


def question_three():
    response = input("""
    3)
    A. Logical, thinking, questioning
    B. Empathetic, feeling, accommodating: """)
    response_question_three(response)
    question_four()


def response_question_three(response):
    global tf_response
    if response == "a" or response == "b":
        tf_response += [response]
    else:
        print("Invalid choice")
        question_three()


def question_four():
    response = input("""
    4)
    A. Organized, orderly:
    B. Flexible, adaptable: """)
    response_question_four(response)
    question_five()


def response_question_four(response):
    global jp_response
    if response == "a" or response == "b":
        jp_response += [response]
    else:
        print("Invalid choice")
        question_four()


def question_five():
    response = input("""
    5)
    A. More outgoing, think out loud 
    B. More reserved, think to yourself: """)
    response_question_five(response)
    question_six()


def response_question_five(response):
    global ei_response
    if response == "a" or response == "b":
        ei_response += [response]
    else:
        print("Invalid choice")
        question_five()


def question_six():
    response = input("""
    6)
    A. Practical, realistic, experiential
    B. Imagination, innovative, theoretical: """)
    response_question_six(response)
    question_seven()


def response_question_six(response):
    global sn_response
    if response == "a" or response == "b":
        sn_response += [response]
    else:
        print("Invalid choice")
        question_six()


def question_seven():
    response = input("""
    7)
    A. Candid, straight forward, frank
    B. Tactful, kind, encouraging: """)
    response_question_seven(response)
    question_eight()


def response_question_seven(response):
    global tf_response
    if response == "a" or response == "b":
        tf_response += [response]
    else:
        print("Invalid choice")
        question_seven()


def question_eight():
    response = input("""
    8)
    A. Plan, schedule
    B. Unplanned, spontaneous:  """)
    response_question_eight(response)
    question_nine()


def response_question_eight(response):
    global jp_response
    if response == "a" or response == "b":
        jp_response += [response]
    else:
        print("Invalid choice")
        question_eight()


def question_nine():
    response = input("""
    9)
    A. Candid, straight forward, frank
    B. Tactful, kind, encouraging: """)
    response_question_nine(response)
    question_ten()


def response_question_nine(response):
    global ei_response
    if response == "a" or "b":
        ei_response += [response]
    else:
        print("Invalid choice")
        question_nine()


def question_ten():
    response = input("""
   10)
    A. Standard, usual, conventional  
    B. Different, novel, unique:  """)
    response_question_ten(response)
    question_eleven()


def response_question_ten(response):
    global sn_response
    if response == "a" or response == "b":
        sn_response += [response]
    else:
        print("Invalid choice")
        question_nine()


def question_eleven():
    response = input("""
    11)
    A. Firm, tend to criticize, hold the line
    B. Gentle, tend to appreciate, conciliate: """)
    response_question_eleven(response)
    question_twelve()


def response_question_eleven(response):
    global tf_response
    if response == "a" or response == "b":
        tf_response += [response]
    else:
        print("Invalid choice")
        question_eleven()


def question_twelve():
    response = input("""
    12)
    A. Regulated, structured
    B. Easygoing, live and let live: """)
    response_question_twelve(response)
    question_thirteen()


def response_question_twelve(response):
    global jp_response
    if response == "a" or response == "b":
        jp_response += [response]
    else:
        print("Invalid choice")
        question_twelve()


def question_thirteen():
    response = input("""
    13)
    A. External, communicative, express yourself
    B. Internal, reticent, keep to yourself: """)
    response_question_thirteen(response)
    question_fourteen()


def response_question_thirteen(response):
    global ei_response
    if response == "a" or response == "b":
        ei_response += [response]
    else:
        print("Invalid choice")
        question_thirteen()


def question_fourteen():
    response = input("""
    14)
    A. Focus on here-and-now 
    B. Look to the future, global perspective, "big picture: """)
    response_question_fourteen(response)
    question_fifteen()


def response_question_fourteen(response):
    global sn_response
    if response == "a" or response == "b":
        sn_response += [response]
    else:
        print("Invalid choice")
        question_fourteen()


def question_fifteen():
    response = input("""
     15)
     A. Tough minded, just
     B. Tender-hearted, merciful: """)
    response_question_fifteen(response)
    question_sixteen()


def response_question_fifteen(response):
    global tf_response
    if response == "a" or response == "b":
        tf_response += [response]
    else:
        print("Invalid choice")
        question_fifteen()


def question_sixteen():
    response = input("""
    16)
    A. Preparation, plan ahead
    B. Go with the flow, adapt as you go: """)
    response_question_sixteen(response)
    question_seventeen()


def response_question_sixteen(response):
    global jp_response
    if response == "a" or response == "b":
        jp_response += [response]
    else:
        print("Invalid choice")
        question_sixteen()


def question_seventeen():
    response = input("""
    17)
    A. Active, initiate
    B. Reflective, deliberate: """)
    response_question_seventeen(response)
    question_eighteen()


def response_question_seventeen(response):
    global ei_response
    if response == "a" or response == "b":
        ei_response += [response]
    else:
        print("Invalid choice")
        question_seventeen()


def question_eighteen():
    response = input("""
     18)
     A. Facts, things, "what is"		 
     B. Ideas, dreams, what could be, philosophical:  """)
    response_question_eighteen(response)
    question_nineteen()


def response_question_eighteen(response):
    global sn_response
    if response == "a" or response == "b":
        sn_response += [response]
    else:
        print("Invalid choice")
        question_eighteen()


def question_nineteen():
    response = input("""
    19)
    A. Matter of fact, issue oriented	 
    B. Sensitive, people-oriented, compassionate:  """)
    response_question_nineteen(response)
    question_twenty()


def response_question_nineteen(response):
    global tf_response
    if response == "a" or response == "b":
        tf_response += [response]
    else:
        print("Invalid choice")
        question_nineteen()


def question_twenty():
    response = input("""
    20)
    A. Control, govern
    B. Latitude, freedom: """)
    response_question_twenty(response)


def response_question_twenty(response):
    global jp_response
    if response == "a" or response == "b":
        jp_response += [response]
    else:
        print("Invalid choice")
        question_twenty()


question_one()
