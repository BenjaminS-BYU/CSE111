import math
def main():
    most_cost_eff = 0
    most_cost_name = ""
    most_storage_eff = 0
    most_storage_name = ""

    with open("can_sizes_list.txt") as can_list:
        next(can_list)
        for item in can_list:
            item_split = item.strip().split(",")
            name:str = item_split[0]
            radius:float = float(item_split[1])
            height:float = float(item_split[2])
            cost:float = float(item_split[3].strip().lstrip("$"))

            volume_cal = math.pi * radius **2 * height
            surface_area = 2*math.pi*radius*(radius + height)
            storage_eff = volume_cal/surface_area
            cost_eff = volume_cal/cost

            if cost_eff > most_cost_eff:
                most_cost_eff = cost_eff
                most_cost_name = name

            if storage_eff > most_storage_eff:
                most_storage_eff = storage_eff
                most_storage_name = name



            print(f"--- {name} ---")
            print(f"Volume: {volume_cal:.2f}")
            print(f"Surface Area: {surface_area:.2f}")
            print(f"Storage Efficiency: {storage_eff:.2f}")
            print(f"Cost Efficiency: ${cost_eff:.2f}\n")

    print(f"\nMost storage efficient can: {most_storage_name} ({most_storage_eff:.2f})")
    print(f"Most cost efficient can: {most_cost_name} $({most_cost_eff:.2f})")
    
main()
