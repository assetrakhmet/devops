

servers,daily_updated_servers =212, 8

full_day = servers // daily_updates_servers

print("They will doing updates for",full_day,"full_days.")

outdated_servers = servers % daily_updated_servers 

print ("we will have", outdated_servers,)