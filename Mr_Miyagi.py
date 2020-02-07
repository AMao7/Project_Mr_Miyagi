while True:
    question = (input("what is your question sir ")).strip().lower()
    print("questions are wise, but for now. Wax on, and Wax off!")

    if "sensei" not in question:
        print("You are smart, but not wise, address me as sensei please")

    elif "block" or "blocking:" in question:
        print("Rememeber, best block, not to be there")


    elif "sensei im at peace" in question:
        print('Sometimes, what heart know, head forget')


    elif "sensei" or "block" or "blocking" or "sensei im at peace" not in question:
        print("do not lose focus. Wax on. Wax off")

    else:
        print("do not lose focus. Wax on. Wax off.")
