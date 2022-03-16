import time
from psutil import disk_usage as d_usg, cpu_percent as cpu_per, virtual_memory as vm


async def bot_sys_stats():
    botStartTime = time.time()
    usage_disk = d_usg()
    usage_cpu = cpu_per()
    vir_mem = vm()
    uptime = int(time.time() - botStartTime)
    uptime_stats = f"""
Bot alive✅
UPTIME: {uptime}
CPU: {usage_cpu}%
RAM: {vir_mem}%
DISK: {usage_disk}%
"""
    return uptime_stats