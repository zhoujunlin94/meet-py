import psutil

def netstat_ano():
    connections = psutil.net_connections(kind='inet')  # 包括 TCP 和 UDP
    results = []

    for conn in connections:
        laddr = f"{conn.laddr.ip}" if conn.laddr else "-"
        lport = f"{conn.laddr.port}" if conn.laddr else "-"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
        status = conn.status
        pid = conn.pid if conn.pid is not None else "-"
        results.append([laddr, lport, raddr, status, pid])
    
    return results


def printNetStatus(netStats):
    print(f"{'Local Address':<15}{'Local Port':<15}{'Remote Address':<15}{'Status':<15}{'PID':<6}")
    print("-" * 70)
    for row in netStats:
        print(f"{row[0]:<15}{row[1]:<15}{row[2]:<15}{row[3]:<15}{row[4]:<6}")

def kill_process_by_pid(pid: int):
    try:
        proc = psutil.Process(pid)
        proc.terminate()  # 尝试优雅终止
        # proc.wait(timeout=3)  # 最多等待 3 秒
        print(f"成功终止进程 PID={pid}，名称={proc.name()}")
    except psutil.NoSuchProcess:
        print(f"错误：找不到 PID={pid} 的进程")
    except psutil.TimeoutExpired:
        print(f"警告：进程 PID={pid} 未及时响应，尝试强制杀死")
        proc.kill()
        print(f"已强制杀死 PID={pid}")
    except psutil.AccessDenied:
        print(f"权限错误：无权终止 PID={pid} 的进程")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    netStats = netstat_ano()
    filteredNet = [net for net in netStats if net[1] == '5500']
    printNetStatus(filteredNet)
    if filteredNet:
        pid = filteredNet[0][4]
        print(pid)
        kill_process_by_pid(pid)