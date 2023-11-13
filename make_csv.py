import json
import csv
import os

target_files = ['1384392.json', '1384393.json', '1384394.json', '1384395.json', '1384396.json', '1384397.json', '1384398.json', '1384399.json', '1384400.json', '1384401.json', '1384402.json', '1384403.json', '1384404.json', '1384405.json', '1384406.json', '1384407.json', '1384408.json', '1384409.json', '1384410.json', '1384411.json', '1384412.json',
                '1384413.json', '1384414.json', '1384415.json', '1384416.json', '1384417.json', '1384418.json', '1384419.json', '1384420.json', '1384421.json', '1384422.json', '1384423.json', '1384424.json', '1384425.json', '1384426.json', '1384427.json', '1384428.json', '1384429.json', '1384430.json', '1384431.json', '1384432.json', '1384433.json']

json_folder = "C:/Semisters/SEM-05/IT496 - Data Mining/Assignment-3/matches_data_json"
csv_file_path = "C:/Semisters/SEM-05/IT496 - Data Mining/Assignment-3/datasets/batsmen.csv"


def flatten_innings(innings_data, match_date, winner, venue):
    flattened_data = []

    for inning_number, inning in enumerate(innings_data, start=1):
        team = inning["team"]
        for over_data in inning["overs"]:
            over_number = over_data["over"]
            for delivery_number, delivery in enumerate(over_data["deliveries"], start=1):
                ball_count = over_number * 6 + delivery_number
                row_data = {
                    "Date": match_date,
                    "Winner": winner,
                    "Inning": inning_number,
                    "Team": team,
                    "Over": over_number,
                    "Balls": ball_count,
                    "Batsman": delivery["batter"],
                    "Bowler": delivery["bowler"],
                    "Non_Striker": delivery["non_striker"],
                    "Runs": delivery["runs"]["batter"],
                    "Extras": delivery["runs"]["extras"],
                    "Total_Runs": delivery["runs"]["total"],
                    "Venue": venue,
                }

                wickets = delivery.get("wickets")
                if wickets:
                    for wicket in wickets:
                        row_data.update({
                            "Wicket": "Out",
                            "Wicket_Type": wicket["kind"],
                        })
                else:
                    row_data.update({
                        "Wicket": "Not Out",
                        "Wicket_Type": "None",
                    })
                flattened_data.append(row_data)
    return flattened_data


for file_name in target_files:
    json_file_path = os.path.join(json_folder, file_name)

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)

        match_date = json_data["info"]["dates"][0]
        winner = json_data["info"]["outcome"]["winner"]
        venue = json_data["info"]["venue"]

        flattened_innings_data = flatten_innings(
            json_data["innings"], match_date, winner, venue)

        with open(csv_file_path, 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(
                csv_file, fieldnames=flattened_innings_data[0].keys())

            if os.path.getsize(csv_file_path) == 0:
                csv_writer.writeheader()

            csv_writer.writerows(flattened_innings_data)
    else:
        print(f"File not found: {json_file_path}")

print("Conversion and appending completed.")
