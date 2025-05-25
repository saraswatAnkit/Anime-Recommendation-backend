import requests

def search_anime(query=None, genre=None):
    url = "https://graphql.anilist.co"
    graphql_query = '''
    query ($search: String, $genre: String) {
        Page(perPage: 10) {
            media(search: $search, genre_in: [$genre], type: ANIME) {
                id
                title {
                    romaji
                }
                genres
                popularity
            }
        }
    }
    '''
    variables = {
        "search": query,
        "genre": genre
    }
    response = requests.post(url, json={'query': graphql_query, 'variables': variables})
    return response.json()