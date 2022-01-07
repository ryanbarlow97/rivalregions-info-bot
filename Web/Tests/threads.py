from Toolbox.stats_collector import collect_stats

from Web.Toolbox.threader import myThread

stats_thread = myThread(1, "Stats_Thread-1", collect_stats(60, 2))
stats_thread.run()

while True:
    continue