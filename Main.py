
_STATUS_OPEN = "open"
_AGE_DAYS_MIN = 2

from ticket_data import TICKETS



def check_validation(ticket):
    list_of_tickets = []
    try:
        id = ticket["id"]
        status = ticket["status"]
        category = ticket["category"]
        age_days = ticket["age_days"]
        priority = ticket["priority"]
        correct = 0
        if id != "":
            correct += 1
        if status == "open" or status == "closed":
            correct += 1
        if category == "software" or category == "network" or category == "access":
            correct += 1
        if isinstance(age_days, int) and not isinstance(age_days, bool) and age_days >= 0:
            correct += 1
        if priority == "low" or priority == "normal" or priority == "high":
            correct += 1
        if correct == 5:
                list_of_tickets.append({
                    "id": id,
                    "status": status,
                    "category": category,
                    "age_days": age_days,
                    "priority": priority
                })
    except:
        return []
    if len(list_of_tickets) == 0:
        print("No valid tickets found.")
    return list_of_tickets
def check_missing(field, ticket):
    try:
        field_value = ticket[field]
        return field_value


def check_tickets():
    for each in check_validation(ticket):
        if each["status"] == _STATUS_OPEN and each["age_days"] >= _AGE_DAYS_MIN:
            print(each)


def main():
    list_of_tickets = []
    #print(check_validation())
    check_tickets()






if __name__ == "__main__":
    main()


    
