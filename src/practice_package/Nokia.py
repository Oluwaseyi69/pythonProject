def power_off():
    print(f""" Power Off  """)
    exit()
    # elif owner_input == "00":
    #     power_off()


def type_of_view():
    print("Type of view \n 1. Back")
    owner_input = input("press 1 t0 back")
    if owner_input == "1":
        phonebook()
    else:
        phonebook()


def voice_tags():
    print("Voice tags\n 0.Back")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def speed_dials():
    print("1.Speed dials\n0. Back")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def options():
    print(f"""     1.Type of view
     2.Memory Status\n0. Back""")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def sending_b_card():
    print("Sending b'card \n\n0.Back")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def assign_tone():
    print("Assign Tone \n\n0.Back")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def erase():
    print("erase \n\n0.Back")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def edit():
    print("edit \n\n0.Back")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def add_name():
    print("Add name \n\n0.Back")
    owner_input = input("Press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def service_number():
    print("Service Nos \n\n0.Back")
    owner_input = input("Press a number")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def search():
    print("Search"
          "\n\n0. Back")
    owner_input = input("Press a number")
    if owner_input == "0":
        main_menu()
    else:
        main_menu()


def messages_centre_number():
    print("Message center number\n0. Back")
    owner_input = input("Press 0 to go back: ")
    if owner_input == "0":
        messages_settings()


def message_sent_as():
    print("Message sent as \n0.Back")
    owner_input = input("Press 0 to go back: ")
    if owner_input == "0":
        messages_settings()


def message_validity():
    print("Message validity \n0.Back")
    owner_input = input("Press 0 to go back: ")
    if owner_input == "0":
        messages_settings()


def set_one():
    print("""Set 1
    1. Message centre Number
    2.Message sent as
    3. Message validity
    0. Back
    """)
    owner_input = input("press a number: ")
    if owner_input == "1":
        messages_centre_number()
    elif owner_input == "2":
        message_sent_as()
    elif owner_input == "3":
        message_validity()
    elif owner_input == "0":
        messages_settings()


def common():
    print(f"""
            1. Delivery reports
            2. Reply via same centers
            3. Character support
            0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "0":
        messages_settings()


def messages_settings():
    print(f"""
            1. Set
            2. Common
            \n\n0. Back       """)
    user_entry = input("press a number: ")
    if user_entry == "1":
        set_one()
    elif user_entry == 2:
        common()
    if user_entry == 0:
        messages()


def smileys():
    print("Smileys\n0.Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        messages()


def templates():
    print("Templates\n0.Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        messages()


def picture_messages():
    print("Picture Message\n0.Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        messages()


def outbox():
    print("Outbox\n0.Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        messages()


def inbox():
    print("Inbox\n0. Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        messages()


def write_messages():
    print("Write message\n0. Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        messages()


def invalid():
    print("invalid input")


def sim_services():
    print(f"""
        Sim Services
        \n\n 0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        invalid()
        sim_services()


def profiles():
    print(f"""
            Profiles
            \n\n0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        invalid()
        profiles()


def clock():
    print(f"""
            1. Alarm clock
            2. Clock settings
            3. Date setting
            4. Stopwatch
            5. Counter timer
            6. Auto update of date and time
            \n\n0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()


def reminder():
    print("Reminder"
          "\n\n 0.Back")
    owner_input = input("press a number: ")
    if owner_input == 0:
        main_menu()
    else:
        invalid()
        reminder()


def calculator():
    print("Calculator"
          "\n\n 0. Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        invalid()
        calculator()


def games():
    print("Games"
          "\n\n 0. Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        invalid()
        games()


def call_divert():
    print("Call Divert"
          "\n\n0. Main menu ")
    owner_input_one = input("press a number: ")
    if owner_input_one == "0":
        main_menu()
    else:
        invalid()
        call_divert()


def call_settings():
    print(f"""
        1. Automatic redial
        2. Speed dialling
        3. Call waiting
        4. Own number sending
        5. Phone line in use
        6. Automatic answer
        0. Back""")
    owner_input = input("press 0: ")
    if owner_input == "0":
        settings()
    else:
        invalid()
        call_settings()


def phone_settings():
    print(f"""
        1. Language
        2. Cell info display
        3. Welcome note
        4. Network selection
        5. Lights
        6. Confirm SIM services actions
        0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "0":
        settings()
    else:
        invalid()
        phone_settings()


def pin_code_request():
    print("PIN code Request"
          "\n\n1. Back")
    owner_input = input("Enter a number:  ")
    if owner_input == "1":
        security_settings()
    else:
        pin_code_request()


def call_barring_service():
    print("Call barring settings"
          "\n0. Back"
          "\n1. Main menu")
    owner_input = input("Enter a number:  ")
    if owner_input == 0:
        security_settings()
    elif owner_input == 1:
        main_menu()
    else:
        invalid()
        call_barring_service()


def security_settings():
    print(f"""
    1. PIN code request
    2. Call barring service
    3. Fixed dialling
    4. Closed user group
    5. Phone security
    6. Change access codes
    0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "1":
        pin_code_request()
    elif owner_input == "2":
        call_barring_service()
    elif owner_input == "0":
        settings()
    else:
        invalid()
        security_settings()


def restore_factory_settings():
    print("Restore factory settings\n\n 0. Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        settings()
    else:
        invalid()
        restore_factory_settings()


def settings():
    print(f"""
        1. Call settings
        2. Phone settings
        3. Security settings
        4. Restore factory settings
        0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "1":
        call_settings()
    elif owner_input == "2":
        phone_settings()
    elif owner_input == "3":
        security_settings()
    elif owner_input == "4":
        restore_factory_settings()
    elif owner_input == "0":
        main_menu()
    else:
        print("Invalid")
        settings()


def main_menu():
    pass


main_menu()


def tone():
    print("""
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Composer
        5. Message alert tone
        6. Keypad tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        invalid()
        tone()


def call_register():
    print(f"""
                1. Missed calls
                2. Received calls
                3. Dialed numbers
                4. Erase recent call lists
                5. Show call duration
                6. Show call costs
                7. Call cost settings
                8. prepaid credit
                0. Back""")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()

    if owner_input == "5":
        print(f"""
            1. Last call duration
            2. All calls' duration
            3. Received calls' duration
            4. Dialled calls' duration
            5. Clear timers
            0. Back""")
        owner_input = input("press a number: ")
        if owner_input == "0":
            call_register()
        else:
            invalid()
            call_register()

    if owner_input == "6":
        print(f"""
            1. Last call cost
            2. All calls' cost
            3. Clear counters
            0. Back""")
        owner_input = int(input("press a number: "))
        if owner_input == "0":
            call_register()
        else:
            invalid()
            call_register()

    elif owner_input == "7":
        print(f"""
            1. Call cost limit
            2. Show costs in
            0. Back""")
        owner_input = input("press a number: ")
        if owner_input == "0":
            call_register()
    elif owner_input == "8":
        print(f"""Prepaid credit
                \n\n 0. Back""")
        owner_input = input("press a number: ")
        if owner_input == "0":
            call_register()


def chat():
    print("Chat"
          "\n\n 0. Back")
    owner_input = input("press a number: ")
    if owner_input == "0":
        main_menu()
    else:
        invalid()
        chat()


def messages():
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
          10.Service command editor
          0. Main Menu""")
    owner_input_two_seven = input("press a number: ")
    if owner_input_two_seven == "1":
        write_messages()
    elif owner_input_two_seven == "2":
        inbox()
    elif owner_input_two_seven == "3":
        outbox()
    elif owner_input_two_seven == "4":
        picture_messages()
    elif owner_input_two_seven == "5":
        templates()
    elif owner_input_two_seven == "6":
        smileys()
    elif owner_input_two_seven == "7":
        messages_settings()
    elif owner_input_two_seven == "0":
        main_menu()
    owner_input_one = input("press a number: ")
    if owner_input_one == "1":

        owner_input_one = input("press 0 to back: ")
        if owner_input_one == "0":
            messages_settings()
    elif owner_input_one == "2":
        owner_input_one = input("press 0 to back: ")
        if owner_input_one == "0":
            main_menu()
    else:
        invalid()
        messages()


# def call_settings():
#     pass


def main_menu():
    print(f"""
*****************************************
        List of menu functions
*****************************************
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
      13. SIM services
      00. Power Off""")
    owner_input = input("Press a number: ")
    if owner_input == "1":
        phonebook()
    elif owner_input == "2":
        messages()
    elif owner_input == "3":
        chat()
    elif owner_input == "4":
        call_register()
    elif owner_input == "5":
        tone()
    elif owner_input == "6":
        settings()
    elif owner_input == "7":
        call_divert()
    elif owner_input == "8":
        games()
    elif owner_input == "9":
        calculator()
    elif owner_input == "10":
        reminder()
    elif owner_input == "11":
        clock()
    elif owner_input == "12":
        profiles()
    elif owner_input == "13":
        sim_services()
    elif owner_input == "00":
        power_off()
    else:
        invalid()
        main_menu()


def phonebook():
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
          10. Voice tags
          \n\n0. Back to menu""")

    owner_input_a = input("Press a number: ")
    if owner_input_a == "1":
        search()
    elif owner_input_a == "2":
        service_number()
    elif owner_input_a == "3":
        add_name()
    elif owner_input_a == "4":
        erase()
    elif owner_input_a == "5":
        edit()
    elif owner_input_a == "6":
        assign_tone()
    elif owner_input_a == "7":
        sending_b_card()
    elif owner_input_a == "8":
        options()
    elif owner_input_a == "9":
        speed_dials()
    elif owner_input_a == "10":
        voice_tags()
    elif owner_input_a == "0":
        main_menu()
    else:
        invalid()
        phonebook()


main_menu()
