import pandas as pd
from src.duplicate_removal import remove_duplicates
def test_remove_duplicates():
   input_file = "data/dataset.csv"
   output_file = "data/processed_dataset.csv"
   cleaned_df = remove_duplicates(input_file, output_file)
   original_df = pd.read_csv(input_file)
   assert len(cleaned_df) <= len(original_df)
