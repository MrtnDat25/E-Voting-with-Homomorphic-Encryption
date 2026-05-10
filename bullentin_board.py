import os 

from config import *

def display_bulletin_board():
    print("\n" + "="*20 +"Election BULLETIN BOARD " + "="*20)

    if not os.path.exists("bulletin_board.txt"):
        print("\nThe bullentin board is currently blank. No vote(s) has been recoreded yet")

        print("="*40)
        return
    
    print(f"{'Voted ID': <40} | {'Encrypted ballot':<50}")
    print("="*40)

    with open("bulletin_board.txt", 'r') as f:
        lines = f.readlines()
        if not lines:
            print("No data")
        else:
            for line in lines:
                parts = line.strip().split()
                if len(parts) >=2 :
                    v_id = parts[0]

                    #
                    enc_val = parts[1]
                    display_enc = (enc_val[:45] + '...') if len(enc_val) >45 else enc_val
                    print(f"{v_id:<40} | {display_enc:<50}")
    print("="*50)
    print(f"\nTotal number of votes currently on the bulletin board: {len(lines)}")


def search_vote():
    """
    lookup id
    """

    if not os.path.exists("bulletin_board.txt"):
        return
    
    print("\n[Lookup Ballot]")

    search_id = input("Enter your vote id: ").strip()
    found = False

    with open("bulletin_board.txt", "r") as f:
        for line in f:
            v_id, enc_val = line.strip().split()
            if v_id == search_id:
                print(f"\n[v] CONFIRMATION: Your ballot is now in the system.!")
                print(f"Full code: {enc_val}")
                found = True
                break

    if not found :
        print("\n[x]WARNING: This Vote ID was not found. Please check again.!")

if __name__ == "__main__":
    while True:
        display_bulletin_board()
        print("\nSelection :")
        print("1. Look up votes using Vote ID")

        print("2. Refresh the news feed")

        print("3. Exit")

        choice = input("Enter your selection: ")

        if choice == '1':
            search_vote()
            input("\nPress Enter to continue...")
        elif choice == '2':
            continue

        elif choice == '3':
            break

        else:
            print("Invalid selection")

