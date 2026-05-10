print("===== PVG College, Nashik Chatbot =====")

while True:

    msg = input("You : ")

    if msg.lower() == "hii" or msg.lower() == "hello":

        print("Bot : Hii! Welcome to PVG Chatbot")

    elif msg.lower() == "where is your college located":

        print("Bot : We are located in Nashik")

    elif msg.lower() == "when was your college established":

        print("Bot : Our college was established in 2010")

    elif msg.lower() == "does your college have placements":

        print("Bot : Yes, our college has high placement rate")

    elif msg.lower() == "what are the branches in your college":

        print("Bot : Our college has following branches:")
        print("1. Computer Engineering")
        print("2. Information Technology")
        print("3. AIDS")
        print("4. ENTC")
        print("5. MBA")
        print("6. Mechanical Engineering")

    elif msg.lower() == "know more":

        print("Bot : www.pvgcoe.com")

    elif msg.lower() == "bye":

        print("Bot : Thank you for your time")
        break

    else:

        print("Bot : Please visit our website")