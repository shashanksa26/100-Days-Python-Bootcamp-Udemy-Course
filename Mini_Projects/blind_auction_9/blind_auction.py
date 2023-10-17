import os
from art import logo
print(logo)
bids={}
bidding_finished=False

def all_bids(bids):
    print("All bidding done are: ")
    for bidder in bids:        
        print(f"{bidder} : ${bids[bidder]}")

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:        
        bid_amount = bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    all_bids(bids)
    

while not bidding_finished:
    name=input("What is your name?: ")
    price=int(input("What's your bid?: "))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'y' or 'n'. :")
    if should_continue=="n":
        bidding_finished=True
        find_highest_bidder(bids)

    elif should_continue=="y":
        os.system('cls')