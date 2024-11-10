import hmac
import os
from typing import Any

import numpy as np
import toml
from dotenv import find_dotenv, load_dotenv


def check_password(st) -> bool:
    """Returns `True` if the user had the correct password."""

    def password_entered():
        env_variables = load_configurations()
        pw = str(env_variables.get("PASSWORD"))

        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], pw):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


def load_configurations() -> dict[str, Any]:
    """
    Charge uniquement les variables du fichier .env si celui-ci est présent.
    Si le fichier .env n'existe pas, charge toutes les variables d'environnement du système.
    """
    dotenv_path = find_dotenv(".env")

    if dotenv_path:
        # The .env file exists, load only its variables
        load_dotenv(dotenv_path)
        # Return the variables loaded from the .env
        return {
            key: os.environ[key]
            for key in os.environ
            if key in open(dotenv_path).read()
        }
    else:
        # The .env file does not exist, return all the system environment variables
        return dict(os.environ)


def load_toml_config(file_path: str) -> dict[str, Any]:
    """
    Charge les configurations à partir d'un fichier .toml
    """
    try:
        with open(file_path, "r") as file:
            return toml.load(file).get("theme", {})
    except FileNotFoundError:
        raise FileNotFoundError("config.toml file not found")


def page_config() -> dict[str, Any]:
    """
    Set the page configuration (title, favicon, layout, etc.)
    """
    env_variables = load_configurations()
    toml_config = load_toml_config(".streamlit/config.toml")

    page_dict = {
        "page_title": toml_config.get("page_title", "Dividendes SASU vs SCI"),
        "sidebar_title": f"# {toml_config.get('sidebar_title', 'Dividendes SASU vs SCI')}",
        "base": toml_config.get("base", "dark"),
        "page_icon": f'{env_variables.get("AWS_S3_URL", "")}/Sotis_AI_pure_darkbg_240px.ico',
        "page_logo": f'{env_variables.get("AWS_S3_URL", "")}/Sotis_AI_pure_darkbg_240px.png',
        "layout": toml_config.get("layout", "centered"),
        "initial_sidebar_state": toml_config.get("initial_sidebar_state", "auto"),
        "author": "Sotis AI",
        "markdown": """<style>.css-10pw50 {visibility:hidden;}</style>""",
        "page_description": """
        Une application pour comparer les coûts d'achat d'un bien immobilier en 
        France en tant que président d'une société.
        \n\nDeux possibilités explorées :
        \n\n  - [Perso] SASU IS + dividendes
        \n\n  - [Pro] EURL IS + Holding + SCI
        \n\nDans cette situation, bénéficier du régime mère-fille peut être intéressant 
        comparativement à sortir des revenus sous formes de salaires ou de dividendes.
        \n\nSi achat pro, le président devra verser un loyer à la SCI. Néanmoins en 
        fonction du loyer à verser et du prix du bien, le temps pour que le prix à payer
        en loyers rattrape le prix des taxes sur les dividendes peut être plus ou moins long.
        """,
    }

    return page_dict


def data_URL() -> dict[str, Any]:
    """
    Set the URLs to the data sources.
    """

    env_variables = load_configurations()

    data_dict = {
        "summarized_data_url": f'{env_variables["AWS_S3_URL"]}/geo_dvf_summarized_full.csv.gz',
        "datagouv_source_URL": env_variables["DATA_GOUV_URL"],
        "available_years_datagouv": list(np.arange(2018, 2023 + 1)),
        "scrapped_year_current": f'{env_variables["AWS_S3_URL"]}/2024_merged/departements',
    }

    return data_dict


def firebase_credentials() -> dict[str, str]:
    """
    Load configuration from .env file or from OS environment variables
    """

    # List of required keys in lowercase
    keys_list = [
        "type",
        "project_id",
        "private_key_id",
        "private_key",
        "client_email",
        "client_id",
        "auth_uri",
        "token_uri",
        "auth_provider_x509_cert_url",
        "client_x509_cert_url",
        "universe_domain",
    ]

    cred_dict = {}
    env_variables = load_configurations()

    # Check if all required keys exist and have a non-empty value
    try:
        for key in keys_list:
            value = env_variables.get(key.upper())
            if not value:
                raise ValueError(f"Missing or empty value for key: {key}")
            cred_dict[key] = value

        # Add prefix and suffix for the private_key
        cred_dict["private_key"] = cred_dict["private_key"].replace("/breakline/", "\n")
    except ValueError as e:
        cred_dict = {}  # Reset cred_dict if any key is missing or empty
        raise ValueError(
            f"Firebase credentials are missing or incomplete: check the .env file... {e}"
        )

    return cred_dict
