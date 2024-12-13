import json
def save_borrower(all_borrowers):
    with open("all_borrowers.json", "w") as bfp:
        json.dump(all_borrowers, bfp, indent=4)