from json import load

from algoliasearch.search_client import SearchClient

from config.settings.base import env

client = SearchClient.create("V0U0845ZUX", env("ALGOLIA_ADMIN_API_KEY"))
index_name = env("ALGOLIA_INDEX", default="test_help_guru_user_data")
index = client.init_index(index_name)
batch = load(open(f"{index_name}.json"))
index.save_objects(batch, {"autoGenerateObjectIDIfNotExist": True})
