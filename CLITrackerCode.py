print("Hello, what would you like to do?")

sessions = [] ## List to store training session data

user_command = "" ## Declare variable to store user command

while user_command != "exit": ## Loop until user wants to exit
    user_command = input("Enter a command (add, list, delete, summarize, or exit): ").strip().lower() ## Removes spaces and converts to lowercase
    
    if user_command == "add": ## Add a new training session
        print("Sessions so far:", len(sessions)) ## Print number of sessions stored
        while True: ## Loop until valid input is received
            training_duration_input = input("Enter training duration in minutes: ") ## Initialize variable to store user input for training duration

            try: ## Try to convert input to integer
                training_duration = int(training_duration_input)

                if training_duration <= 0:
                    print ("Training duration can't be a negative number")
                else:
                    break
            
            except ValueError: ## If conversion fails, print error message
                print ("Invalid input, please try again")

        while True:                
            training_intensity = input("Enter training intensity (1-10): ")

            try:
                training_intensity = float(training_intensity)

                if training_intensity < 1 or training_intensity > 10:
                    print ("Training intensity must be between 1 and 10")
                else:
                    break
            
            except ValueError:
                print ("Invalid input, enter a number between 1 and 10")
                
        while True:    
            hours_slept = input("Enter hours slept last night: ")

            try:
                hours_slept = float(hours_slept)

                if hours_slept < 0 or hours_slept > 24:
                    print ("Hours slept must be between 0 and 24")
                else:
                    break
            except ValueError:
                print ("Invalid input, enter a number between 0 and 24")

        while True:
            soreness_level = input("Enter muscle soreness level (1-10): ")

            try:
                soreness_level = float(soreness_level)

                if soreness_level < 1 or soreness_level > 10:
                    print ("Soreness level must be between 1 and 10")
                else:
                    break
            except ValueError:
                print ("Invalid input, enter a number between 1 and 10")

        while True:
            energy_level = input("Enter current energy level (1-10): ")
            
            try:
                energy_level = float(energy_level)

                if energy_level < 1 or energy_level > 10:
                    print ("Energy level must be between 1 and 10")
                else:
                    break
            except ValueError:
                print ("Invalid input, enter a number between 1 and 10")
        
        session = { ## Create a dictionary to store session data
            "duration": training_duration,
            "intensity": training_intensity,
            "hours_slept": hours_slept,
            "soreness_level": soreness_level,
            "energy_level": energy_level
        }
        sessions.append(session) ## Add session data to sessions list
        print("Training session data saved")

    elif user_command == "list":
        if not sessions: ## Check if there are any sessions stored
            print("No training sessions recorded.")
        else:
            print("Training sessions:")
        for index, session in enumerate(sessions): ## Loop through sessions and print details
            load = session["duration"] * session["intensity"] ## Calculate load
            print(
                f"[{index}] " 
                f"{session['duration']} min | " 
                f"Intensity {session['intensity']} | "
                f"Load {load}"
            )

    elif user_command == "delete":
        if not sessions: ## Check if there are any sessions to delete
            print("No training sessions to delete.")
            continue
        else:

            if not sessions: ## Check if there are any sessions stored
                print("No training sessions recorded.")
            else:
                print("Training sessions:")
            for index, session in enumerate(sessions): ## Loop through sessions and print details
                load = session["duration"] * session["intensity"] ## Calculate load
                print(
                    f"[{index}] " 
                    f"{session['duration']} min | " 
                    f"Intensity {session['intensity']} | "
                    f"Load {load}"
                )

            index_input = input("Enter the session index [#] to delete: ")

        try:
            index_input = int(index_input)

            if 0 <= index_input < len(sessions): ## Check if index is valid
                removed_session = sessions.pop(index_input) ## Remove session at specified index

                duration = removed_session["duration"] ## Get duration and intensity of removed session to calculate load
                intensity = removed_session["intensity"]
                load = duration * intensity

                print(
                    f"Deleted session [{index_input}] — "
                    f"{duration} min | Intensity {intensity} | Load {load}"
                )
                
                print("Sessions left:", len(sessions)) ## Print number of sessions remaining
            
            else:
                print("Invalid index. No session deleted.")

        except ValueError:
            print("Invalid input. Please enter a numeric session index.")

    elif user_command == "summarize":
        if not sessions: ## Check if there are any sessions to summarize
            print("No training sessions to summarize.")
        else:
            total_duration = sum(session["duration"] for session in sessions) ## Calculate total duration of all sessions
            total_load = sum(session["duration"] * session["intensity"] for session in sessions) 
            avg_intensity = total_load / total_duration if total_duration > 0 else 0

            print("Training Summary:")
            print(f"Total Sessions: {len(sessions)}")
            print(f"Total Duration: {total_duration} minutes")
            print(f"Total Load: {total_load}")
            print(f"Average Intensity: {avg_intensity:.2f}")
    
    elif user_command == "exit":
        print("Exiting the program...")
    else:
        print("Invalid command, please enter add, list, delete, summarize, or exit")