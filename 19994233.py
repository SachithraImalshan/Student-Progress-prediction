#https://stackoverflow.com/questions/74450587/the-credits-that-can-be-entered-are-0-20-40-60-how-to-print-out-of-range-when-a
def validate_credit_input(credit):
    try:
        int_credit = int(credit)
    except ValueError:
        print("Integer required.")
        return False

    if int_credit not in [0, 20, 40, 60, 80, 100, 120]:
        print("Out of range.")
        return False

    return int_credit

def calculate_progression_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits
    if total_credits != 120:
        return "Total incorrect."
    elif fail_credits >= 80:
        return "Exclude"
    elif pass_credits == 120:
        return "Progress"
    elif pass_credits >= 100:
        return "Progress (module trailer)"
    elif pass_credits >= 0 and defer_credits >= 0:
        return "Do not progress – module retriever"
    else:
        return "Exclude"

def generate_histogram(outcomes):
    categories = {
        "Progress": 0,
        "Trailer": 0,
        "Retriever": 0,
        "Excluded": 0,
    }
    for outcome in outcomes:
        if outcome == "Progress":
            categories["Progress"] += 1
        elif outcome == "Progress (module trailer)":
            categories["Trailer"] += 1
        elif outcome == "Do not progress – module retriever":
            categories["Retriever"] += 1
        elif outcome == "Exclude":
            categories["Excluded"] += 1

    print("---------------------------------------------------------------")
    print("Histogram")
    print("Progress", categories["Progress"], ":", "*"*categories["Progress"])
    print("Trailer", categories["Trailer"], ":", "*"*categories["Trailer"])
    print("Retriever", categories["Retriever"], ":", "*"*categories["Retriever"])
    print("Excluded", categories["Excluded"], ":", "*"*categories["Excluded"])
    print(len(outcomes), "outcomes in total.")
    print("---------------------------------------------------------------")

outcomes = []
credit_data = []
check = input("Are you a student(S) or a staff member(F)? ")
while True:

    pass_credits = validate_credit_input(input("Please enter your credits at pass: "))
    defer_credits = validate_credit_input(input("Please enter your credits at defer: "))
    fail_credits = validate_credit_input(input("Please enter your credits at fail: "))
    outcome = calculate_progression_outcome(pass_credits, defer_credits, fail_credits)
    outcomes.append(outcome)
    credit_data.append([pass_credits, defer_credits, fail_credits])
    print(outcome)
    if check.upper() == "S":
        break

    while True:
        quit_program = input("Enter 'y' for yes or 'q' to quit and view results: ")
        if quit_program == "q":
            generate_histogram(outcomes)
            print("Progression outcomes:")
            for i, outcome in enumerate(outcomes):
                data_str = ", ".join(str(x) for x in credit_data[i])
                print(f"{i+1}. {outcome} - {data_str}")
            break
        elif quit_program == "y":
            break
        else:
            print("Invalid input. Please enter 'y' or 'q'.")
    
    if quit_program == "q":
        break
