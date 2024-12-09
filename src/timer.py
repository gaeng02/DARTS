import re

input_path = "../experiments/cluster_logs"

target = [68752, 69233, 69371, 68360, 69429, 69578]

extension = "_1.o"

for tg in target :
    
    filepath = input_path + "/" + str(tg) + extension

    result = 0.0
    cnt = 0


    try :
        with open(filepath, "r") as file :

            print(" =================")
            print(f" Found file :: {tg}")
            
            for line in file :

                match = re.search(r"===\s+([\d.]+)\s+sec", line)

                if match :
                    result += float(match.group(1))
                    cnt += 1

            print(f" {result} \n {cnt} \n")

    except FileNotFoundError :
        print(f" No file :: {filepath}")
        
    except Exception as e :
        print(f" Except error :: {e}")


