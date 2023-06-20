import time
import sys
import psutil

if __name__ == '__main__':

    cpu_count = int(sys.argv[1])
    CPU_SUM = 0
    CPU_100SUM = 0
    MEM_SUM = 0
    header_columns = []
    columns = []


    with open(str(cpu_count) + 'cores_cpu_summary.csv', 'w') as f:
        header_columns = ["TIME", "CPU_SUM", "CPU_100%SUM", "MEM_SUM"]
        f.write(",".join(header_columns) + "\n")

    while True:
        # 获取CPU使用率
        cpu_percentages = psutil.cpu_percent(interval=1, percpu=True)
        # 获取内存使用率
        mem_info = psutil.virtual_memory()
        # 把CPU使用率和内存使用率合计并打印
        for j in range(cpu_count):
            print(f"CPU{j+1} usage: {cpu_percentages[j]}%")
            CPU_SUM = CPU_SUM + cpu_percentages[j]
            CPU_100SUM = CPU_SUM / (cpu_count * 100)
            MEM_SUM = (mem_info.used / (1024.0 ** 3)) / (mem_info.total / (1024.0 ** 3))
            TIME  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print("---")
        print("TIME: ", TIME)
        print("CPU_SUM: ", CPU_SUM, "%")
        print("CPU_100%SUM: ", CPU_100SUM, "%"),
        print("MEM_SUM: ", mem_info.used / (1024.0 ** 3), "GB/", mem_info.total / (1024.0 ** 3), "GB")
        print("MEM_SUM%: ", MEM_SUM, "%")
        print("---")

        columns.append(TIME)
        columns.append(str(CPU_SUM))
        columns.append(str(CPU_100SUM))
        columns.append(str(MEM_SUM))

        f = open(str(cpu_count) + 'cores_cpu_summary.csv', 'a')
        f.write(",".join(columns) + "\n")

        CPU_SUM = 0
        CPU_100SUM = 0
        MEM_SUM = 0
        columns = []
        
        time.sleep(1)