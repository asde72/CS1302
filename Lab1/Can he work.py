def CanHeVote(age):
    Voter_age = age
    if Voter_age >= 18:
        return "Yes"
    else:
        return "No"
        

User_name = input("What is your name?")
User_age = int(input("What is your age"))
Eligibility = CanHeVote(User_age)
if Eligibility == "Yes":
    print(f'Congradulations, {User_name}! You are eligible to vote!')
else:
    print(f'Sorry, {User_name}! You are not yet old enough to vote!')
