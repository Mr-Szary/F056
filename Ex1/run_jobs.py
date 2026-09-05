import multiprocessing 
import subprocess

def run_job(num_job):

    name = f"output_py_{num_job}.txt"

    with open(name, "w") as output:
        subprocess.run(
            ["./hello", str(num_job)],
                stdout=output,
                text=True
                      )

    if __name__ == "__main__":
        processos = []

    for i in range(1,10):
        mp = multiprocessing.Process(target=run_job, args=(i,))
        processos.append(mp)
        mp.start()

    for mp in processos:
        mp.join()
