from algoliasearch.search_client import SearchClient

from config.settings.base import env

client = SearchClient.create("V0U0845ZUX", env("ALGOLIA_ADMIN_API_KEY"))
index = client.init_index("test_help_guru_user_data")
