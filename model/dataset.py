from datasets import load_dataset
import pandas
def get_dataset(excel_file):
    data=pandas.read_excel(excel_file)
    ff = open("data.json", "w")
    ff.write(data.to_json(orient='records', lines=True))
    ff.close()
    dataset = load_dataset("json", data_files="data.json", split="train")
    new_dataset = dataset.train_test_split(test_size=0.2, shuffle=True)
    return new_dataset

