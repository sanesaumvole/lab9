# generate_models.py
import subprocess

# Generate model for products.json
subprocess.run(["python", "-m", "datamodel_code_generator", "--input", "products.json", "--input-file-type", "json", "--output", "product_model.py"])

# Generate model for stats.json
subprocess.run(["python", "-m", "datamodel_code_generator", "--input", "stats.json", "--input-file-type", "json", "--output", "stats_model.py"])

# Generate model for historical_data.json
subprocess.run(["python", "-m", "datamodel_code_generator", "--input", "historical_data.json", "--input-file-type", "json", "--output", "historical_data_model.py"])
