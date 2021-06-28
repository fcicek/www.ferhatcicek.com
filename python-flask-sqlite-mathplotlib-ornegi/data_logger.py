import time
import sqlite3
import psutil

dbname='system_usage.db'

ornekleme_zamani = 60

def sistem_bilgisi_oku():
    mem = psutil.virtual_memory()[2]
    cpu = psutil.cpu_percent(1)
    if mem is not None and cpu is not None:
        return cpu,mem

def veritabani_ekle (cpu, mem):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO system_usage values(datetime('now'), (?), (?))", (cpu, mem))
    conn.commit()
    conn.close()

def main():
    while True:
        cpu, mem = sistem_bilgisi_oku()
        veritabani_ekle (cpu, mem)
        time.sleep(ornekleme_zamani)

main()
