#DJ, 1st, Crew Shares


#User inputs for calculations
crew_members = int(input(f"How many crew members are there?(Not including the captain and first mate): ").strip())
total_earned = int(input(f"How much money did the crew makes?: ").strip())


shares = int(total_earned / (crew_members + 10))



#Print results
print(f"Each crew member recieves ${shares - 500}")
print(f"The first mate recieves ${shares * 3}")
print(f"The captian receives ${shares * 7}")