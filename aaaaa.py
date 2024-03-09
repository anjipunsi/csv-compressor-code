import gzip
import shutil
import os

# Path to the input CSV file
input_file_path = 'anj.csv'

# Path to the output compressed file
output_file_path = 'path_to_your_output_file.csv'

# Compress the file
with open(input_file_path, 'rb') as f_in:
    with gzip.open(output_file_path + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Calculate the compression ratio
original_size = os.path.getsize(input_file_path)
compressed_size = os.path.getsize(output_file_path + '.gz')
compression_ratio = (compressed_size / original_size) * 100

print(f"Original size: {original_size} bytes")
print(f"Compressed size: {compressed_size} bytes")
print(f"Compression ratio: {compression_ratio:.2f}%")

# Rename the compressed file to remove the .gz extension
os.rename(output_file_path + '.gz', output_file_path)
