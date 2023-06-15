import subprocess
import time
import multiprocessing

def split_line(line):
    # 拆分为两部分，前一部分包含前11个元素，后一部分包含剩余的元素
    elements = line.split()

    # 分成两部分，前一部分包含前11个元素，后一部分包含剩余的元素
    process = elements[:11]
    # 将后一部分中的COMMAND拆分出来
    back = ' '.join(elements[11:])

    # 将COMMAND添加到process中
    process.append(back)

    return process

def get_top_info():

    # f = open('cpu_summary.csv', 'w')
    # header_columns = []
    # columns = []
    # header_columns.append("PID")
    # header_columns.append("USER")
    # header_columns.append("PR")
    # header_columns.append("NICE")
    # header_columns.append("VIRT")
    # header_columns.append("RES")
    # header_columns.append("SHR")
    # header_columns.append("status")
    # header_columns.append("％CPU")
    # header_columns.append("％MEM")
    # header_columns.append("TIME+")
    # header_columns.append("COMMAND")
    # f.write(",".join(header_columns) + "\n")

    # 执行top命令并获取输出
    # top -b -d 0.2 -n 1000 -w 512 -c -H -i
    top_output = subprocess.check_output(['top', '-b', '-n', '1', '-w', '512', '-c', '-H', '-i'])
    top_output = top_output.decode('utf-8')  # 将输出从字节转化为字符串

    # 寻找以PID USER PR NI等开始的那一行
    lines = top_output.split("\n")
    # splited_lines = []
    CPU_SUM = 0
    MEM_SUM = 0
    for i in range(len(lines)):
        if lines[i].strip().startswith("PID USER"):
            # 找到该行后，将该行之后的所有行作为进程信息
            process_info_lines = lines[i+1:]
            
            for i in range(len(process_info_lines)-1):
                line = process_info_lines[i]
                # 总CPU使用率和总MEM使用率
                CPU_SUM += float(split_line(line)[8])
                MEM_SUM += float(split_line(line)[9])
            
            break
    # print(splited_lines)
    print("TIME: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "JST")
    print("CORES: ", multiprocessing.cpu_count())
    print("CPU_SUM: ", CPU_SUM, "%")
    print("CPU_100%SUM: ", CPU_SUM / (multiprocessing.cpu_count() * 100), "%")
    print("MEM_SUM: ", MEM_SUM, "%")

print(get_top_info())