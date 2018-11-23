from pathlib import Path
import pandas as pd

# this is nice and concise but takes way too long
def do_merge(csvs):
    merged = pd.concat(map(pd.read_csv, csvs))
    return(merged)

def concat_csvs(infolder: str, outfolder: str):
    p = Path(infolder)
    print(f"Searching for all .csv files below: {infolder}")
    csvs = p.rglob("*.csv")
    csvs = list(filter(lambda x: not x.is_dir(), csvs))
    print(f"Found {len(csvs)} .csv files")
    csv_unique_names = set(list(map(lambda x: x.name, csvs))) 
    print(f"Unique file names: {csv_unique_names}")
    for name in csv_unique_names:
        print(f"####### Processing {name}")
        print("Read and merge")
        subset = filter(lambda x: x.name == name, csvs)
        merged = do_merge(subset)
        outfile = str(Path(outfolder) / name.replace(".csv","_concat.csv"))
        print(f"Save merged to outfile: {outfile}")
        #print(merged.head())
        merged.to_csv(outfile)

#concat_csvs('/scratch/su62/naderer_for_cp/Full_Plates/Seong_splitted', '/scratch/su62/naderer_for_cp/Full_Plates/Seong_splitted')