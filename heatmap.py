import subprocess


command = [
    "python", "HiCPlotter.py",
    "-f", "data/HiC/Mouse/mES.chr2",
    "-n", "mES",
    "-o", "outputs/heatmap",
    "-chr", "chr2",

    #  "-r", "25000",
    #  "-da", "1",
    #  "-mm", "6",
    #  "-spi", "1",
    #  "-t", "HUVEC.E122.states.bed NHEK.E127.states.bed",
    #  "-tl", "States States",
    #  "-s", "1940",
    #  "-e", "2156",
    #  "-hist", "HUVEC.H3K9me3.bedGraph,Huvec.CTCF.bedGraph NHEK.H3K9me3.bedGraph,Nhek.CTCF.bedGraph",
    #  "-hl", "H3K9me3,CTCF H3K9me3,CTCF",
    #  "-si", "1",
    #  "-hc", "FF78B7,85d8e6 FF78B7,85d8e6",
    #  "-fhist", "1,0 1,0",
    #  "-hm", "18,600 18,600",
    #  "-c", "1",
    #  "-a", "HUVEC.Arrowhead.txt NHEK.Arrowhead.txt",
    #  "-al", "Domains Domains",
    #  "-ac", "cecece cecece",
    #  "-g", "Sox9genes.sorted.bed",
]

result = subprocess.run(command)

print("returncode: ", result.returncode)
print("result: ", result)
