import subprocess


# python HiCPlotter.py 
# -f data/HiC/Mouse/mES.chr2 
# -n mES 
# -chr chr2 
# -r 40000 
# -o HoxD 
# -hist data/HiC/Mouse/GSM1334415_4C_Mouse_EScells_Hoxd4_smoothed_11windows.bedGraph,data/HiC/Mouse/GSM1334440_4C_Mouse_E9.5TB_Hoxd4_smoothed_11windows.bedGraph,data/HiC/Mouse/GSM1334412_4C_Mouse_EScells_Hoxd13_smoothed_11windows.bedGraph,data/HiC/Mouse/GSM1334437_4C_Mouse_E9.5TB_Hoxd13_smoothed_11windows.bedGraph,data/HiC/Mouse/GSM747534_ChIPseq_CTCF_ES_rep1.chr2.bedGraph 
# -hl Hoxd4
# -ES,Hoxd4
# -Tail,Hoxd13
# -ES,Hoxd13
# -Tail,CTCF
# -ES 
# -s 1830 
# -e 1880 
# -fh 0 
# -pi 0 
# -pcd 1 
# -pcdf data/mES_domains_mm9.bed 
# -fhist 1,1,1,1,0 
# -hm 2000,2000,2000,2000,50


command = [
    "python", "HiCPlotter.py",
    "-f", "data/HiC/Mouse/mES.chr2",
    "-n", "mES",
    "-o", "outputs/heatmap.png",
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
