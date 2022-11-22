weight = 80 


if weight >= 10:
  ground_cost = 4.75 * weight + 20
elif weight >= 6:
  ground_cost = 4.0 * weight + 20
elif weight >= 2:
  ground_cost = 3.0 * weight + 20
else:
  ground_cost = 1.5 * weight + 20


ground_cost_premium = 125

if weight >= 10:
  drone_cost = 14.25 * weight 
elif weight >= 6:
  drone_cost = 12.00 * weight 
elif weight >= 2:
  drone_cost = 9.00 * weight 
else:
  drone_cost = 4.50 * weight


print("Ground cost: $" + str(ground_cost))
print("Ground cost premium: $ " + str(ground_cost_premium))
print("Drone cost: $" + str(drone_cost))
