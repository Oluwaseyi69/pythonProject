print(f"""List of menu functions
      1.  Phone book
      2.  Messages
      3.  Chat
      4.  Call register
      5.  Tones
      6.  Settings
      7.  Call divert
      8.  Games
      9.  Calculator
      10. Reminder
      11. Clock
      12. Profiles
      13. SIM services""")
owner_input = int(input("Press a number: "))
if owner_input == 1:
    print(f""" 
      1.  Search
      2.  Service Nos.
      3.  Add name
      4.  Erase
      5.  Edit
      6.  Assign tone
      7.  Send b'crd
      8.  Options
      9.  Speed dials
      10. Voice tags""")
    owner_input_a = int(input("Press a number: "))
    if owner_input_a == 8:
        print(f"""
    1. Type of view
    2. Memory Status """)
elif owner_input == 2:
    print(f"""
      1. Write messages
      2. inbox
      3. Outbox
      4. Picture messages
      5. Templates
      6. Smileys
      7. Message settings
      8. Info service
      9. Voice mailbox number
      10.Service command editor""")
    owner_input_two_seven = int(input("press a number: "))
    if owner_input_two_seven == 7:
        print(f"""
            1. Set 1
            2. Common 
            """)
    owner_input_one = int(input("press a number : "))
    if owner_input_one == 1:
        print(f"""
            1. Message centre number
            2. Messages sent as
            3. Messages validity""")
    owner_input_one = int(input("press a number: "))
    if owner_input == 2:
        print(f"""
            1. Delivery reports
            2. Reply via same centre
            3. Character support""")
elif owner_input == 4:
    print(f"""
            1. Missed calls
            2. Received calls
            3. Dialed numbers
            4. Erase recent call lists
            5. Show call duration
            6. Show call costs
            7. Call cost settings
            8. prepaid credit""")
    owner_input = int(input("press a number: "))
    if owner_input == 5:
        print(f"""
        1. Last call duration
        2. All calls' duration
        3. Received calls' duration
        4. Dialled calls' duration
        5. Clear timers""")

    elif owner_input == 6:
        print(f"""
        1. Last call cost
        2. All calls' cost
        3. Clear counters""")
    elif owner_input == 7:
        print(f"""
        1. Call cost limit
        2. Show costs in""")
elif owner_input == 5:
    print("""
    1. Ringing tone
    2. Ringing volume
    3. Incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver""")
elif owner_input == 6:
    print(f"""
    1. Call settings
    2. Phone settings
    3. Security settings
    4. Restore factory settings""")
    owner_input = int(input("press a number: "))
    if owner_input == 1:
        print(f"""
        1. Automatic redial
        2. Speed dialling
        3. Call waiting
        4. Own number sending
        5. Phone line in use
        6. Automatic answer""")
    elif owner_input == 2:
        print(f"""
        1. Language
        2. Cell info display
        3. Welcome note
        4. Network selection
        5. Lights
        6. Confirm SIM services actions""")
    elif owner_input == 3:
        print(f"""
        1. PIN code request
        2. Call barring service
        3. Fixed dialling
        4. Closed user group
        5. Phone security
        6. Change access codes""")
    elif owner_input == 4:
        print("Restore factory settings")
elif owner_input == 7:
    print("Call divert ")
elif owner_input == 8:
    print("Games ")
elif owner_input == 9:
    print("Calculator")
elif owner_input == 10:
    print("Reminders ")
elif owner_input == 11:
    print(f"""
          1. Alarm clock
          2. Clock settings
          3. Date setting
          4. Stopwatch 
          5. Counter timer
          6. Auto update of date and time""")

else:
    print("Invalid input")
