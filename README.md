# TNA - Experimental

![Python Version Compatibility](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20-blue)

Deployment URL: [Azure](https://TODO.azurewebsites.net/)


# Inputs and Outputs

## MongoDB Uri credentials
The MongoDB credentials are stored in json format [secrets.json](resources/secrets.json). This only needs to be altered if the database connection for the project changes.

# Developer Guidelines 

## Requirements

### Installing Dependencies
- Install through the local requirements file.
```
pip install -r requirements.txt
```

### Adding a Dependency
- run "pipreqs" whenever adding a new dependency.
```
python .\src\generate_requirements.py
```

## Project Deployment
### Azure Deployment
- Azure deployment is automated, and run in a CI/CD pipeline whenever this repository receives a new commit. The recommended configurations are as follows:
    - Python version: 3.10 (any between 3.10 - 3.12)
    - Azure Startup Configuration: 
    ```
    python -m streamlit run Home.py --server.port 8000 --server.address 0.0.0.0
    ```
    
### Local Deployment
- Project can also be deployed locally with:

```
streamlit run Home.py
```

## Style Guide
- Developers should follow PEP8 when writing code. The official formatter is `black` and imports are organized with `isort`. See [pyproject.toml](pyproject.toml) for formatter configurations and compatibility.