#initializations
f = open("data.txt", "a+")
v_id = {"1": "abc", "2": "xyz", "3": "pqr"}
empty_id = list(v_id.keys())
limit = len(v_id)
i = 0
incorrect = 0
counter = 0
PartyA = 0
PartyB = 0
NOTA = 0

# Admin password
password = 1234

# admin adding new voters
def register_voter():
    new_id = input("Enter new voter id: ")
    new_name = input("Enter new voter name: ")
    if new_id not in v_id:
        v_id[new_id] = new_name
        empty_id.append(new_id)
        print("Voter registered successfully.")
    else:
        print("Voter id already exists.")

# admin choice
def admin_panel():
    input_password = int(input("Enter admin password: "))
    if input_password == password:
        print("1. Register new voter")
        print("2. View results")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            register_voter()
        elif choice == 2:
            view_results()
        else:
            print("Invalid choice.")
    else:
        print("Incorrect password.")

# result
def view_results():
    total_votes = PartyA + PartyB + NOTA
    if total_votes == 0:
        print("No votes cast yet.")
        return
    print(f"Party A: {PartyA} votes ({(PartyA/total_votes)*100:.2f}%)")
    print(f"Party B: {PartyB} votes ({(PartyB/total_votes)*100:.2f}%)")
    print(f"NOTA: {NOTA} votes ({(NOTA/total_votes)*100:.2f}%)")
    if PartyA > PartyB and PartyA > NOTA:
        print("Party A has won")
    elif PartyB > PartyA and PartyB > NOTA:
        print("Party B has won")
    elif NOTA > PartyA and NOTA > PartyB:
        print("NOTA has won")
    elif PartyA == PartyB and PartyA == NOTA:
        print("It's a tie")

# main loop
print(f.read())
while True:
    counter = len(v_id)
    # choice for operator
    vote = int(input("Enter choice (1 for voting, 2 for admin panel, 3 for exit): "))
    # voter code
    if vote == 1:
        for i in range(counter):
            # get voter id and name
            id = input("Enter your id number: ")
            name = input("Enter your name: ")
            # main voting logic
            if id in v_id and v_id[id] == name:
                if id in empty_id:
                    vote = input("Enter vote (A for Party A, B for Party B, C for NOTA, D for exit): ")
                    if vote == 'A':
                        PartyA += 1
                    elif vote == 'B':
                        PartyB += 1
                    elif vote == 'C':
                        NOTA += 1
                    elif vote == 'D':
                        ex_pass = int(input("Enter password: "))
                        if ex_pass == password:
                            break
                    else:
                        print("Invalid vote. Please enter A, B, C, or D.")
                        continue
                    # file writing
                    f.write(f"id: {id}, name: {name} voted\n")
                    empty_id.remove(id)
                else:
                    print("Already voted")
            else:
                print("Invalid ID or name")
    # admin code    
    elif vote == 2:
        admin_panel()
    # exit system
    elif vote == 3:
        ex_pass = int(input("Enter password: "))
        if ex_pass == password:
            break
    # default block
    else:
        print("Incorrect information")
        incorrect += 1
                
    if incorrect > 3:
        print("System blocked")
        break

# file storing    
for temp in empty_id:
    f.write(f"id: {temp} name: {v_id[temp]} not voted\n")           
print("Thank you")    
view_results()
f.close()