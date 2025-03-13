import yaml
import jsonschema

def main():
    # Load the schema
    with open("schema.json", "r") as schema_file:
        schema_dict = yaml.safe_load(schema_file)

    # Load the data to validate against schema
    with open("data.json", "r") as data_file:
        data_dict = yaml.safe_load(data_file)

    # Validate using the JSON Schema library
    jsonschema.validate(instance=data_dict, schema=schema_dict)
    print("Validation successful!")

if __name__ == "__main__":
    main()
