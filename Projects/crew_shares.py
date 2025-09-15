#DJ, 1st, Crew Shares


#User inputs for calculations
crew_members = float(input(f"How many crew members are there?(Not including the captain and first mate): ").strip())
total_earned = float(input(f"How much money did the crew makes?: ").strip())


shares = float(total_earned / (crew_members + 10))



#Print results
print(f"Each crew member recieves ${(shares - 500):.2f}")
print(f"The first mate recieves ${(shares * 3):.2f}")
print(f"The captian receives ${(shares * 7):.2f}")