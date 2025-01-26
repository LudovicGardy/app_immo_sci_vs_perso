# Immobilier : Stratégie d'achat en tant que président d'une société

## 📄 Overview
🏡 Cette application compare deux options d'investissement pour l'achat d'un bien immobilier utilisé comme résidence principale :

1. **Achat personnel avec les dividendes d'une SASU à l'IS.**
2. **Achat via holding et SCI à l'IS, avec une SASU à l'IS comme société d'exploitation .**

### Fonctionnalités

- **Calculs financiers détaillés** pour chaque option.
- **Interface interactive** avec Streamlit.
- **Visualisations graphiques** pour comparer les coûts.

🌐 Access the app and start your exploration now at [@Not implemented yet](https://wikipedia.com).

![Image1](images/image1.0.png)

## Prerequisites

- **Anaconda or Miniconda**: For easy environment management (optional)
- **Docker** (optional): To run the app in a containerized setup
- **Python 3.12**

## ⚙️ Installation and Setup

This project uses **Poetry** for dependency management, which offers an option to create virtual environments directly. You have two choices to set up your environment:

### Option 1: Using Poetry to Create and Manage the Virtual Environment

Poetry can handle the creation and activation of a virtual environment automatically, without needing Conda or other virtual environment tools.

#### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/LudovicGardy/the_project_name
    cd the_project_name
    ```

2. **Install Dependencies and Create the Environment**:
   - Run the following command to let `poetry` create an isolated environment and install dependencies directly:
     ```bash
     poetry install --no-root
     ```

3. **Activate the Environment**:
   - Poetry automatically creates a virtual environment, but it may not activate it by default. Use the following command to activate it:
     ```bash
     poetry shell
     ```

4. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

#### Note on Poetry-managed Environments

Using `poetry install` to create and activate an environment directly is a streamlined approach, making Conda unnecessary. This can be ideal if you want a simple, Python-only virtual environment managed by `poetry`.

---

### Option 2: Using Conda for Virtual Environment Management

If you prefer using Conda, follow these steps:

#### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/LudovicGardy/the_project_name
    cd the_project_name
    ```

2. **Create and Activate the Conda Environment**:
   - **Using Conda** (recommended):
       ```bash
       conda create -n myenv python=3.11
       conda activate myenv
       ```

3. **Install Dependencies with Poetry**:
   - Once the environment is active, install dependencies within it:
     ```bash
     poetry install --no-root
     ```

4. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

---

### Option 3: Run the App with Docker

If you prefer to run the application in a containerized setup, use Docker.

#### Steps

1. **Prepare Docker environment**
    - Ensure Docker is installed and running on your system.

2. **Navigate to project directory**
    - For multiple containers:
        ```bash
        cd [path-to-app-folder-containing-docker-compose.yml]
        ```
    - For a single container:
        ```bash
        cd [path-to-app-folder-containing-Dockerfile]
        ```

3. **Build the containers**
    - For multiple containers:
        ```bash
        docker-compose up --build
        ```
    - For a single container:
        ```bash
        docker build -t my-app-title .
        ```

4. **Run the containers**
    - For multiple containers:
        ```bash
        docker run -p 8501:8501 my-app-title
        ```
    - The application will be accessible at `http://localhost:8501`.

5. **Other notes**

    - ⚠️ If you encounter issues with `pymssql`, adjust its version in `requirements.txt` or remove it before building the Docker image.
    - ⚠️ If you encounter issues with `pyspark`, you might need to uninstall and reinstall it. Additionally, ensure that Java is installed and properly configured on your system, as `pyspark` depends on Java. You can install Java by following the instructions on the [official Java website](https://www.java.com/en/download/help/download_options.html). Make sure to set the `JAVA_HOME` environment variable to point to your Java installation directory.


---

## 🧪 Running Unit Tests

Poetry can also manage unit tests to help you verify that the application functions as expected. This project uses **pytest** for testing.

### Setting Up and Running Tests

1. **Add Testing Dependencies**:

   If `pytest` and other test dependencies are not yet added, include them using Poetry:
   ```bash
   poetry add --dev pytest
   ```

2. **Writing Tests**:

   - Place your test files in a `tests` directory at the root of the project.
   - Name your test files following the pattern `test_*.py`.

3. **Running Tests**:

   To run tests within the Poetry environment, use:
   ```bash
   poetry run pytest
   ```

   Alternatively, if you are in an activated Poetry shell (`poetry shell`), you can simply run:
   ```bash
   pytest
   ```

4. **Viewing Test Results**:

   - Test results will appear in the terminal, with a summary of passed, failed, and skipped tests.
   - Use `pytest -v` for more detailed output.

---

## 👤 Author

- **LinkedIn**: [Ludovic Gardy](https://www.linkedin.com/in/ludovic-gardy/)
- **Website**: [https://www.sotisanalytics.com](https://www.sotisanalytics.com)