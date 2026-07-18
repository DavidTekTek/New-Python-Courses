# PART 1: Ask the agent for their details
name = input("Enter your real name, Agent: ")
gadget = input("Enter your favorite gadget: ")

# PART 2: Store the agent's details using different data types
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

# PART 3: Print each detail along with its data type
print("Name:", name, "-> type:", type(name))
print("Gadget:", gadget, "-> type:", type(gadget))
print("Agent Number:", agent_number, "-> type:", type(agent_number))
print("Speed Rating:", speed_rating, "-> type:", type(speed_rating))
print("Mission Count:", mission_count, "-> type:", type(mission_count))
print("Height (m):", height_m, "-> type:", type(height_m))
print("Is Active:", is_active, "-> type:", type(is_active))

# PART 4: Typecast the numbers and true/false value into text
agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print("Agent Number as text:", agent_number_text, "-> type:", type(agent_number_text))
print("Mission Count as text:", mission_count_text, "-> type:", type(mission_count_text))
print("Speed Rating as text:", speed_rating_text, "-> type:", type(speed_rating_text))
print("Status as text:", status_text, "-> type:", type(status_text))

# PART 5: Slice the name to create a secret code name
first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Secret Code Name:", code_name)

# PART 6: Reverse the gadget name using slicing
reversed_gadget = gadget[::-1]
print("Reversed Gadget Name:", reversed_gadget)

# PART 7: Join everything together to build the final badge message
badge_line_1 = "AGENT " + code_name.upper()
badge_line_2 = "ID: " + agent_number_text + " | MISSIONS: " + mission_count_text
badge_line_3 = "SPEED: " + speed_rating_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET GADGET CODE: " + reversed_gadget.upper()

# PART 8: Print the complete secret agent badge
print("")
print("===== SECRET AGENT BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===============================")
