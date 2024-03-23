#!/usr/bin/env python3


import re
import os

time_pattern = re.compile(r":time-seconds (.*)")
mem_pattern = re.compile(r":memory-mb (.*)")
calls_pattern = re.compile(r"total-calls (.*)") #multiple instances of this one

def main():
    operations = ["a", "adms", "as", "dm", "m"]
    difficulties = ["easiest", "easy", "medium", "hard"]

    overall_count = 0
    overall_time_avr = 0
    overall_mem_avr = 0
    overall_calls_avr = 0
    
    overall_time_worst = 0
    overall_mem_worst = 0
    overall_calls_worst = 0

    for op in operations:
        op_count = 0
        op_time_avr = 0
        op_mem_avr = 0
        op_calls_avr = 0
        
        op_time_worst = 0
        op_mem_worst = 0
        op_calls_worst = 0
        print(op)
        
        for diff in difficulties:
            diff_count = 0
            diff_time_avr = 0
            diff_mem_avr = 0
            diff_calls_avr = 0
            
            diff_time_worst = 0
            diff_mem_worst = 0
            diff_calls_worst = 0
            print(diff)

            for filename in os.listdir(f"./7/{op}/{diff}"):
                if filename.endswith("-puzzle.txt"):
                    overall_count += 1
                    op_count += 1
                    diff_count += 1

                    os.system(f"./kenken2smt.py <./7/{op}/{diff}/{filename} >puzzle.smt")
                    os.system("mathsat -stats <puzzle.smt >model.smt")
                    
                    stat_txt = open("model.smt", "r")
                    curr_stats = stat_txt.read()
                    stat_txt.close()


                    time = time_pattern.search(curr_stats)
                    mem = mem_pattern.search(curr_stats)
                    calls = calls_pattern.findall(curr_stats)


                    if time:
                        x = float(time.group(1))
                        if x > overall_time_worst:
                            overall_time_worst = x
                            
                        if x > op_time_worst:
                            op_time_worst = x
                            
                        if x > diff_time_worst:
                            diff_time_worst = x

                        overall_time_avr += x
                        op_time_avr += x
                        diff_time_avr += x


                    if mem:
                        x = float(mem.group(1))
                        if x > overall_mem_worst:
                            overall_mem_worst = x
                            
                        if x > op_mem_worst:
                            op_mem_worst = x
                            
                        if x > diff_mem_worst:
                            diff_mem_worst = x

                        overall_mem_avr += x
                        op_mem_avr += x
                        diff_mem_avr += x


                    if calls:
                        for call in calls:
                            x += int(call)
                        
                        if x > overall_calls_worst:
                            overall_calls_worst = x
                            
                        if x > op_calls_worst:
                            op_calls_worst = x
                            
                        if x > diff_calls_worst:
                            diff_calls_worst = x

                        overall_calls_avr += x
                        op_calls_avr += x
                        diff_calls_avr += x
            
            print("diff avr:", diff_time_avr/diff_count, diff_mem_avr/diff_count, diff_calls_avr/diff_count, "diff worst:", diff_time_worst, diff_mem_worst, diff_calls_worst)
        print("op avr:", op_time_avr/op_count, op_mem_avr/op_count, op_calls_avr/op_count, "op worst:", op_time_worst, op_mem_worst, op_calls_worst)
    print("overall avr:", overall_time_avr/overall_count, overall_mem_avr/overall_count, overall_calls_avr/overall_count, "overall worst:", overall_time_worst, overall_mem_worst, overall_calls_worst)
    



if __name__ == "__main__":
    main()